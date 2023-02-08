import time

start_browser = time.time()
import pprint
import data
import json
import html_parser

from seleniumbase import Driver

driver = Driver(
  uc=True,
  chromium_arg='--disable-web-security',
  page_load_strategy='none',
)

driver.get("https://www.betonline.ag/sportsbook/home/livebetting")
print("--- load browser %s seconds ---" % (time.time() - start_browser))
start_parse = time.time()
result = driver.execute_async_script(data.data_header,
                                     json.dumps({"gameID": 0}))
resultGlobal = result

resultGame = {'games': []}

gameData = []

for game in result['d']['games']:
  try:
    if game['gameStat'] == 2:
      gameData.append(game)
  except Exception as err:
    print(f"Ошибка парсинга result['d']['games'] : {err}")

for game in gameData:
  try:
    result = driver.execute_async_script(
      data.data_header_gvGameHtml, json.dumps({"gameID": game['gameID']}))
  except Exception as err:
    print(f'Ошибка выполнения POST запроса gvGameHtml: {err}')
    result = {}
  if not 'd' in result:
    continue
  result = result['d']
  Props = []
  #Парсинг коэфициентов в game
  if 'gameProps' in result:
    if result['gameProps'] != None and result['gameProps'] != '':
      Props = html_parser.parser_gvGameHtml_Props(result['gameProps'])

  table = {}
  if 'html' in result:
    if result['html'] != None and result['html'] != '':
      table = html_parser.parser_gvGameHtml_Html(result['html'],
                                                 result['sport'])

  resultGame['games'].append({
    'gameId': game['gameID'],
    'props': Props,
    'table': table
  })

pprint.pprint(resultGame, indent=2)
print("--- time load selenium %s seconds ---" % (start_parse - start_browser))
print("--- time parsing Live %s seconds ---" % (time.time() - start_parse))
print("--- FULL TIME %s seconds ---" % (time.time() - start_browser))

driver.quit()
