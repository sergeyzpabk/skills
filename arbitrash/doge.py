
from data import username_list, password_list, proxy_list
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver
from datetime import date, datetime
from anticaptchaofficial.imagecaptcha import *
from fake_useragent import UserAgent
import pickle

API_KEY = '26d7985260270f8ea8b4ab36de2839ac'
# useragent = UserAgent()
MAX_CAPTCHA = 3 # максимум 3 раза решать на 1 аккаунт капчу )
def acp_api_send_request(driver, message_type, data={}):
    message = {
        'receiver': 'antiCaptchaPlugin',
        'type': message_type,
        **data
    }
    return driver.execute_script("""
    return window.postMessage({});
    """.format(json.dumps(message)))

def doge_register():

    time.sleep(3)
    try:

        name = str(username).replace('.','')
        print('Загрузка cookie:',name)
        cookies = pickle.load(open("cookie\cookies_"+name+".pkl", "rb"))
        for cookie in cookies:
            browser.add_cookie(cookie)
        print('Успешно загрузили cookie: ',name)
    except Exception as err:
        print('Ошибка загрузки cookie:', name, err)
    browser.get('https://dogetrix.com/')
    time.sleep(3)
    #return 0
    if browser.page_source.find('Balance:') != -1:

        print('Авторищовались по cookie')
    else:
        try:
            try:
                WebDriverWait(browser, 20).until(lambda x: x.find_element_by_id('cookie-btn'))
                okay_btn = browser.find_element_by_id('cookie-btn')
                okay_btn.click()
            except Exception as err:
                print('Ошибка нажатия btn-cookie', err)
            time.sleep(1)

            initiate_btn = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[3]/div/div/div/div/div/div[2]/div[1]/div/a')
            initiate_btn.click()
            time.sleep(1)

            WebDriverWait(browser, 120).until(lambda x: x.find_element_by_css_selector('.antigate_solver.solved'))

            WebDriverWait(browser, 20).until(lambda x: x.find_element_by_name('email'))
            email_login = browser.find_element_by_name('email')
            email_login.clear()
            time.sleep(0.1)
            email_login.send_keys(username)
            time.sleep(0.1)

            WebDriverWait(browser, 20).until(lambda x: x.find_element_by_name('password'))
            pass_login = browser.find_element_by_name('password')
            pass_login.clear()
            pass_login.send_keys(password)
            time.sleep(3)

            #Сохраняем куки
            pickle.dump(browser.get_cookies(), open("cookie\cookies_" + name + ".pkl", "wb"))
        except Exception as ex:
            print(ex)
    try:
        captcha_bool = False
        for i in range(MAX_CAPTCHA):
            WebDriverWait(browser, 20).until(lambda x: x.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[5]/div[1]/div/div/div/div/div[2]/a'))
            collect_btn = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[5]/div[1]/div/div/div/div/div[2]/a')
            collect_btn.click()
            time.sleep(1)
            file_name='captcha.png'
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
            time.sleep(0.1)
            key.send_keys(captcha_text)
            time.sleep(0.1)
            btn = browser.find_element_by_xpath('//*[@id="action_claim"]')
            btn.click()
            if str(browser.page_source).find('Captcha is wrong') == -1:
                #Прошли капчу)
                print('Успешно прошли капчу')
                captcha_bool=True
                break




    except Exception as err:
        print('Глобальная ошибка : ', err)

while True:
    start_pack_time = datetime.now()
    i = 0
    print(f'Время старта{start_pack_time}')
    for i in range(len(username_list)):
        try:
            start_time = datetime.now()
            username = username_list[i]
            password = password_list[i]
            options = webdriver.ChromeOptions()
            opts = Options()
            # opts.binary_location = "Chrome\\chrome.exe"
            # opts.add_argument(f"user-agent={useragent.random}")
            opts.add_argument('--disable-blink-features=AutomationControlled')
            opts.add_argument('--log-level=3')
            proxy_options ={
                "proxy":{
                    "https": f"http://{proxy_list[i]}"
                }
            }
            opts.add_extension('ant.zip')
            opts.binary_location = "Chrome\\chrome.exe"
            #browser = webdriver.Chrome(executable_path="C:\\Users\\Administrator\\chromedriver.exe", options=opts, seleniumwire_options=proxy_options)
            browser = webdriver.Chrome(executable_path="Chrome\\chromedriver_86.exe", options=opts, seleniumwire_options=proxy_options)

            browser.get('https://antcpt.com/blank.html')

            acp_api_send_request(
                browser,
                'setOptions',
                {'options': {'antiCaptchaApiKey': API_KEY}}
            )

            doge_register()
            browser.close()
            browser.quit()
            i+=1
            end_time = datetime.now()
            account_time = end_time-start_time
            print(f'Пройден аккаунт №{i}, Email: {username}, Прокси: {proxy_list[i-1]}\nВремя за которое был пройден аккаунт: {account_time} ')
        except Exception as ex:
            print(ex)
            print(f"Упс, что-то пошло не так, аккаунт {i-1} не удалось обработать")
            browser.close()
            browser.quit()
            i+=1
    
    end_pack_time = datetime.now()
    print(f'Время окончания: {end_pack_time}')
    time_per_accs_pack = end_pack_time - start_pack_time
    print(f"------------------------------Время за которое была пройдена пачка аккаунтов: {time_per_accs_pack}------------------------------")









