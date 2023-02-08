import time
from collections import namedtuple
import aiohttp
import json

#Result = namedtuple('okex',  ('asks' , 'bids'  ))(0,0)



class hotbit_asyncio:
	urlDepth = 'https://api.hotbit.io/api/v1/order.depth?&limit=5&interval=1e-8&market='
	def __init__(self,timeout:int):
		self.timeout = timeout
	def geturl(self,token):
		return 'https://www.hotbit.io/exchange?symbol=' + token + '_USDT'

	async def depth(self, token:str):
		url = self.urlDepth + token + '/USDT'
		async with aiohttp.ClientSession() as session:
			try:

				start = time.time()
				async with session.get(url=url,timeout=self.timeout) as response:
					response_text = await response.text()
					json_response = json.loads(response_text)['result']
					response.close()
					sum_asks = 0
					sum_bids = 0
					price_ask = 0
					price_bid = 0
					#print('ask:',json_response['asks'])
				#	print('bid:',json_response['bids'])
					for ask in json_response['asks']:
						sum_asks = sum_asks + float(ask[0]) *  float(ask[1])
						price_ask = price_ask + float(ask[0])
					for bid in json_response['bids']:
						sum_bids = sum_bids + float(bid[0]) * float(bid[1])
						price_bid = price_bid + float(bid[0])

					price_ask = price_ask / 5
					price_bid = price_bid / 5

					#print('price bid',price_bid)
					#print('price ask',price_ask)
				#	#print('объём bids',sum_bids)
				#	print('объём asks',sum_asks)

					#price_ask = float(json_response['asks'][0][0])
					#price_bid = float(json_response['bids'][0][0])
					#print('HOTBIT time: '+ str(time.time() - start))
					return namedtuple('hotbit',  ('asks', 'bids','price_ask','price_bid'))(sum_asks,sum_bids,price_ask,price_bid)
			except Exception as err:
				return []


