from selenium import webdriver
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

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

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



def doge_register():
    browser.get('https://dogetrix.com/#')

    browser.implicitly_wait(10)
    okay_btn = browser.find_element_by_id('cookie-btn')
    browser.find_element()
    time.sleep(1)
    okay_btn.click()

    initiate_btn = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/div[2]/div[1]/div/a')
    time.sleep(1)
    initiate_btn.click()

    email_login = browser.find_element_by_name('email')
    email_login.clear()
    email_login.send_keys(username)
    time.sleep(1)

    pass_login = browser.find_element_by_name('password')
    pass_login.clear()
    pass_login.send_keys(password)

    time.sleep(2)

    WebDriverWait(browser, 120).until(lambda x: x.find_element_by_css_selector('.antigate_solver.solved'))
    time.sleep(1)
    enter = browser.find_element_by_id('action-signin')
    enter.click()

    browser.implicitly_wait(10)
    collect_btn = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[5]/div[1]/div/div/div/div/div[2]/a')
    time.sleep(1)
    collect_btn.click()
    time.sleep(3)
    file_name='test.png'
    with open(file_name, 'wb') as file:
        img_id = browser.find_element_by_xpath('//*[@id="adcopy-puzzle-image-image"]')
        file.write(img_id.screenshot_as_png)

    time.sleep(0.5)
    solver = imagecaptcha()
    solver.set_verbose(1)
    solver.set_key(API_KEY)

    captcha_text = solver.solve_and_return_solution(file_name)
    if captcha_text != 0:
        print("Успешно решили 2 капчу: " + captcha_text)
    else:
        print("Провал( Не решили 2 капчу: " + solver.error_code)
        return 0


    key = browser.find_element_by_xpath('//*[@id="adcopy_response"]')
    key.clear()
    key.send_keys(captcha_text)
    btn = browser.find_element_by_xpath('//*[@id="action_claim"]')
    btn.click()




    # try:
    #     # result = solver.recaptcha(
    #     #     sitekey='6LcJYQgbAAAAAIVpInUQ1iNUqvnqdbanZqPtel-8',
    #     #     url='https://dogetrix.com/#')
    #     r = requests.get('http://2captcha.com/in.php?key=ccaa75ddeeeb74cfe56900d3189814c0&method=userrecaptcha&googlekey=6LcJYQgbAAAAAIVpInUQ1iNUqvnqdbanZqPtel-8&pageurl=https://dogetrix.com')
    #     print(r.text)
    #     time.sleep(random.randrange(15, 20))
    #     res_req = requests.get(f'http://2captcha.com/res.php?key=ccaa75ddeeeb74cfe56900d3189814c0&action=get&id={r}')

    # except Exception as e:
    #     sys.exit(e)

def xpath_exists(xpath):
    try:
        browser.find_element_by_xpath(xpath)
        exist = True
    except NoSuchElementException:
        exist = False
    return exist

options = webdriver.ChromeOptions()
opts = Options()
opts.binary_location = "Chrome\\chrome.exe"
opts.add_extension('ant.zip')
browser = webdriver.Chrome(executable_path="Chrome\\chromedriver_86.exe", options=opts)


browser.get('https://antcpt.com/blank.html')

acp_api_send_request(
    browser,
    'setOptions',
    {'options': {'antiCaptchaApiKey': API_KEY}}
)


time.sleep(3)

doge_register()
# img = requests.get("//api-secure.solvemedia.com/papi/media?c=2@Fxgpm4nZi.CN5g.57IFE3EiYDWTB4jaP@ZbwiReM915kENU8bgrS5nn9APTC4lJjoOLLCh-vHWjXYYuwMxiy7VSDFa0qZ1-RfACcsYHRNnVW4H0dJwPpQ69nSYvI1Iu7oBjoApJ6WDLW9O.yXFlDqohWSd5zeSqEQtgCHX4HtEb0iBm.Ec9sXvYcfCX6HeuK7ryQEOvXppWGtvLgmEt4iA7kNHdj8-y6H2mp6om6R2gszQJxUPKWxLGFNugK5v8BaDyw6SOD7sFREJTKxLt0nnhK2P6yAUN9STyM1KD5iIx8vlEosmzdZ5Nm6do20V6nyJkhFXIK0uoA;w=300;h=150;fg=ffffff;bg=212121")
# img_file = open('C:\\Users\\Administrator\\Desktop\\dogecran abuze', 'r')
# img_file.write(img.content)
# get the image source
# img = browser.find_element_by_id('adcopy-puzzle-image-image')
# src = img.get_attribute('src')

# # download the image
# img_file = urllib.request.urlretrieve(src, "captcha.png")
# try:
#     id = solver.send(file=img_file)
#     time.sleep(20)

#     code = solver.get_result(id)
#     result = solver.normal(img_file)
#     time.sleep(1)
#     send_result = browser.find_elements_by_name('adcopy_response').send_keys(result)
#     img_file.close()
#     claim_btn = browser.find_elements_by_id('action_claim')
#     time.sleep(1)
#     claim_btn.click()
# except Exception as e:
#     img_file.close()
#     print('Капча не разгадана')
#     sys.exit(e)

# else:
#     img_file.close()
#     sys.exit('solved: ' + str(result))













