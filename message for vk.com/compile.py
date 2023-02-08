import sys
from cx_Freeze import setup, Executable

executables = [Executable('send_message.py',
targetName='vk Sender.exe',
icon='icon.ico')]


includes = ['sys','GUI','PyQt5', 'threading', 'time', 'json', 'vk_api','openpyxl', 'random', 'datetime','python_rucaptcha']

#zip_include_packages = ['json', 'os', 'random', 'threading', 'time', 'tkinter', 're', 'time', 'pickle', 'selenium.webdriver', 'selenium.webdriver.chrome.options', 'selenium.webdriver.common.action_chains', 'urllib3.exceptions']

include_files = [
    'base.',
    'credentials',
    'data',
    'data_file.json',
    'url_file.json',
    'chrome/'
]

include_files = []

options = {
'build_exe': {
'include_msvcr': True,
'includes': includes,
#'zip_include_packages': zip_include_packages,
'build_exe': 'build_windows',
'include_files': include_files,
}
}

setup(name='Расслыка [Ирина Ростова]',
version='0.0.3',
description='SergeyZpAbk',
executables=executables,

options=options)