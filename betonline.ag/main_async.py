import time
import asyncio
import pprint
import data
import json

import html_parser


start_browser = time.time()
from seleniumbase import Driver
driver = Driver(uc=True, chromium_arg='--disable-web-security'   )
driver.get("https://www.betonline.ag/sportsbook/home/livebetting")
start_parse = time.time()
result = driver.execute_async_script(data.data_header,json.dumps({"gameID":0}))
resultGlobal = result

resultGame = {'games':[]}

gameData = []

for game in result['d']['games']:
    try:
        if game['gameStat']==2:
            gameData.append(game)
    except Exception as err:
        print(f"Ошибка парсинга result['d']['games'] : {err}")

async def Parse(game):
    try:
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, driver.execute_async_script, data.data_header_gvGameHtml, json.dumps({"gameID":game['gameID']}))
        #result = await driver.execute_async_script(data.data_header_gvGameHtml, json.dumps({"gameID":game['gameID']}))
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


    resultGame['games'].append(
        {
            'gameId': game['gameID'],
            'props': Props,
            'table' : table
        }
    )

def main():
    tasks = []
    for game in gameData:
        tasks.append(asyncio.create_task(Parse(game)))
        for task in tasks:
            await task
    pprint.pprint(resultGame, indent=2)
    print("--- Load Broser %s seconds ---" % (start_parse - start_browser))
    print("--- Job Start Browser %s seconds ---" % (time.time() - start_browser))
    print("---Job Parse %s seconds ---" % (time.time() - start_parse))



asyncio.run(main())




