import time
from collections import namedtuple
import aiohttp

#Result = namedtuple('okex',  ('asks' , 'bids'  ))(0,0)

class okex_asyncio:
	name = 'okex'
	urlDepth = 'https://www.okex.com/api/v5/market/books?sz=5&instId='
	def __init__(self,timeout:int):
		self.timeout = timeout
	def geturl(self,token):
		return 'https://www.okx.com/trade-spot/' + token + '-USDT'

	async def depth(self, token:str):
		url = self.urlDepth + token + '-USDT'
		async with aiohttp.ClientSession() as session:
			try:

				start = time.time()
				async with session.get(url=url,timeout=self.timeout) as response:
					response_text = await response.text()
					json_response = await response.json()
					response.close()
					sum_asks = 0
					sum_bids = 0
					price_ask = 0
					price_bid = 0

					for ask in json_response['data'][0]['asks']:
						sum_asks = sum_asks + float(ask[0]) * float(ask[1])
						price_ask = price_ask + float(ask[0])
					for bid in json_response['data'][0]['bids']:
						sum_bids = sum_bids +float(bid[0]) * float(bid[1])
						price_bid = price_bid +float(bid[0])
					#price_ask = float(json_response['data'][0]['asks'][0][0])
					#price_bid = float(json_response['data'][0]['bids'][0][0])
					price_ask = price_ask/5
					price_bid = price_bid/5
				#	print('Okex time:',time.time() - start)
					#return  ('asks', 'bids','price_ask','price_bid')(sum_asks,sum_bids,price_ask,price_bid)
					return namedtuple('okex',  ('asks', 'bids','price_ask','price_bid'))(sum_asks,sum_bids,price_ask,price_bid)
			except Exception as err:
				return []