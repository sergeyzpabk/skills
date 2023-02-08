import time
from collections import namedtuple
import aiohttp

#Result = namedtuple('okex',  ('asks' , 'bids'  ))(0,0)

class gate_io_asyncio:
	name = 'gate_io'
	urlDepth = 'https://api.gateio.ws/api/v4/spot/order_book?limit=5&currency_pair='
	def __init__(self,timeout:int):
		self.timeout = timeout
	def geturl(self,token):
		return 'https://www.gate.io/ru/trade/' + token + '_USDT'

	async def depth(self, token:str):
		url = self.urlDepth + token + '_USDT'
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

					for ask in json_response['asks']:
						sum_asks = sum_asks + float(ask[0]) * float(ask[1])
						price_ask = price_ask + float(ask[0])
					for bid in json_response['bids']:
						sum_bids = sum_bids +float(bid[0]) * float(bid[1])
						price_bid = price_bid +float(bid[0])

					price_bid = price_bid /5
					price_ask = price_ask /5

					#price_ask = float(json_response['asks'][0][0])
					#price_bid = float(json_response['bids'][0][0])
				#	print('GATE_IO time:',time.time() - start)
					#return  ('asks', 'bids','price_ask','price_bid')(sum_asks,sum_bids,price_ask,price_bid)
					return namedtuple('gate_io',  ('asks', 'bids','price_ask','price_bid'))(sum_asks,sum_bids,price_ask,price_bid)
			except Exception as err:
				return []


