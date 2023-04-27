// Google custom login button url vue
export const getGoogleUrl = (from) => {
	const rootUrl = `https://accounts.google.com/o/oauth2/v2/auth`

	const options = {
		redirect_uri: import.meta.env.VITE_GOOGLE_OAUTH_REDIRECT,
		client_id: import.meta.env.VITE_GOOGLE_OAUTH_CLIENT_ID,
		prompt: 'consent',
		scope: ['https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/userinfo.email'].join(' '),
		state: from,
		// Show the account selector and aprowal ui
		// prompt: 'select_account consent'

		// Get with access_token
		// Send with bearer header with access_token to:
    // `https://www.googleapis.com/oauth2/v2/userinfo`
    // Or 
    // `https://www.googleapis.com/oauth2/v2/userinfo?alt=json&access_token=${access_token}`
		response_type: 'token',
		access_type: 'online',

		// Get with jwt id_token
		// Userinfo uri: https://oauth2.googleapis.com/tokeninfo?id_token=
		// response_type: 'id_token',
		// access_type: 'online',
		// nonce: 'random_string',

		// Get with code
		// Code request method POST to: `https://oauth2.googleapis.com/token`
		// response_type: 'code',
		// access_type: 'offline',
	}

	const qs = new URLSearchParams(options)

	return `${rootUrl}?${qs.toString()}`
}

/*
// Docs
// https://developers.google.com/identity/protocols/oauth2/javascript-implicit-flow?hl=pl

// Get access_token from code method POST (node.js server side)

const url = 'https://oauth2.googleapis.com/token';
const data = new URLSearchParams({
    // Refresh token
    // refresh_token: refreshToken,
    // grant_type: 'refresh_token',

    // Get access_token
    grant_type = "authorization_code",
    code = googleCode
    redirect_uri = "http://127.0.0.1:8000/oauth/google",

    // Oauth details
    client_id: import.meta.env.VITE_GOOGLE_OAUTH_CLIENT_ID,
    client_secret: import.meta.env.VITE_GOOGLE_OAUTH_CLIENT_SECRET,
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

// Allowed params oauth

const oauth = {
  "issuer": "https://accounts.google.com",
  "authorization_endpoint": "https://accounts.google.com/o/oauth2/v2/auth",
  "device_authorization_endpoint": "https://oauth2.googleapis.com/device/code",
  "token_endpoint": "https://oauth2.googleapis.com/token",
  "userinfo_endpoint": "https://openidconnect.googleapis.com/v2/userinfo",
  "revocation_endpoint": "https://oauth2.googleapis.com/revoke",
  "jwks_uri": "https://www.googleapis.com/oauth2/v3/certs",
  "response_types_supported": [
    "code",
    "token",
    "id_token",
    "code token",
    "code id_token",
    "token id_token",
    "code token id_token",
    "none"
  ],
  "subject_types_supported": [
    "public"
  ],
  "id_token_signing_alg_values_supported": [
    "RS256"
  ],
  "scopes_supported": [
    "openid",
    "email",
    "profile"
  ],
  "token_endpoint_auth_methods_supported": [
    "client_secret_post",
    "client_secret_basic"
  ],
  "claims_supported": [
    "aud",
    "email",
    "email_verified",
    "exp",
    "family_name",
    "given_name",
    "iat",
    "iss",
    "locale",
    "name",
    "picture",
    "sub"
  ],
  "code_challenge_methods_supported": [
    "plain",
    "S256"
  ]
}

*/
