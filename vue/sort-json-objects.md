# Sortowanie json array z obiektami 
Sortowanie w javascript json z obiektami (country phone codes)

### Sortowanie tablicy obiektów
```js
import prefix from '@/assets/json/country.json'

function compare(a, b) {
	if (parseInt(a.prefix) < parseInt(b.prefix)) {
		return -1
	}
	if (parseInt(a.prefix) > parseInt(b.prefix)) {
		return 1
	}
	return 0
}

// Sortowanie obiektów
const codes = prefix.sort(compare)
```

### Html select

```vue
<select name="prefix">
	<option v-for="v of codes" value="v.prefix">{{ v.prefix }}</option>
</select>
```

### Sortowanie tablicy z integer
```js
import prefix from '@/assets/json/country.json'

// Unikalna tablica prefixów
const unique_prefix = [...new Set(prefix.map((item) => item.prefix))]

// Sortowanie prefixów
const codes = unique_prefix.sort((a, b) => parseInt(a) - parseInt(b))
```

### Html select

```vue
<select name="prefix">
	<option v-for="v of codes" value="v">{{ v }}</option>
</select>
```

### Plik country.json
```sh
[
	{
		"name": "Afghanistan",
		"prefix": "93",
		"emoji": "🇦🇫",
		"code": "AF"
	},
	{
		"name": "Aland Islands",
		"prefix": "358",
		"emoji": "🇦🇽",
		"code": "AX"
	},
	{
		"name": "Albania",
		"prefix": "355",
		"emoji": "🇦🇱",
		"code": "AL"
	},
	{
		"name": "Algeria",
		"prefix": "213",
		"emoji": "🇩🇿",
		"code": "DZ"
	},
	{
		"name": "AmericanSamoa",
		"prefix": "1684",
		"emoji": "🇦🇸",
		"code": "AS"
	},
	{
		"name": "Andorra",
		"prefix": "376",
		"emoji": "🇦🇩",
		"code": "AD"
	},
	{
		"name": "Angola",
		"prefix": "244",
		"emoji": "🇦🇴",
		"code": "AO"
	},
	{
		"name": "Anguilla",
		"prefix": "1264",
		"emoji": "🇦🇮",
		"code": "AI"
	},
	{
		"name": "Antarctica",
		"prefix": "672",
		"emoji": "🇦🇶",
		"code": "AQ"
	},
	{
		"name": "Antigua and Barbuda",
		"prefix": "1268",
		"emoji": "🇦🇬",
		"code": "AG"
	},
	{
		"name": "Argentina",
		"prefix": "54",
		"emoji": "🇦🇷",
		"code": "AR"
	},
	{
		"name": "Armenia",
		"prefix": "374",
		"emoji": "🇦🇲",
		"code": "AM"
	},
	{
		"name": "Aruba",
		"prefix": "297",
		"emoji": "🇦🇼",
		"code": "AW"
	},
	{
		"name": "Australia",
		"prefix": "61",
		"emoji": "🇦🇺",
		"code": "AU"
	},
	{
		"name": "Austria",
		"prefix": "43",
		"emoji": "🇦🇹",
		"code": "AT"
	},
	{
		"name": "Azerbaijan",
		"prefix": "994",
		"emoji": "🇦🇿",
		"code": "AZ"
	},
	{
		"name": "Bahamas",
		"prefix": "1242",
		"emoji": "🇧🇸",
		"code": "BS"
	},
	{
		"name": "Bahrain",
		"prefix": "973",
		"emoji": "🇧🇭",
		"code": "BH"
	},
	{
		"name": "Bangladesh",
		"prefix": "880",
		"emoji": "🇧🇩",
		"code": "BD"
	},
	{
		"name": "Barbados",
		"prefix": "1246",
		"emoji": "🇧🇧",
		"code": "BB"
	},
	{
		"name": "Belarus",
		"prefix": "375",
		"emoji": "🇧🇾",
		"code": "BY"
	},
	{
		"name": "Belgium",
		"prefix": "32",
		"emoji": "🇧🇪",
		"code": "BE"
	},
	{
		"name": "Belize",
		"prefix": "501",
		"emoji": "🇧🇿",
		"code": "BZ"
	},
	{
		"name": "Benin",
		"prefix": "229",
		"emoji": "🇧🇯",
		"code": "BJ"
	},
	{
		"name": "Bermuda",
		"prefix": "1441",
		"emoji": "🇧🇲",
		"code": "BM"
	},
	{
		"name": "Bhutan",
		"prefix": "975",
		"emoji": "🇧🇹",
		"code": "BT"
	},
	{
		"name": "Bolivia, Plurinational State of",
		"prefix": "591",
		"emoji": "🇧🇴",
		"code": "BO"
	},
	{
		"name": "Bosnia and Herzegovina",
		"prefix": "387",
		"emoji": "🇧🇦",
		"code": "BA"
	},
	{
		"name": "Botswana",
		"prefix": "267",
		"emoji": "🇧🇼",
		"code": "BW"
	},
	{
		"name": "Brazil",
		"prefix": "55",
		"emoji": "🇧🇷",
		"code": "BR"
	},
	{
		"name": "British Indian Ocean Territory",
		"prefix": "246",
		"emoji": "🇮🇴",
		"code": "IO"
	},
	{
		"name": "Brunei Darussalam",
		"prefix": "673",
		"emoji": "🇧🇳",
		"code": "BN"
	},
	{
		"name": "Bulgaria",
		"prefix": "359",
		"emoji": "🇧🇬",
		"code": "BG"
	},
	{
		"name": "Burkina Faso",
		"prefix": "226",
		"emoji": "🇧🇫",
		"code": "BF"
	},
	{
		"name": "Burundi",
		"prefix": "257",
		"emoji": "🇧🇮",
		"code": "BI"
	},
	{
		"name": "Cambodia",
		"prefix": "855",
		"emoji": "🇰🇭",
		"code": "KH"
	},
	{
		"name": "Cameroon",
		"prefix": "237",
		"emoji": "🇨🇲",
		"code": "CM"
	},
	{
		"name": "Canada",
		"prefix": "1",
		"emoji": "🇨🇦",
		"code": "CA"
	},
	{
		"name": "Cape Verde",
		"prefix": "238",
		"emoji": "🇨🇻",
		"code": "CV"
	},
	{
		"name": "Cayman Islands",
		"prefix": "345",
		"emoji": "🇰🇾",
		"code": "KY"
	},
	{
		"name": "Central African Republic",
		"prefix": "236",
		"emoji": "🇨🇫",
		"code": "CF"
	},
	{
		"name": "Chad",
		"prefix": "235",
		"emoji": "🇹🇩",
		"code": "TD"
	},
	{
		"name": "Chile",
		"prefix": "56",
		"emoji": "🇨🇱",
		"code": "CL"
	},
	{
		"name": "China",
		"prefix": "86",
		"emoji": "🇨🇳",
		"code": "CN"
	},
	{
		"name": "Christmas Island",
		"prefix": "61",
		"emoji": "🇨🇽",
		"code": "CX"
	},
	{
		"name": "Cocos (Keeling) Islands",
		"prefix": "61",
		"emoji": "🇨🇨",
		"code": "CC"
	},
	{
		"name": "Colombia",
		"prefix": "57",
		"emoji": "🇨🇴",
		"code": "CO"
	},
	{
		"name": "Comoros",
		"prefix": "269",
		"emoji": "🇰🇲",
		"code": "KM"
	},
	{
		"name": "Congo",
		"prefix": "242",
		"emoji": "🇨🇬",
		"code": "CG"
	},
	{
		"name": "Congo, The Democratic Republic of the Congo",
		"prefix": "243",
		"emoji": "🇨🇩",
		"code": "CD"
	},
	{
		"name": "Cook Islands",
		"prefix": "682",
		"emoji": "🇨🇰",
		"code": "CK"
	},
	{
		"name": "Costa Rica",
		"prefix": "506",
		"emoji": "🇨🇷",
		"code": "CR"
	},
	{
		"name": "Cote d'Ivoire",
		"prefix": "225",
		"emoji": "🇨🇮",
		"code": "CI"
	},
	{
		"name": "Croatia",
		"prefix": "385",
		"emoji": "🇭🇷",
		"code": "HR"
	},
	{
		"name": "Cuba",
		"prefix": "53",
		"emoji": "🇨🇺",
		"code": "CU"
	},
	{
		"name": "Cyprus",
		"prefix": "357",
		"emoji": "🇨🇾",
		"code": "CY"
	},
	{
		"name": "Czech Republic",
		"prefix": "420",
		"emoji": "🇨🇿",
		"code": "CZ"
	},
	{
		"name": "Denmark",
		"prefix": "45",
		"emoji": "🇩🇰",
		"code": "DK"
	},
	{
		"name": "Djibouti",
		"prefix": "253",
		"emoji": "🇩🇯",
		"code": "DJ"
	},
	{
		"name": "Dominica",
		"prefix": "1767",
		"emoji": "🇩🇲",
		"code": "DM"
	},
	{
		"name": "Dominican Republic",
		"prefix": "1849",
		"emoji": "🇩🇴",
		"code": "DO"
	},
	{
		"name": "Ecuador",
		"prefix": "593",
		"emoji": "🇪🇨",
		"code": "EC"
	},
	{
		"name": "Egypt",
		"prefix": "20",
		"emoji": "🇪🇬",
		"code": "EG"
	},
	{
		"name": "El Salvador",
		"prefix": "503",
		"emoji": "🇸🇻",
		"code": "SV"
	},
	{
		"name": "Equatorial Guinea",
		"prefix": "240",
		"emoji": "🇬🇶",
		"code": "GQ"
	},
	{
		"name": "Eritrea",
		"prefix": "291",
		"emoji": "🇪🇷",
		"code": "ER"
	},
	{
		"name": "Estonia",
		"prefix": "372",
		"emoji": "🇪🇪",
		"code": "EE"
	},
	{
		"name": "Ethiopia",
		"prefix": "251",
		"emoji": "🇪🇹",
		"code": "ET"
	},
	{
		"name": "Falkland Islands (Malvinas)",
		"prefix": "500",
		"emoji": "🇫🇰",
		"code": "FK"
	},
	{
		"name": "Faroe Islands",
		"prefix": "298",
		"emoji": "🇫🇴",
		"code": "FO"
	},
	{
		"name": "Fiji",
		"prefix": "679",
		"emoji": "🇫🇯",
		"code": "FJ"
	},
	{
		"name": "Finland",
		"prefix": "358",
		"emoji": "🇫🇮",
		"code": "FI"
	},
	{
		"name": "France",
		"prefix": "33",
		"emoji": "🇫🇷",
		"code": "FR"
	},
	{
		"name": "French Guiana",
		"prefix": "594",
		"emoji": "🇬🇫",
		"code": "GF"
	},
	{
		"name": "French Polynesia",
		"prefix": "689",
		"emoji": "🇵🇫",
		"code": "PF"
	},
	{
		"name": "Gabon",
		"prefix": "241",
		"emoji": "🇬🇦",
		"code": "GA"
	},
	{
		"name": "Gambia",
		"prefix": "220",
		"emoji": "🇬🇲",
		"code": "GM"
	},
	{
		"name": "Georgia",
		"prefix": "995",
		"emoji": "🇬🇪",
		"code": "GE"
	},
	{
		"name": "Germany",
		"prefix": "49",
		"emoji": "🇩🇪",
		"code": "DE"
	},
	{
		"name": "Ghana",
		"prefix": "233",
		"emoji": "🇬🇭",
		"code": "GH"
	},
	{
		"name": "Gibraltar",
		"prefix": "350",
		"emoji": "🇬🇮",
		"code": "GI"
	},
	{
		"name": "Greece",
		"prefix": "30",
		"emoji": "🇬🇷",
		"code": "GR"
	},
	{
		"name": "Greenland",
		"prefix": "299",
		"emoji": "🇬🇱",
		"code": "GL"
	},
	{
		"name": "Grenada",
		"prefix": "1473",
		"emoji": "🇬🇩",
		"code": "GD"
	},
	{
		"name": "Guadeloupe",
		"prefix": "590",
		"emoji": "🇬🇵",
		"code": "GP"
	},
	{
		"name": "Guam",
		"prefix": "1671",
		"emoji": "🇬🇺",
		"code": "GU"
	},
	{
		"name": "Guatemala",
		"prefix": "502",
		"emoji": "🇬🇹",
		"code": "GT"
	},
	{
		"name": "Guernsey",
		"prefix": "44",
		"emoji": "🇬🇬",
		"code": "GG"
	},
	{
		"name": "Guinea",
		"prefix": "224",
		"emoji": "🇬🇳",
		"code": "GN"
	},
	{
		"name": "Guinea-Bissau",
		"prefix": "245",
		"emoji": "🇬🇼",
		"code": "GW"
	},
	{
		"name": "Guyana",
		"prefix": "595",
		"emoji": "🇬🇾",
		"code": "GY"
	},
	{
		"name": "Haiti",
		"prefix": "509",
		"emoji": "🇭🇹",
		"code": "HT"
	},
	{
		"name": "Holy See (Vatican City State)",
		"prefix": "379",
		"emoji": "🇻🇦",
		"code": "VA"
	},
	{
		"name": "Honduras",
		"prefix": "504",
		"emoji": "🇭🇳",
		"code": "HN"
	},
	{
		"name": "Hong Kong",
		"prefix": "852",
		"emoji": "🇭🇰",
		"code": "HK"
	},
	{
		"name": "Hungary",
		"prefix": "36",
		"emoji": "🇭🇺",
		"code": "HU"
	},
	{
		"name": "Iceland",
		"prefix": "354",
		"emoji": "🇮🇸",
		"code": "IS"
	},
	{
		"name": "India",
		"prefix": "91",
		"emoji": "🇮🇳",
		"code": "IN"
	},
	{
		"name": "Indonesia",
		"prefix": "62",
		"emoji": "🇮🇩",
		"code": "ID"
	},
	{
		"name": "Iran, Islamic Republic of Persian Gulf",
		"prefix": "98",
		"emoji": "🇮🇷",
		"code": "IR"
	},
	{
		"name": "Iraq",
		"prefix": "964",
		"emoji": "🇮🇷",
		"code": "IQ"
	},
	{
		"name": "Ireland",
		"prefix": "353",
		"emoji": "🇮🇪",
		"code": "IE"
	},
	{
		"name": "Isle of Man",
		"prefix": "44",
		"emoji": "🇮🇲",
		"code": "IM"
	},
	{
		"name": "Israel",
		"prefix": "972",
		"emoji": "🇮🇱",
		"code": "IL"
	},
	{
		"name": "Italy",
		"prefix": "39",
		"emoji": "🇮🇹",
		"code": "IT"
	},
	{
		"name": "Jamaica",
		"prefix": "1876",
		"emoji": "🇯🇲",
		"code": "JM"
	},
	{
		"name": "Japan",
		"prefix": "81",
		"emoji": "🇯🇵",
		"code": "JP"
	},
	{
		"name": "Jersey",
		"prefix": "44",
		"emoji": "🇯🇪",
		"code": "JE"
	},
	{
		"name": "Jordan",
		"prefix": "962",
		"emoji": "🇯🇴",
		"code": "JO"
	},
	{
		"name": "Kazakhstan",
		"prefix": "77",
		"emoji": "🇰🇿",
		"code": "KZ"
	},
	{
		"name": "Kenya",
		"prefix": "254",
		"emoji": "🇰🇪",
		"code": "KE"
	},
	{
		"name": "Kiribati",
		"prefix": "686",
		"emoji": "🇰🇮",
		"code": "KI"
	},
	{
		"name": "Korea, Democratic People's Republic of Korea",
		"prefix": "850",
		"emoji": "🇰🇵",
		"code": "KP"
	},
	{
		"name": "Korea, Republic of South Korea",
		"prefix": "82",
		"emoji": "🇰🇷",
		"code": "KR"
	},
	{
		"name": "Kuwait",
		"prefix": "965",
		"emoji": "🇰🇼",
		"code": "KW"
	},
	{
		"name": "Kyrgyzstan",
		"prefix": "996",
		"emoji": "🇰🇬",
		"code": "KG"
	},
	{
		"name": "Laos",
		"prefix": "856",
		"emoji": "🇱🇦",
		"code": "LA"
	},
	{
		"name": "Latvia",
		"prefix": "371",
		"emoji": "🇱🇻",
		"code": "LV"
	},
	{
		"name": "Lebanon",
		"prefix": "961",
		"emoji": "🇱🇧",
		"code": "LB"
	},
	{
		"name": "Lesotho",
		"prefix": "266",
		"emoji": "🇱🇸",
		"code": "LS"
	},
	{
		"name": "Liberia",
		"prefix": "231",
		"emoji": "🇱🇷",
		"code": "LR"
	},
	{
		"name": "Libyan Arab Jamahiriya",
		"prefix": "218",
		"emoji": "🇱🇾",
		"code": "LY"
	},
	{
		"name": "Liechtenstein",
		"prefix": "423",
		"emoji": "🇱🇮",
		"code": "LI"
	},
	{
		"name": "Lithuania",
		"prefix": "370",
		"emoji": "🇱🇹",
		"code": "LT"
	},
	{
		"name": "Luxembourg",
		"prefix": "352",
		"emoji": "🇱🇺",
		"code": "LU"
	},
	{
		"name": "Macao",
		"prefix": "853",
		"emoji": "🇲🇴",
		"code": "MO"
	},
	{
		"name": "Macedonia",
		"prefix": "389",
		"emoji": "🇲🇰",
		"code": "MK"
	},
	{
		"name": "Madagascar",
		"prefix": "261",
		"emoji": "🇲🇬",
		"code": "MG"
	},
	{
		"name": "Malawi",
		"prefix": "265",
		"emoji": "🇲🇼",
		"code": "MW"
	},
	{
		"name": "Malaysia",
		"prefix": "60",
		"emoji": "🇲🇾",
		"code": "MY"
	},
	{
		"name": "Maldives",
		"prefix": "960",
		"emoji": "🇲🇻",
		"code": "MV"
	},
	{
		"name": "Mali",
		"prefix": "223",
		"emoji": "🇲🇱",
		"code": "ML"
	},
	{
		"name": "Malta",
		"prefix": "356",
		"emoji": "🇲🇹",
		"code": "MT"
	},
	{
		"name": "Marshall Islands",
		"prefix": "692",
		"emoji": "🇲🇭",
		"code": "MH"
	},
	{
		"name": "Martinique",
		"prefix": "596",
		"emoji": "🇲🇶",
		"code": "MQ"
	},
	{
		"name": "Mauritania",
		"prefix": "222",
		"emoji": "🇲🇷",
		"code": "MR"
	},
	{
		"name": "Mauritius",
		"prefix": "230",
		"emoji": "🇲🇺",
		"code": "MU"
	},
	{
		"name": "Mayotte",
		"prefix": "262",
		"emoji": "🇾🇹",
		"code": "YT"
	},
	{
		"name": "Mexico",
		"prefix": "52",
		"emoji": "🇲🇽",
		"code": "MX"
	},
	{
		"name": "Micronesia, Federated States of Micronesia",
		"prefix": "691",
		"emoji": "🇫🇲",
		"code": "FM"
	},
	{
		"name": "Moldova",
		"prefix": "373",
		"emoji": "🇲🇩",
		"code": "MD"
	},
	{
		"name": "Monaco",
		"prefix": "377",
		"emoji": "🇲🇨",
		"code": "MC"
	},
	{
		"name": "Mongolia",
		"prefix": "976",
		"emoji": "🇲🇳",
		"code": "MN"
	},
	{
		"name": "Montenegro",
		"prefix": "382",
		"emoji": "🇲🇪",
		"code": "ME"
	},
	{
		"name": "Montserrat",
		"prefix": "1664",
		"emoji": "🇲🇸",
		"code": "MS"
	},
	{
		"name": "Morocco",
		"prefix": "212",
		"emoji": "🇲🇦",
		"code": "MA"
	},
	{
		"name": "Mozambique",
		"prefix": "258",
		"emoji": "🇲🇿",
		"code": "MZ"
	},
	{
		"name": "Myanmar",
		"prefix": "95",
		"emoji": "🇲🇲",
		"code": "MM"
	},
	{
		"name": "Namibia",
		"emoji": "🇳🇦",
		"prefix": "264",
		"code": "NA"
	},
	{
		"name": "Nauru",
		"prefix": "674",
		"emoji": "🇳🇷",
		"code": "NR"
	},
	{
		"name": "Nepal",
		"prefix": "977",
		"emoji": "🇳🇵",
		"code": "NP"
	},
	{
		"name": "Netherlands",
		"prefix": "31",
		"emoji": "🇳🇱",
		"code": "NL"
	},
	{
		"name": "Netherlands Antilles",
		"prefix": "599",
		"emoji": "🇧🇶",
		"code": "AN"
	},
	{
		"name": "New Caledonia",
		"prefix": "687",
		"emoji": "🇳🇨",
		"code": "NC"
	},
	{
		"name": "New Zealand",
		"prefix": "64",
		"emoji": "🇳🇿",
		"code": "NZ"
	},
	{
		"name": "Nicaragua",
		"prefix": "505",
		"emoji": "🇳🇮",
		"code": "NI"
	},
	{
		"name": "Niger",
		"prefix": "227",
		"emoji": "🇳🇪",
		"code": "NE"
	},
	{
		"name": "Nigeria",
		"prefix": "234",
		"emoji": "🇳🇬",
		"code": "NG"
	},
	{
		"name": "Niue",
		"prefix": "683",
		"emoji": "🇳🇺",
		"code": "NU"
	},
	{
		"name": "Norfolk Island",
		"prefix": "672",
		"emoji": "🇳🇫",
		"code": "NF"
	},
	{
		"name": "Northern Mariana Islands",
		"prefix": "1670",
		"emoji": "🇲🇵",
		"code": "MP"
	},
	{
		"name": "Norway",
		"prefix": "47",
		"emoji": "🇳🇴",
		"code": "NO"
	},
	{
		"name": "Oman",
		"prefix": "968",
		"emoji": "🇴🇲",
		"code": "OM"
	},
	{
		"name": "Pakistan",
		"prefix": "92",
		"emoji": "🇵🇰",
		"code": "PK"
	},
	{
		"name": "Palau",
		"prefix": "680",
		"emoji": "🇵🇼",
		"code": "PW"
	},
	{
		"name": "Palestinian Territory, Occupied",
		"prefix": "970",
		"emoji": "🇵🇸",
		"code": "PS"
	},
	{
		"name": "Panama",
		"prefix": "507",
		"emoji": "🇵🇦",
		"code": "PA"
	},
	{
		"name": "Papua New Guinea",
		"prefix": "675",
		"emoji": "🇵🇬",
		"code": "PG"
	},
	{
		"name": "Paraguay",
		"prefix": "595",
		"emoji": "🇵🇾",
		"code": "PY"
	},
	{
		"name": "Peru",
		"prefix": "51",
		"emoji": "🇵🇪",
		"code": "PE"
	},
	{
		"name": "Philippines",
		"prefix": "63",
		"emoji": "🇵🇭",
		"code": "PH"
	},
	{
		"name": "Pitcairn",
		"prefix": "872",
		"emoji": "🇵🇳",
		"code": "PN"
	},
	{
		"name": "Poland",
		"prefix": "48",
		"emoji": "🇵🇱",
		"code": "PL"
	},
	{
		"name": "Portugal",
		"prefix": "351",
		"emoji": "🇵🇹",
		"code": "PT"
	},
	{
		"name": "Puerto Rico",
		"prefix": "1939",
		"emoji": "🇵🇷",
		"code": "PR"
	},
	{
		"name": "Qatar",
		"prefix": "974",
		"emoji": "🇶🇦",
		"code": "QA"
	},
	{
		"name": "Romania",
		"prefix": "40",
		"emoji": "🇷🇴",
		"code": "RO"
	},
	{
		"name": "Russia",
		"prefix": "7",
		"emoji": "🇷🇺",
		"code": "RU"
	},
	{
		"name": "Rwanda",
		"prefix": "250",
		"emoji": "🇷🇼",
		"code": "RW"
	},
	{
		"name": "Reunion",
		"prefix": "262",
		"emoji": "🇷🇪",
		"code": "RE"
	},
	{
		"name": "Saint Barthelemy",
		"prefix": "590",
		"emoji": "🇧🇱",
		"code": "BL"
	},
	{
		"name": "Saint Helena, Ascension and Tristan Da Cunha",
		"prefix": "290",
		"emoji": "🇸🇭",
		"code": "SH"
	},
	{
		"name": "Saint Kitts and Nevis",
		"prefix": "1869",
		"emoji": "🇰🇳",
		"code": "KN"
	},
	{
		"name": "Saint Lucia",
		"prefix": "1758",
		"emoji": "🇱🇨",
		"code": "LC"
	},
	{
		"name": "Saint Martin",
		"prefix": "590",
		"emoji": "🇲🇫",
		"code": "MF"
	},
	{
		"name": "Saint Pierre and Miquelon",
		"prefix": "508",
		"emoji": "🇵🇲",
		"code": "PM"
	},
	{
		"name": "Saint Vincent and the Grenadines",
		"prefix": "1784",
		"emoji": "🇻🇨",
		"code": "VC"
	},
	{
		"name": "Samoa",
		"prefix": "685",
		"emoji": "🇼🇸",
		"code": "WS"
	},
	{
		"name": "San Marino",
		"prefix": "378",
		"emoji": "🇸🇲",
		"code": "SM"
	},
	{
		"name": "Sao Tome and Principe",
		"prefix": "239",
		"emoji": "🇸🇹",
		"code": "ST"
	},
	{
		"name": "Saudi Arabia",
		"prefix": "966",
		"emoji": "🇸🇦",
		"code": "SA"
	},
	{
		"name": "Senegal",
		"prefix": "221",
		"emoji": "🇸🇳",
		"code": "SN"
	},
	{
		"name": "Serbia",
		"prefix": "381",
		"emoji": "🇷🇸",
		"code": "RS"
	},
	{
		"name": "Seychelles",
		"prefix": "248",
		"emoji": "🇸🇨",
		"code": "SC"
	},
	{
		"name": "Sierra Leone",
		"prefix": "232",
		"emoji": "🇸🇱",
		"code": "SL"
	},
	{
		"name": "Singapore",
		"prefix": "65",
		"emoji": "🇸🇬",
		"code": "SG"
	},
	{
		"name": "Slovakia",
		"prefix": "421",
		"emoji": "🇸🇰",
		"code": "SK"
	},
	{
		"name": "Slovenia",
		"prefix": "386",
		"emoji": "🇸🇮",
		"code": "SI"
	},
	{
		"name": "Solomon Islands",
		"prefix": "677",
		"emoji": "🇸🇧",
		"code": "SB"
	},
	{
		"name": "Somalia",
		"prefix": "252",
		"emoji": "🇸🇴",
		"code": "SO"
	},
	{
		"name": "South Africa",
		"prefix": "27",
		"emoji": "🇿🇦",
		"code": "ZA"
	},
	{
		"name": "South Sudan",
		"prefix": "211",
		"emoji": "🇸🇸",
		"code": "SS"
	},
	{
		"name": "South Georgia and the South Sandwich Islands",
		"prefix": "500",
		"emoji": "🇬🇸",
		"code": "GS"
	},
	{
		"name": "Spain",
		"prefix": "34",
		"emoji": "🇪🇸",
		"code": "ES"
	},
	{
		"name": "Sri Lanka",
		"prefix": "94",
		"emoji": "🇱🇰",
		"code": "LK"
	},
	{
		"name": "Sudan",
		"prefix": "249",
		"emoji": "🇸🇩",
		"code": "SD"
	},
	{
		"name": "Suriname",
		"prefix": "597",
		"emoji": "🇸🇷",
		"code": "SR"
	},
	{
		"name": "Svalbard and Jan Mayen",
		"prefix": "47",
		"emoji": "🇸🇯",
		"code": "SJ"
	},
	{
		"name": "Swaziland",
		"prefix": "268",
		"emoji": "🇸🇿",
		"code": "SZ"
	},
	{
		"name": "Sweden",
		"prefix": "46",
		"emoji": "🇸🇪",
		"code": "SE"
	},
	{
		"name": "Switzerland",
		"prefix": "41",
		"emoji": "🇨🇭",
		"code": "CH"
	},
	{
		"name": "Syrian Arab Republic",
		"prefix": "963",
		"emoji": "🇸🇾",
		"code": "SY"
	},
	{
		"name": "Taiwan",
		"prefix": "886",
		"emoji": "🇹🇼",
		"code": "TW"
	},
	{
		"name": "Tajikistan",
		"prefix": "992",
		"emoji": "🇹🇯",
		"code": "TJ"
	},
	{
		"name": "Tanzania, United Republic of Tanzania",
		"prefix": "255",
		"emoji": "🇹🇿",
		"code": "TZ"
	},
	{
		"name": "Thailand",
		"prefix": "66",
		"emoji": "🇹🇭",
		"code": "TH"
	},
	{
		"name": "Timor-Leste",
		"prefix": "670",
		"emoji": "🇹🇱",
		"code": "TL"
	},
	{
		"name": "Togo",
		"prefix": "228",
		"emoji": "🇹🇬",
		"code": "TG"
	},
	{
		"name": "Tokelau",
		"prefix": "690",
		"emoji": "🇹🇰",
		"code": "TK"
	},
	{
		"name": "Tonga",
		"prefix": "676",
		"emoji": "🇹🇴",
		"code": "TO"
	},
	{
		"name": "Trinidad and Tobago",
		"prefix": "1868",
		"emoji": "🇹🇹",
		"code": "TT"
	},
	{
		"name": "Tunisia",
		"prefix": "216",
		"emoji": "🇹🇳",
		"code": "TN"
	},
	{
		"name": "Turkey",
		"prefix": "90",
		"emoji": "🇹🇷",
		"code": "TR"
	},
	{
		"name": "Turkmenistan",
		"prefix": "993",
		"emoji": "🇹🇲",
		"code": "TM"
	},
	{
		"name": "Turks and Caicos Islands",
		"prefix": "1649",
		"emoji": "🇹🇨",
		"code": "TC"
	},
	{
		"name": "Tuvalu",
		"prefix": "688",
		"emoji": "🇹🇻",
		"code": "TV"
	},
	{
		"name": "Uganda",
		"prefix": "256",
		"emoji": "🇺🇬",
		"code": "UG"
	},
	{
		"name": "Ukraine",
		"prefix": "380",
		"emoji": "🇺🇦",
		"code": "UA"
	},
	{
		"name": "United Arab Emirates",
		"prefix": "971",
		"emoji": "🇦🇪",
		"code": "AE"
	},
	{
		"name": "United Kingdom",
		"prefix": "44",
		"emoji": "🇬🇧",
		"code": "GB"
	},
	{
		"name": "United States",
		"prefix": "1",
		"emoji": "🇺🇸",
		"code": "US"
	},
	{
		"name": "Uruguay",
		"prefix": "598",
		"emoji": "🇺🇾",
		"code": "UY"
	},
	{
		"name": "Uzbekistan",
		"prefix": "998",
		"emoji": "🇺🇿",
		"code": "UZ"
	},
	{
		"name": "Vanuatu",
		"prefix": "678",
		"emoji": "🇻🇺",
		"code": "VU"
	},
	{
		"name": "Venezuela, Bolivarian Republic of Venezuela",
		"prefix": "58",
		"emoji": "🇻🇪",
		"code": "VE"
	},
	{
		"name": "Vietnam",
		"prefix": "84",
		"emoji": "🇻🇳",
		"code": "VN"
	},
	{
		"name": "Virgin Islands, British",
		"prefix": "1284",
		"emoji": "🇻🇬",
		"code": "VG"
	},
	{
		"name": "Virgin Islands, U.S.",
		"prefix": "1340",
		"emoji": "🇻🇮",
		"code": "VI"
	},
	{
		"name": "Wallis and Futuna",
		"prefix": "681",
		"emoji": "🇼🇫",
		"code": "WF"
	},
	{
		"name": "Yemen",
		"prefix": "967",
		"emoji": "🇾🇪",
		"code": "YE"
	},
	{
		"name": "Zambia",
		"prefix": "260",
		"emoji": "🇿🇲",
		"code": "ZM"
	},
	{
		"name": "Zimbabwe",
		"prefix": "263",
		"emoji": "🇿🇼",
		"code": "ZW"
	}
]
```
