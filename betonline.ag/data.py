data_header = """
                var data = arguments[0];
                var callback = arguments[1];
                var xhr = new XMLHttpRequest();
                xhr.responseType = 'json';
                xhr.onload = function(){ callback( xhr.response  )};
                xhr.onerror = function(){ callback(xhr.status) };
                xhr.open('POST', 'https://dgslivebetting.betonline.ag/ngwbet.aspx/gvFrameHtml');
                xhr.setRequestHeader('Host', 'dgslivebetting.betonline.ag');
                xhr.setRequestHeader('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36');
                xhr.setRequestHeader('Accept', '*/*');
                xhr.setRequestHeader('Accept-Language', 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3');
                xhr.setRequestHeader('Accept-Encoding', 'gzip, deflate, br');
                xhr.setRequestHeader('Referer', 'https://dgslivebetting.betonline.ag/ngwbet.aspx');
                xhr.setRequestHeader('X-NewRelic-ID', 'VgcFUVNTDxACV1NaDgIDVlw=');
                xhr.setRequestHeader('Content-Type', 'application/json; charset=utf-8');
                xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
                xhr.setRequestHeader('Origin', 'https://dgslivebetting.betonline.ag');
                xhr.setRequestHeader('Connection', 'keep-alive');
                xhr.setRequestHeader('Access-Control-Allow-Origin', '*');
                xhr.setRequestHeader('Sec-Fetch-Dest', 'empty');
                xhr.setRequestHeader('Sec-Fetch-Mode', 'no-cors');
                xhr.setRequestHeader('Sec-Fetch-Site', 'same-site');
                xhr.setRequestHeader('TE', 'trailers');
                xhr.setRequestHeader('Pragma', 'no-cache');
                xhr.setRequestHeader('Cache-Control', 'no-cache');
                xhr.send(data);
                """

data_headerGame = """
                var data = arguments[0];
                var callback = arguments[1];
                var xhr = new XMLHttpRequest();
                xhr.responseType = 'json';
                xhr.onload = function(){ callback( xhr.response  )};
                xhr.onerror = function(){ callback(xhr.status) };
                xhr.open('POST', 'https://dgslivebetting.betonline.ag/ngwbet.aspx/gvGameHtml');
                xhr.setRequestHeader('Host', 'dgslivebetting.betonline.ag');
                xhr.setRequestHeader('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36');
                xhr.setRequestHeader('Accept', '*/*');
                xhr.setRequestHeader('Accept-Language', 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3');
                xhr.setRequestHeader('Accept-Encoding', 'gzip, deflate, br');
                xhr.setRequestHeader('Referer', 'https://dgslivebetting.betonline.ag/ngwbet.aspx');
                xhr.setRequestHeader('X-NewRelic-ID', 'VgcFUVNTDxACV1NaDgIDVlw=');
                xhr.setRequestHeader('Content-Type', 'application/json; charset=utf-8');
                xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
                xhr.setRequestHeader('Origin', 'https://dgslivebetting.betonline.ag');
                xhr.setRequestHeader('Connection', 'keep-alive');
                xhr.setRequestHeader('Access-Control-Allow-Origin', '*');
                xhr.setRequestHeader('Sec-Fetch-Dest', 'empty');
                xhr.setRequestHeader('Sec-Fetch-Mode', 'no-cors');
                xhr.setRequestHeader('Sec-Fetch-Site', 'same-site');
                xhr.setRequestHeader('TE', 'trailers');
                xhr.setRequestHeader('Pragma', 'no-cache');
                xhr.setRequestHeader('Cache-Control', 'no-cache');


                xhr.send(data);
                """


data_header_gvGameHtml = """
                var data = arguments[0];
                var callback = arguments[1];
                var xhr = new XMLHttpRequest();
                xhr.responseType = 'json';
                xhr.onload = function(){ callback( xhr.response  )};
                xhr.onerror = function(){ callback(xhr.status) };
                xhr.open('POST', 'https://dgslivebetting.betonline.ag/ngwbet.aspx/gvGameHtml');
                xhr.setRequestHeader('Host', 'dgslivebetting.betonline.ag');
                xhr.setRequestHeader('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36');
                xhr.setRequestHeader('Accept', '*/*');
                xhr.setRequestHeader('Accept-Language', 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3');
                xhr.setRequestHeader('Accept-Encoding', 'gzip, deflate, br');
                xhr.setRequestHeader('Referer', 'https://dgslivebetting.betonline.ag/ngwbet.aspx');
                xhr.setRequestHeader('X-NewRelic-ID', 'VgcFUVNTDxACV1NaDgIDVlw=');
                xhr.setRequestHeader('Content-Type', 'application/json; charset=utf-8');
                xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
                xhr.setRequestHeader('Origin', 'https://dgslivebetting.betonline.ag');
                xhr.setRequestHeader('Connection', 'keep-alive');
                xhr.setRequestHeader('Access-Control-Allow-Origin', '*');
                xhr.setRequestHeader('Sec-Fetch-Dest', 'empty');
                xhr.setRequestHeader('Sec-Fetch-Mode', 'no-cors');
                xhr.setRequestHeader('Sec-Fetch-Site', 'same-site');
                xhr.setRequestHeader('TE', 'trailers');
                xhr.setRequestHeader('Pragma', 'no-cache');
                xhr.setRequestHeader('Cache-Control', 'no-cache');
                xhr.send(data);
                """