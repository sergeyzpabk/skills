import time
from builtins import print
from collections import namedtuple
import aiohttp

#Result = namedtuple('okex',  ('asks' , 'bids'  ))(0,0)

class bitrue_asyncio:
	name = 'bitrue'
	urlDepth = 'https://www.bitrue.com/api/v1/depth?limit=5&symbol='
	def __init__(self,timeout:int):
		self.timeout = timeout
	def geturl(self,token):
		return str('https://www.bitrue.com/trade/' + token + '_USDT')

	async def depth(self, token:str):
		url = self.urlDepth + token + 'USDT'
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
					#json_response = json_response['data']
					for ask in json_response['asks'][:5]:
						sum_asks = sum_asks + float(ask[0]) * float(ask[1])
						price_ask = price_ask + float(ask[0])
					for bid in json_response['bids'][:5]:
						sum_bids = sum_bids +float(bid[0]) * float(bid[1])
						price_bid = price_bid +float(bid[0])

					price_bid = price_bid / 5
					price_ask = price_ask / 5
					"""
					print('buy',json_response['bids'][:5])
					print('sell',json_response['asks'][:5])
					print('buy',price_bid)
					print('sell',price_ask)
					"""
					return namedtuple(self.name,  ('asks', 'bids','price_ask','price_bid'))(sum_asks,sum_bids,price_ask,price_bid)
			except Exception as err:
				return []


