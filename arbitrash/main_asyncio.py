from collections import namedtuple
import time
import asyncio
import logging
import math
from logging import exception
import telebot
from DataBase import DB

from okex_asyncio import okex_asyncio
from gate_io_asyncio import gate_io_asyncio
from hotbit_asyncio import hotbit_asyncio
from huobi_asyncio import huobi_asyncio
from kucoin_asyncio import kucoin_asyncio
from bitrue_asyncio import bitrue_asyncio
from crypto_asyncio import crypto_asyncio
from ftx_asyncio import  ftx_asyncio
from kraken_asyncio import  kraken_asyncio
from mexc_asyncio import mexc_asyncio
from poloniex_asyncio import  poloniex_asyncio
from binance_asyncio import binance_asyncio
from hoo_asyncio import  hoo_asyncio

import config



tokens = """
ATOM
ALGO
MATIC
SHIB
IOTX
EPS
GLM
NEAR
AUDIO
FLOW
HNT
COMP
STX
SLP
FARM
QI
RUNE
SDN
HOD
ZRX
FORTH
GHST
BCH
OMG
DOT
IQ
BAND
1INCH
BTC
NKN
RSR
AR
AVAX
MIR
FTM
POWR
KNC
RADAR
CVX
ONE
RLC
TONIC
ANKR
SUSHI
ATOM
SC
PENDLE
QUICK
LPT
WBTC
BOBA
ONT
GODS
SNX
RLY
MANA
API3
DAI
VTHO
CSPR
DERC
SGB
XYO
SOL
NMR
FET
DAR
MKR
ETC
CELR
OGN
ICP
ETH
MCO
NEO
REN
KLAY
LRC
BADGER
ADA
ICX
STORJ
REQ
RARI
VET
PAXG
TRB
PAX
USDT
BNT
DOGE
HBAR
OXT
CHR
MLN
NANO
WAVES
ILV
VVS
CHZ
TRU
XRP
CTSI
JASMY
GUSD
SAND
KAVA
C98
AMP
OCEAN
KEEP
CQT
UMA
STRAX
TUSD
IMX
LTC
USDC
EGLD
RGT
THETA
SPELL
ENJ
FXS
CRO
BOSON
INJ
PLA
CRV
NU
GRT
TRIBE
EFI
DYDX
TFUEL
ENS
ANY
MASK
SRM
UNI
AAVE
QNT
PERP
ALICE
XLM
LINK
CKB
BOND
QTUM
YFI
XTZ
LUNA
SUPER
POLS
KSM
ELON
EOS
FIL
POLY
RNDR
BICO
BAL
GALA
RAD
BAT
SKL
GTC
YGG
MOVR
BUSD
ZIL
AXS
ARPA
COTI
BNB
TRX
LEO
FTT
XMR
APE
KCS
ZEC
HT
BTT
BSV
MIOTA
USDP
XEC
USDN
CAKE
OKB
NEXO
USDD
DASH
GMT
CELO
GNO
XDC
DCR
MINA
XEM
GT
FEI
BTG
KDA
BORA
ROSE
GLMR
IOST
LDO
XYM
JST
VGX
RVN
CHSB
SCRT
ZEN
SXP
NFT
HIVE
BTRST
MXC
RENBTC
DGB
TWT
CEL
WOO
LSK
ACA
USTC
XPRT
FLUX
XNO
WIN
MX
CFX
MED
XDB
ORBS
VLX
DAO
CEEK
XCH
ONG
PUNDIX
SYS
SNT
TEL
ARDR
DENT
CVC
WXT
SUSD
UOS
TRAC
DIVI
DAG
REP
HEX
WTRX
stETH
YOUC
BTCB
XCN
WBNB
TON
FRAX
BTTOLD
HBTC
DFI
LUSD
LUNC
SAFE
WEMIX
XAUT
T
BIT
HUSD
NXM
SAPP
TTT
OSMO
CCXX
FRTS
LN
EVER
BNX
LOOKS
BEST
ASTR
KOK
CBG
RPL
HUM
GAL
MOB
RACA
MVL
WVLX
PLTC
TITAN
EURS
BSW
XSGD
ARRR
SURE
AVINOC
MPL
AURORA
SOLO
USDX
FX
1ECO
CTC
RAY
SUN
PEOPLE
vUSDC
STEEM
LOCUS
MCT
HXRO
WRX
FUN
DESO
PYR
ASD
ARK
STMX
RBTC
DEP
XWC
ABBC
HEDG
BRG
XCAD
BTCST
MTL
REV
LQTY
TLM
META
MDX
METIS
DAWN
MV
JOE
REEF
EWT
STRK
XVG
UQC
UTK
QKC
AMA
SSX
STPT
NEST
BFC
ORC
HYN
RKN
DERO
ANT
RIF
ERG
CFG
MBOX
ETN
HOO
ACH
CENNZ
MBL
LYXe
TLOS
MAID
HERO
PRO
LOOM
PROM
BAKE
SNL
AGIX
WMT
ALPHA
SSV
KLV
CTK
ADS
DKA
ANC
ZEON
OUSD
GTN
EXRD
FWT
HUNT
BLOK
ZB
CUSD
SPS
VERI
AMPL
CRTS
CORE
DPR
DPI
SAFEMOON
vBUSD
TT
DVI
TOMO
AERGO
BETA
NRG
NSBT
XVS
WOZX
MNGO
KAI
DUSK
DMCH
STAKE
VAI
HI
ALEPH
ONUS
DVF
UFO
QC
aETHc
XPR
LCX
CRE
FOX
SOV
ORN
MFT
IDEX
BNANA
AKT
SOS
AIOZ
COCOS
ATOLO
AXEL
AQT
GENE
YOOSHI
ALT
EGG
CON
MOC
RBN
ALPACA
ICHI
SPA
RMRK
SFP
STARL
FLETA
MC
LAT
BIFI
PRE
XNC
CTCN
UBT
WAN
MUSD
POND
MONA
BCD
GXC
HTR
TKO
MLK
UPP
VR
CLT
NOIA
BTS
ALCX
ELA
KILT
VELO
CBK
RFR
BOO
BABY
VOXEL
QRDO
VRSC
ALPINE
CLV
LOG
TROY
LINA
SFUND
AGLD
BEL
HNS
GRS
FCT,FCT2
AVA
QOM
LTO
EUM
SWAP
H2O
PHA
ZLW
HYDRA
BMX
RAI
RISE
LON
NCT
DREP
VXV
ULT
DIA
VEGA
SERO
TPT
vUSDT
ASM
DNT
ZASH
VRA
MWC
CUDOS
IRIS
SWP
BZRX
SBD
ERN
ADX
DDX
KMD
FLM
COS
SOUL
CET
TVK
WNXM
PEAK
SDAO
GAS
KRT
QUACK
BTSE
RSV
BIOT
DG
USDK
ATA
HARD
AKRO
erowan
DAD
MEV
DXD
COVAL
LOKA
ALI
BZZ
CTXC
YLD
MNW
AMO
TORN
MIX
CHESS
KP3R
RARE
WILD
FIO
AE
LA
APX
BLCT
BOR
DATA
SIX
NYE
FSN
MDT
OM
AHT
HIGH
PNK
FIRO
FRONT
VBIT
ALBT
RFOX
NIF
CUBE
PNY
TABOO
MET
MSOL""".split('\n')


#604 tokens

"""
for token in tokens:
	DB.insert_Newtoken(token)
"""


bot=telebot.TeleBot(config.TELEGRAM_API_BOT)

#logging.basicConfig(filename="sample.log", level=logging.DEBUG)
PROCENT = 2.0
PROCENT = 0.8
PROCENT_MAX = 30.0
VOLUME = 500
POSITION = 5
Exch = namedtuple('exch',  ('name' , 'clas' ))

TIMEOUT = 3

list_arb = [
	'hotbit',
	'okex',
	'gate_io',
	'huobi',
	'kucoin',
	'crypto',
	'ftx',
	'kraken',
	'mexc',
	'poloniex',
	'binance',
	'hoo',
]


EXCH = (
	#Exch('hotbit',hotbit_asyncio(TIMEOUT)),
	#Exch('hotbit',bitrue_asyncio(TIMEOUT)),
	Exch('okex', okex_asyncio(TIMEOUT)),
	Exch('gate_io',gate_io_asyncio(TIMEOUT)),
	Exch('huobi',huobi_asyncio(TIMEOUT)),
	Exch('kucoin',kucoin_asyncio(TIMEOUT)),
	Exch('crypto',crypto_asyncio(TIMEOUT)),
	Exch('ftx',ftx_asyncio(TIMEOUT)),
	Exch('kraken',kraken_asyncio(TIMEOUT)),
	Exch('mexc',mexc_asyncio(TIMEOUT)),
	Exch('poloniex',poloniex_asyncio(TIMEOUT)),
	Exch('binance',binance_asyncio(TIMEOUT)),
	Exch('hoo',hoo_asyncio(TIMEOUT)),
)




def get_class(cls):
	for i in range(0, len(EXCH)):
		if cls == EXCH[i].name:
			return EXCH[i].clas

def log(s):
	#logging.info(str(time.ctime()) + ' ' +str(s))
	pass


def get_procent(min,max):
	try:
		return math.fabs((min - max) / ((min + max) / 2)) * 100
	except:
		return 0


async def asynchronous(token):
	try:
		tokens = DB.getAllToken()
		futures = []
		print('Token:', token)
		for exch in EXCH:
			print(exch.name, ':',tokens[token][exch.name] )
			if (str(tokens[token][exch.name]) == 'True') or (str(tokens[token][exch.name]) == '1'):
				continue

			futures.append(asyncio.create_task(exch.clas.depth(token=token)))
			



			# futures = [asyncio.create_task(exch.clas.depth(token=token)) for exch in EXCH]
		print('len: ',len(futures))
	except Exception as err:
		raise





	done, pending = await asyncio.wait(
		futures)




	min_res =[]
	max_res = []

	for d in done:
		if d.exception() != None:
			print('!' + str(d.exception()))
			continue
		if d.result() == []:
			continue
		print(d.result())
		log(str(d.result()))
		min_res.append( d.result())
		max_res.append( d.result())

	if len(min_res)<2:
		log('Получили меньше 2 пар')
		print('Получили меньше 2 пар')
		return

	min_res.sort(key=lambda x: (x.price_ask))
	max_res.sort(key=lambda x: (x.price_bid),reverse=True)

	arb_min = []
	arb_max = []
	text = ''
	pair = ''
	send = False
	text_i = ''

	data_j = False

	text_j = ''
	for i in range(0,len(min_res)):
		arb_min = min_res[i]
		name_min = arb_min.__class__.__name__

		text_i=''
		text_j = ''

		data_j = False

		pair = token + '-USDT'
		text_i = text_i + 'Пара: ' + pair + '\n'
		text_i = text_i + 'Биржа: ' + str(name_min) + '\n'
		text_i = text_i + 'Минимальна цена:' + str(round(min_res[i].price_ask, 5)) + '\n'
		text_i = text_i + 'Объём за ' + str(POSITION) + ' позиций:' + str(min_res[i].asks) + '\n'
		text_i = text_i + get_class(name_min).geturl(token) + '\n'
		text_i = text_i + '\n'



		for j in range(0,len((max_res))):
			arb_max = max_res[j]
			name_max = arb_max.__class__.__name__

			if ( min_res[i].bids<VOLUME ) or ( max_res[j].asks<VOLUME ):
				#print('NEXT, Малые объёмы')
				continue

			if arb_min.price_ask>arb_max.price_bid:
				#print('Next, Перекос цены')
				continue

			if arb_max == arb_min:
				#print('Next, Пара совпала')
				continue

			if (arb_min==[]) or (arb_max==[]):
				#print('next, Нет данных для объёма')
				continue


			procent = get_procent(arb_min.price_ask, arb_max.price_bid)
			print('Процент: ', procent)
			if (procent < PROCENT) or (procent>PROCENT_MAX):
				continue
			print('Удача, Procent:',procent   )
			print('I=',i)
			send =True
			text_j = text_j + 'Разница: ' + str(round(procent, 2)) + '% \n\n'
			text_j = text_j + 'Биржа: ' + str(name_max) + '\n'
			text_j = text_j + 'Максимальна цена:' + str(round(arb_max.price_bid, 5)) + '\n'
			text_j = text_j + 'Объём за ' + str(POSITION) + ' позиций:' + str(arb_max.bids) + '\n'
			text_j = text_j + get_class(name_max).geturl(token) + '\n'
			data_j = True

		if data_j:
			text = text + text_i + text_j
			text = text + '\n------------\n'
		# Цикл по минимальной цене
	if send:
		DB.deleteOldTime_token()
		if DB.check_token(token):
			#DB.updateTime(name_min, name_max, pair)

			DB.updateTime_token(token)
			"""
			Обновлять в тг
			"""
		else:
			DB.insert_token(token)
			print(text)
			text = text + 'Объём больше' + str(VOLUME) + '\n'
			text = text + '\n'
			try:
				bot.send_message(chat_id=config.CHAT_ID, text=text, disable_web_page_preview=True)
				print('tg')
			# time.sleep(15)
			except Exception as err:
				log('ошибка отправки в tg' + str(err))
				print('ошибка отправки в tg', err)


while True:
	start = time.time()

	tokens = DB.getAllToken()


	for token in tokens:
		try:

			print('Token:', token)
			ioloop = asyncio.get_event_loop()
			ioloop.run_until_complete(asynchronous(token))
		except Exception as err:
			#raise
			log('Глобальная ошибка в цикле TOKEN::' +str(err) )
			print('Глобальная ошибка в цикле TOKEN::' +str(err) )



	finish = (time.time() - start)
	try:
		text = 'Время прохода всех токенов заняло: ' + str(finish)
		bot.send_message(chat_id=config.CHAT_ID, text=text, disable_web_page_preview=True)
	except Exception as err:
		pass





"""
	for res in max_res:
		if res.bids<VOLUME:
			continue
		arb_max = res
		break


	for res in min_res:
		if res.asks<VOLUME:
			continue
		arb_min = res
		break
	"""


