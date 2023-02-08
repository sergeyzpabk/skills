import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
import redis
import json
from pprint import pprint
from redis.commands.json.path import Path
client = redis.Redis(host='localhost', port=6379, db=0)

data = {

}
"""
data = {
    'NEAR':{
        'sushu':{
            'USDC':{
                'url' : 'https://www.dextools.io/app/aurora/pair-explorer/0x20f8aefb5697b77e0bb835a8518be70775cda1b0',
            },
            'USDT':{
                'url' : 'https://www.dextools.io/app/aurora/pair-explorer/0x03b666f3488a7992b2385b12df7f35156d7b29cd',
            }
        }
    }
}
"""
data = {}

def addToken(name,swap,pair, url):
    if name in data:
        if swap in data[name]:
            if pair in data[name][swap]:
                print('Уже есть в базе', name, swap, pair)

            else:
                data[name][swap].update({
                    pair: {
                        'url': url
                    }
                })
        else:
            data[name].update({
                swap: {
                    pair: {
                        'url': url
                    }
                }
            })


    else:
        data.update({
            name : {
                swap: {
                    pair:{
                        'url':url
                    }
                }
            }
        })



addToken('NEAR', 'sushi', 'USDC', url='https://www.dextools.io/app/aurora/pair-explorer/0x20f8aefb5697b77e0bb835a8518be70775cda1b0')
addToken('NEAR', 'sushi', 'USDT', url='https://www.dextools.io/app/aurora/pair-explorer/0x03b666f3488a7992b2385b12df7f35156d7b29cd')
addToken('BTC', 'orkaV2', 'SOL', url='https://www.dextools.io/app/solana/pair-explorer/7N2AEJ98qBs4PwEwZ6k5pj8uZBKMkZrKZeiC7A64B47u')




browser:webdriver.Chrome

while True:
    try:
        browser = webdriver.Chrome(executable_path='chromedriver.exe')
    except Exception as err:
        try:
            browser.quit()
        except Exception as err:
            print('closed #1 browser:', err)
            continue
        print('Error start browser:: ', err)
    try:
        for token in data:
            for swap in data[token]:
                for pair in data[token][swap]:
                    print(pair)
                    res = data[token][swap][pair]
                    url = res['url']
                    browser.get(url)
                    time.sleep(2)
                    for i in range(5):
                        soup = BeautifulSoup(browser.page_source, "html.parser")
                        if str(soup.head.title).find('$') != -1:
                            title = str(soup.head.title)
                            price = title[title.find('$')+1: title.find('-')-1]
                            break
                        print('не нашли title, sleep')
                        time.sleep(3)
                    #price = soup.find('strong', placement="top").text[1:]
                    print('price: ', price)
                    print('price: ', price)
                    """
                    'NEAR':{
                        'sushi':{
                            'USDT':{
                            price
                            }
                        }    
                    }
                    """
                    if client.exists(token):
                        res:dict
                        res = json.loads(client.get(token))
                        # есть ли в токене swap
                        if swap in res:
                            #Есть ли в swap пара
                            if pair in res[swap]:
                                res[swap][pair]['price'] = price
                            else:
                                res[swap].update({
                                    pair:{
                                        'price':price
                                    }

                                })
                        else:
                            res.update({
                                swap:{
                                    pair:{
                                        'price':price
                                    }
                                }
                            })


                        client.set(token, json.dumps(res))


                    else:
                        new = {}
                        new.update({
                                swap:{
                                    pair:{
                                        'price':price
                                    }
                                }

                        })
                        client.set(token, json.dumps(new))
                        print('добавили в базу:', new)





    except Exception as err:
        raise
        print('Global err::', err)
    try:
        browser.quit()
    except Exception as err:
        print('close ERROR browser', err)

    print("FINNALITY")
    pprint(
        client.keys('*')
    )
