
# Данные для запроса
def get_fetch(method, url):
    #
    data_header = """
    
                    var callback = arguments[0];
                    var xhr = new XMLHttpRequest();
                   
                    xhr.onload = function(){ callback( xhr.response  )};
                    xhr.onerror = function(){ callback(xhr.status) };
                    xhr.open('{METHOD}', '{URL}');
                    
                    xhr.setRequestHeader('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0');
                    xhr.setRequestHeader('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8');
                    xhr.setRequestHeader('Accept-Language', 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3');
                    xhr.setRequestHeader('Upgrade-Insecure-Requests', '1');
                    xhr.setRequestHeader('Sec-Fetch-Dest', 'document');
                    xhr.setRequestHeader('Sec-Fetch-Mode', 'navigate');
                    xhr.setRequestHeader('Sec-Fetch-Site', 'none');
                    xhr.setRequestHeader('Sec-Fetch-User', '?1');
                    xhr.setRequestHeader('Cache-Control', 'max-age=0');
                    xhr.send();
                    """.replace('{METHOD}', method).replace('{URL}', url)
    return data_header

"""
await fetch("https://sbermegamarket.ru/catalog/details/smartfon-apple-iphone-14-pro-max-256gb-deep-purple-100039500627/", {
    "credentials": "include",
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0"
    },
    "method": "GET",
    "mode": "cors"
});
"""