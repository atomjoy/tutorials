# Google oauth login w Vue3
Logowanie za pomocą google oauth na stronie www.

## Konto google developer
Utwórz konto na <https://cloud.google.com/>

- utwórz aplikację
- dodaj ekran powitalny aplikacji z pozwoleniami
- dodaj/uruchom "Google+ Api" dla aplikacji
- utwórz klucz oauth Api credentials (pobierz json z danymi)
- ogranicz klucz dodając adresy uri aplikacji i do przekirowań
- dla localhost dodaj koniecznie podwójne uri <http://localhost> i <http://localhost:8000>

## Dodaj parametry w .env

```env
# produkcja
VITE_GOOGLE_OAUTH_REDIRECT="https://your.page.here/oauth/google"
VITE_GOOGLE_OAUTH_CLIENT_ID="YOUR-GOOGLE-CLIENT-ID.apps.googleusercontent.com"
VITE_GOOGLE_OAUTH_CLIENT_SECRET=""

# development
VITE_GOOGLE_OAUTH_REDIRECT="http://localhost/oauth/google"
```

## Tworzenie url dla przycisku

<https://developers.google.com/identity/protocols/oauth2/web-server?hl=pl#httprest_1>

```js
// utils/getGoogleUrl.js

export const getGoogleUrl = (from) => {
 const rootUrl = `https://accounts.google.com/o/oauth2/v2/auth`

 const options = {
  redirect_uri: import.meta.env.VITE_GOOGLE_OAUTH_REDIRECT,
  client_id: import.meta.env.VITE_GOOGLE_OAUTH_CLIENT_ID,
  scope: ['https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/userinfo.email'].join(' '),
  prompt: 'consent',
  state: from,

  // Get with access_token
  response_type: 'token',
  access_type: 'online',

  // Get with jwt id_token
  // JWT userinfo uri: https://oauth2.googleapis.com/tokeninfo?id_token=
  // response_type: 'id_token',
  // access_type: 'online',
  // nonce: 'random_string',

  // Get with code
  // Code userinfo uri request method POST to: `https://oauth2.googleapis.com/token`
  // response_type: 'code',
  // access_type: 'offline',
 }

 const params = new URLSearchParams(options)

 return `${rootUrl}?${params.toString()}`
}
```

## Tworzenie przycisku

```vue
<script setup>
import { getGoogleUrl } from '../utils/getGoogleUrl.js'
const from = '/login'
</script>

<template>
  <a :href="getGoogleUrl(from)" class="google-button">
    <img src="https://developers.google.com/static/identity/images/g-logo.png" width="30" height="30">
    <div>Sign in with Google</div>
  </a>
</template>

<style>
.google-button {
  display: flex;
  align-items: center;
  justify-items: center;
  padding: 10px 20px;
  color: #1a73e8;
  background: transparent;
  border: 3px solid #1a73e8;
  border-radius: 30px;
  cursor: pointer;
}
.google-button div {font-weight: 900;}
.google-button img {margin-right: 10px; border-radius: 30px;}
</style>
```

## Tworzenie strony na przekierowania z google oauth api

Ta część powinna być po stronie serwera (Node.js, Php, ...)

- Uri strony <http://localhost/oauth/google>
- Serwer powinien zweryfikować access_token i pobrać informacje o zalogowanym użytkowniku google
- Autoryzacja zapytania z Bearer tokenem o wartości access_token dla metody GET
- Pobierz google userinfo z <https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token=>
- Po pobraniu userinfo logujemy usera w php na serwerze
- Pozostaje przekirować na stronę główną lub panel klienta w vue

```vue
<script setup>
import { onMounted, reactive, ref } from 'vue'
import { useRoute, useRouter, RouterLink } from 'vue-router'
import axios from 'axios'

let user = ref(null)
let query = ref(null)
let token = ref(null)

async function getUser(access_token) {
 if (access_token) {
  try {
   axios.defaults.headers.common = { Authorization: `Bearer ${access_token}` }
   const data = await axios.get(`https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token=${access_token}`)
   console.log('Api data', data)
   return data
  } catch (err) {
   console.log('Api error', err)
   throw Error(err)
  }
 }
}

onMounted(async () => {
 const route = useRoute()
 query.value = route?.hash
 if (query.value) {
  console.log('Query', query.value)
  token.value = query.value.replace('#', '').split('=')[2].replace('&token_type', '')
  console.log('HashToken', token.value)
  user.value = await getUser(token.value)
 }
})
</script>
<template>
 <p>Api access_token: {{ token }}</p>
 <p>Api access_token: {{ user?.data }}</p>
</template>
```

## Pobierz access_token z code dla metody POST (node.js, Php serwer)

- <https://cloud.google.com/apigee/docs/api-platform/security/oauth/access-tokens>
- <https://developers.google.com/identity/protocols/oauth2/web-server?hl=pl#exchange-authorization-code>

```js
let googleCode = ""

const url = 'https://oauth2.googleapis.com/token';

const data = new URLSearchParams({
  // Oauth details
  client_id: import.meta.env.VITE_GOOGLE_OAUTH_CLIENT_ID,
  client_secret: import.meta.env.VITE_GOOGLE_OAUTH_CLIENT_SECRET,
  code: googleCode

  // Get access_token
  grant_type = "authorization_code",
  redirect_uri = "http://127.0.0.1:8000/oauth/google",

  // Refresh token
  // refresh_token: refreshToken,
  // grant_type: 'refresh_token',
});

try {
    let res = await axios.post(url, data, {
        headers: {
            'content-type': 'application/x-www-form-urlencoded',
            'Accept-Charset': 'UTF-8'
        },
    }).then(response => {
        debugger;
    }).catch(e => {
        // It always enters the 'catch' here
        debugger;
    });
} catch (e) {
    debugger;
}
```

## Tworzenie url dla przycisku z JWT token (id_token)

<https://developers.google.com/identity/protocols/oauth2/web-server?hl=pl#httprest_1>

```js
// utils/getGoogleUrl.js

export const getGoogleUrl = (from) => {
 const rootUrl = `https://accounts.google.com/o/oauth2/v2/auth`

 const options = {
  redirect_uri: import.meta.env.VITE_GOOGLE_OAUTH_REDIRECT,
  client_id: import.meta.env.VITE_GOOGLE_OAUTH_CLIENT_ID,
  scope: ['https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/userinfo.email'].join(' '),
  prompt: 'consent',
  state: from,

  // Get with jwt id_token
  // JWT userinfo uri: https://oauth2.googleapis.com/tokeninfo?id_token=
  response_type: 'id_token',
  access_type: 'online',
  nonce: 'random_string',
 }

 const params = new URLSearchParams(options)
 return `${rootUrl}?${params.toString()}`
}
```

## Odpowiedz z serwera google

```json
{
  clientId: "22026532.apps.googleusercontent.com",
  client_id: "757722026532-0q0fmk45elkm7sum6mad5tmdutduk54t.apps.googleusercontent.com",
  credential: "fy0.p8QNTep8QhZwp8QNTep8QhZwp8QNTep8QhZw...",
  select_by: "user"
}
```

## Pobierz google userinfo z JWT token (id_token)

<https://oauth2.googleapis.com/tokeninfo?id_token=>

```json
{
  "iss": "https://accounts.google.com",
  "nbf": "500280",
  "aud": "22026532.apps.googleusercontent.com",
  "sub": "388663",
  "email": "logged-user-email@gmail.com",
  "email_verified": "true",
  "azp": "22026532.apps.googleusercontent.com",
  "name": "User Name",
  "picture": "https://lh3.googleusercontent.com/a/AGNmyxYkSTMH6VDZc8qIPfjgVh4ZHyoFUnXdy4vGKpiqzQ=s96-c",
  "given_name": "User Name",
  "iat": "500580",
  "exp": "504180",
  "jti": "15a70728ebc01fb43a691eb2033da42",
  "alg": "RS256",
  "kid": "c9afda363055c1c4bd39b751fbf8195",
  "typ": "JWT"
}
```

## Pakiet do automatycznego logowania dla vue (przykład bez backendu)
<https://www.npmjs.com/package/vue3-google-login>

- Trzeba przekierować jwt token na serwer
- Pobrać odpowiedź z <https://oauth2.googleapis.com/tokeninfo?id_token=> zawirającą dane zalogowanego usera
- Zalogować usera na backendzie i przekierować na stronę główną
