import time

import pprint
import data
import json

import html_parser

import threading
start_browser = time.time()
from seleniumbase import Driver
driver = Driver(uc=True, chromium_arg='--disable-web-security'  , page_load_strategy = 'none' )
driver.get("https://www.betonline.ag/sportsbook/home/livebetting")
start_parse = time.time()
result = driver.execute_async_script(data.data_header,json.dumps({"gameID":0}))
resultGlobal = result

resultGame = {'games':[]}

gameData = []

countThread = 0
look = threading.Lock()

for game in result['d']['games']:
    try:
        if game['gameStat']==2:
            gameData.append(game)
    except Exception as err:
        print(f"Ошибка парсинга result['d']['games'] : {err}")

def Thread(game):
    global countThread,look
    try:
        result = driver.execute_async_script(data.data_header_gvGameHtml, json.dumps({"gameID":game['gameID']}))
    except Exception as err:
        print(f'Ошибка выполнения POST запроса gvGameHtml: {err}')
        result = {}
    if not 'd' in result:
        return {}
    result = result['d']
    Props = []
    #Парсинг коэфициентов в game
    if 'gameProps' in result:
        if result['gameProps'] != None and result['gameProps'] != '' :
            Props = html_parser.parser_gvGameHtml_Props(result['gameProps'])

    table = {}
    if 'html' in result:
        if result['html'] != None and result['html'] != '':
            table = html_parser.parser_gvGameHtml_Html(result['html'], result['sport'])

    with look:
        resultGame['games'].append(
            {
                'gameId': game['gameID'],
                'props': Props,
                'table' : table
            }
        )
        countThread = countThread - 1


for game in gameData:
    countThread = countThread +1
    thread = threading.Thread(target = Thread, args = (game, )).start()

while True:
    if countThread == 0:
        break

pprint.pprint(resultGame, indent=2)
print("--- Load Broser %s seconds ---" % (start_parse - start_browser  ))
print("--- Job Start Browser %s seconds ---" % (time.time() - start_browser))
print("---Job Parse %s seconds ---" % (time.time() - start_parse))
driver.quit()


