function getCookie(name) {
    if (document.cookie !== "") {
        const cookies = document.cookie.split(/; */);

        for (let cookie of cookies) {
            const [ cookieName, cookieVal ] = cookie.split("=");
            if (cookieName === decodeURIComponent(name)) {
                return decodeURIComponent(cookieVal);
            }
        }
    }

    return undefined;
}

function setCookie(name, value, options) {
    const opts = {
        path: "/",
        ...options
    }

    if (navigator.cookieEnabled) {
        const cookieName = encodeURIComponent(name);
        const cookieVal = encodeURIComponent(value);
        let cookieText = cookieName + "=" + cookieVal;

        if (opts.days && typeof opts.days === "number") {
            const data = new Date();
            data.setTime(data.getTime() + (opts.days * 24*60*60*1000));
            cookieText += "; expires=" + data.toUTCString();
        }

        if (opts.path) {
            cookieText += "; path=" + opts.path;
        }
        if (opts.domain) {
            cookieText += "; domain=" + opts.domain;
        }
        if (opts.secure) {
            cookieText += "; secure";
        }
        if (opts.strict) {
            cookieText += "; samesite=strict";
        }
        if (opts.lax) {
            cookieText += "; samesite=lax";
        }

        document.cookie = cookieText;
    }
}

function deleteCookie(name, options) {
    const opts = {
        path: "/",
        ...options
    }

    const cookieName = encodeURIComponent(name);
    let cookieText = cookieName + "=";
    if (opts.path) {
        cookieText += "; path=" + opts.path;
    }
    cookieText += "; expires=Thu, 01 Jan 1970 00:00:00 GMT";
    document.cookie = cookieText;
}


// And more secure, value of `SameSite=Lax;`
document.cookie = "test1=Hello; SameSite=None; Secure";
document.cookie = "test2=World; SameSite=Strict; Secure";

const cookieValue = document.cookie
  .split("; ")
  .find((row) => row.startsWith("test2="))
  ?.split("=")[1];

