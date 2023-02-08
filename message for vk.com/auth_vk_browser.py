from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


def auth_vk_driver():
    token = ''
    opts = Options()
    opts.binary_location = "Chrome\\chrome.exe"
    dir = 'Chrome/User Data/'
    opts.add_argument("--user-data-dir=" + dir)
    opts.add_argument('--allow-profiles-outside-user-dir')
    opts.add_argument('--enable-profile-shortcut-manager')
    #opts.add_argument('--headless')
    opts.add_argument("--start-maximized")
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    opts.add_experimental_option('useAutomationExtension', False)
    #driver.minimize_window()
    #test  - тестовый аккаунт#
    #opts.add_argument('--profile-directory=vk')  # с балансом
    opts.add_argument('--profile-directory=test1')  # с балансом
    #opts.add_argument('--profile-directory=irina')  # Ирина
    opts.add_experimental_option("useAutomationExtension", False)
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    browser = Chrome(executable_path="Chrome\\chromedriver_86.exe", chrome_options=opts)

    #browser.get('https://oauth.vk.com/authorize?client_id=2685278&scope=messages&response_type=token')
    #windows desctop
    #browser.get('https://oauth.vk.com/authorize?client_id=3697615&scope=messages&response_type=token')
    browser.get('https://oauth.vk.com/authorize?client_id=2685278&scope=1073741823&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1')

    browser.implicitly_wait(1)
    while True:
        url = browser.current_url
        if str(url).find('access_token=') != -1:
            token = url[url.find('access_token=') + len('access_token='): url.find('&')]
            browser.quit()
            break
    print('browser token = ', token)
    return token
