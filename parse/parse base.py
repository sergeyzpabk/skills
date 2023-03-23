from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import json
import random
import asyncio
import concurrent.futures
import urllib
import urllib.request
import requests
import sys
import os
from anticaptchaofficial.imagecaptcha import *
import sqlite3
from seleniumbase import Driver
from time import sleep
from selenium.webdriver.common.by import By
import json

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
username = 'sirius096123456789@gmail.com'
password = 'jDnzQ39f'

#api_key = os.getenv('ccaa75ddeeeb74cfe56900d3189814c0')

API_KEY = '26d7985260270f8ea8b4ab36de2839ac'


def acp_api_send_request(driver, message_type, data={}):
    message = {
        # всегда указывается именно этот получатель API сообщения
        'receiver': 'antiCaptchaPlugin',
        # тип запроса, например setOptions
        'type': message_type,
        # мерджим с дополнительными данными
        **data
    }
    # выполняем JS код на странице
    # а именно отправляем сообщение стандартным методом window.postMessage
    return driver.execute_script("""
    return window.postMessage({});
    """.format(json.dumps(message)))

browser = Driver(
        uc=True,
        port=5999,
        extension_dir=r'C:\programming\ebay.com_parser_Car\parse\ant',
     #   extension_zip='',
    proxy='iusa3030310:40dO2AU7gv@216.158.228.225:7384',
        chromium_arg=r'--allow-profiles-outside-user-dir,--enable-profile-shortcut-manager,user-data-dir=\User1, --profile-directory=Profile_cookie1'
    )
browser.get('https://antcpt.com/blank.html')
acp_api_send_request(
    browser,
    'setOptions',
    {'options': {'antiCaptchaApiKey': API_KEY}}
)
browser.delete_all_cookies()
browser.get('https://portalattysearch-cloud.njcourts.gov/prweb/PRServletPublicAuth/app/Attorney/-amRUHgepTwWWiiBQpI9_yQNuum4oN16*/!STANDARD?AppName=AttorneySearch')


WebDriverWait(browser, 120).until(lambda x: x.find_element(By.CSS_SELECTOR,'.antigate_solver.solved'))
radioButton = WebDriverWait(browser, 120).until(lambda x: x.find_element(By.XPATH,'//*[@id="3ecee6ffArea of Certification"]'))
radioButton.click()
print()

list_Area = []

select_box = browser.find_element(By.ID, "$PAttorney$pCertificationList")
options = [x for x in select_box.find_elements(By.TAG_NAME,"option")]
for element in options:
    list_Area.append(element.get_attribute("value"))

list_County = []

select_box = browser.find_element(By.ID, "$PAttorney$pCountyList")
options = [x for x in select_box.find_elements(By.TAG_NAME,"option")]
for element in options:
    list_County.append(element.get_attribute("value"))

print(list_Area)
print('-----------------')
print(list_County)

for area in range(0, len(list_Area)):
    for country in range(0, len(list_County)):
        try:
            browser.delete_all_cookies()
            browser.get(
                'https://portalattysearch-cloud.njcourts.gov/prweb/PRServletPublicAuth/app/Attorney/-amRUHgepTwWWiiBQpI9_yQNuum4oN16*/!STANDARD?AppName=AttorneySearch')

            # WebDriverWait(browser, 120).until(lambda x: x.find_element(By.CSS_SELECTOR,'.antigate_solver.solved'))
            radioButton = WebDriverWait(browser, 120).until(
                lambda x: x.find_element(By.XPATH, '//*[@id="3ecee6ffArea of Certification"]'))
            radioButton.click()
            WebDriverWait(browser, 120).until(lambda x: x.find_element(By.CSS_SELECTOR, '.antigate_solver.solved'))

            WebDriverWait(browser, 120).until(lambda x: x.find_element(By.XPATH, '//*[@id="3ecee6ffArea of Certification"]'))
            sleep(0.5)
            select_area = Select(browser.find_element(By.ID, '$PAttorney$pCertificationList'))
            select_area.select_by_index(area)

            select_country = Select(browser.find_element(By.ID, '$PAttorney$pCountyList'))
            select_country.select_by_index(country)

            sumbit = browser.find_element(By.CSS_SELECTOR,'#RULE_KEY > div.layout.layout-noheader.layout-noheader-default > div > div > div.content-item.content-layout.item-4.flex.flex-row > div > div > div > div.content-item.content-field.item-2.flex.flex-row.dataValueWrite > span > button')
            sumbit.click()

            WebDriverWait(browser, 120).until(
                lambda x: x.find_element(By.CSS_SELECTOR, '#RULE_KEY > div > div > div > div.content-item.content-layout.item-3.flex.flex-row > div > div > div > div.content-item.content-field.item-2.remove-bottom-spacing.remove-right-spacing.flex.flex-row.dataValueWrite > span > button'))

            print(f'Module Parsing page: {list_Area[area]}_{list_County[country]}')
            sleep(2)
            #input('stop')



        except Exception as err:
            print(f'Err{err} in {list_Area[area]}_{list_County[country]} ')



input('stop')