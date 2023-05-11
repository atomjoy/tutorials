<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>Laravel</title>

        <!-- Fonts -->
        <link rel="preconnect" href="https://fonts.bunny.net">
        <link href="https://fonts.bunny.net/css?family=figtree:400,600&display=swap" rel="stylesheet" />

        <!-- Styles -->
        <style>           
        </style>

        <script>
            const encodeHtml = str  => str.replace(/[\u00A0-\u9999<>\&]/g, i => '&#'+i.charCodeAt(0)+';')

            function encodeHtmlEntity(str) {
                var buf = [];
                for (var i=str.length-1;i>=0;i--) {
                    buf.unshift(['&#', str[i].charCodeAt(), ';'].join(''));
                }
                return buf.join('');
            }

            function encodeHTMLEntities(text) {
                let textArea = document.createElement('textarea');
                textArea.innerText = text;
                let encodedOutput=textArea.innerHTML;
                let arr=encodedOutput.split('<br>');
                encodedOutput=arr.join('\n');
                return encodedOutput;
            }

            function decode(str) {
                let txt = new DOMParser().parseFromString(str, "text/html");
                return txt.documentElement.textContent;
            }

            window.onload = () => {
                let php = `@php echo '<span> <?php echo "Hello mądralo łoążźć€€!!!"; ?> </span>' @endphp`

                document.querySelector("#data1").innerHTML = encodeHtml(php);
                document.querySelector("#data2").innerHTML = encodeHtmlEntity(php);
                document.querySelector("#data3").innerHTML = encodeHTMLEntities(php);
                document.querySelector("#data4").innerHTML = php.replace(/</g,"&lt;").replace(/>/g,"&gt;")
            }
        </script>
    </head>
    <body class="antialiased">
        <div class="relative sm:flex sm:justify-center sm:items-center min-h-screen bg-dots-darker bg-center bg-gray-100 dark:bg-dots-lighter dark:bg-gray-900 selection:bg-red-500 selection:text-white">
            @if (Route::has('login'))
                <div class="sm:fixed sm:top-0 sm:right-0 p-6 text-right">
                    @auth
                        <a href="{{ url('/dashboard') }}" class="font-semibold text-gray-600 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white focus:outline focus:outline-2 focus:rounded-sm focus:outline-red-500">Dashboard</a>
                    @else
                        <a href="{{ route('login') }}" class="font-semibold text-gray-600 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white focus:outline focus:outline-2 focus:rounded-sm focus:outline-red-500">Log in</a>

                        @if (Route::has('register'))
                            <a href="{{ route('register') }}" class="ml-4 font-semibold text-gray-600 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white focus:outline focus:outline-2 focus:rounded-sm focus:outline-red-500">Register</a>
                        @endif
                    @endauth
                </div>
            @endif

            <div class="max-w-7xl mx-auto p-6 lg:p-8">
                <h1>Hello World</h1>
                <div id="data1"></div>
                <div id="data2"></div>
                <div id="data3"></div>
                <div id="data4"></div>                
                <div id="data5">
                    @php echo htmlentities('<span> <?php echo "Hello mądralo łoążźć€€!!!"; ?> </span>'); @endphp
                </div>
            </div>
        </div>
    </body>
</html>
