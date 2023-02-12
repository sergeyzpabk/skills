import json
from builtins import print
from time import sleep
from turtle import color

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
from data import get_fetch
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from modulParsing import  pars_all,parsProductHTML
import os

urls_all = []
urls = []

MAX = 99999
FILE_NAME='result.csv'

url = 'https://sbermegamarket.ru/'
url_phobne = 'https://sbermegamarket.ru/catalog/details/smartfon-apple-iphone-14-pro-max-256gb-deep-purple-100039500627/'

if not os.path.isfile(FILE_NAME):
    df = pd.DataFrame(columns=['code', 'category', 'name', 'availability', 'price', 'price_stock', 'url'])
    df.to_csv('result.csv',sep=',',index=False)

browser:webdriver.Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
dir = r'C:\Users\PC\AppData\Local\Google\Chrome\User Data'
options.add_argument("--user-data-dir=" + dir)
options.add_argument('--allow-profiles-outside-user-dir')
options.add_argument('--enable-profile-shortcut-manager')
options.add_argument('--profile-directory=sber3')

#Прописать cookit_profile = input('Cookie Profile:')#

service = ChromeService(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)
browser.get(url=url)

workParsUrl = False

def parsProduct_url(url):
    res = ''
    try:
        res = browser.execute_async_script(get_fetch('GET', url))
    except Exception as err:
        print(f'err: {err}')
    return res


def threadParsProduct():
    max = 0

    global workParsUrl,browser,urls_all,urls
    dataFrame = []

    while workParsUrl or len(urls) > 0 :
        max = max + 1
        if max >MAX : break
        try:
            url = urls.pop()
            res = parsProduct_url(url)
            if str(res).find('itemprop="price"') == -1:
                print(res)
            df = pd.DataFrame([parsProductHTML(res,url)],
                              columns=['code', 'category', 'name', 'availability', 'price', 'price_stock', 'url']
                              )
            df.to_csv('result.csv', mode = 'a', header=False,index=False,sep=',')
            #dataFrame.append( parsProductHTML(res,url) )
        except Exception as err:
            print(err)

    """
            frame[0] код товара
            frame[1] категорий
            frame[2] наименование товара
            frame[3] наличие товара
            frame[4] цена
            frame[5] акционная цена
            frame[6] ссылка
            """

    print('Собрали все данные!')


    pass


def threadParsUrl():
    global urls_all,url, workParsUrl, browser
    page = 0
    while True:
        try:
            page = page + 1
            url_ = 'https://sbermegamarket.ru/catalog/smartfony/page-{page}/'.replace('{page}', str(page))
            res: str
            res = browser.execute_async_script(get_fetch('GET', url_))
            if res.find('<a rel="next"') == -1:
                print('Собрали все Url!!!')
                #Закончили собирать url выходим и сообщаем 2 потоку что мы закончили
                workParsUrl =False
                break
            result = pars_all('<div class="item-title"><a href="', res, '" data-list-id="main"')

            for r in result:
                if not r in urls_all:
                    urls_all.append(r)
                    urls.append(r)


            if not workParsUrl:
                workParsUrl =True
                #Запуск 2 потока
                threading.Thread(target=threadParsProduct).start()

        except Exception as err:
            print(err)

threading.Thread(target=threadParsUrl).start()






