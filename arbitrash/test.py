from selenium import  webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://www.dextools.io/app/aurora/pair-explorer/0x20f8aefb5697b77e0bb835a8518be70775cda1b0')


print()