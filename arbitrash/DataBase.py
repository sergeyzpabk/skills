import sqlite3
import time
import math
import sys
import  os
import requests
import configparser

db = (os.path.abspath(os.path.join(os.path.dirname(__file__))) + r"\\DataBase.db")  # читаем конфиг


#db = r""

#Время через сколько удалиться пара
MAXTIMEDELETE = 60 * 5

tokens = """AGLD
MATIC
SHIB
IOTX
EPS
GLM
BRZ
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
HOT
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
ALGO
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
WAXP
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
COTI"""

pref = '_USDT'

tokens = tokens.split('\n')

"""
get_exchs -> Получить список всех бирж



"""

class DBClass:
	def __init__(self):
		pass

	def get_exchs(self):
		try:
			conn = sqlite3.connect(db)
			cursor = conn.cursor()
			cursor.execute(
				'SELECT * FROM exchs' ,
			)
			res = cursor.fetchall()
			result = []
			for r in res:
				result.append(r[0])
			return result
		except Exception as err:
			return []
			pass

	def getTable(self,table:str):
		result = {}
		result.update({'name':table,
		               'list':{}})
		try:
			conn = sqlite3.connect(db)
			cursor = conn.cursor()
			cursor.execute(
				'SELECT * FROM ' + table,
				())
			res = cursor.fetchall()
			if res == []:
				return result


			for l in res:
				result['list'].update({ l[0]:{

					'price': l[1],
					'date': l[2],
				}
				})

			return result

		except Exception as err:
			print('Ошибка:', err)
			return result

	def tokenCheck(self,table, token):
		result = False
		try:
			conn = sqlite3.connect(db)
			cursor = conn.cursor()
			cursor.execute(
				'SELECT * FROM '+table+' WHERE token=?',
				(token,))
			res = cursor.fetchall()
			if not res==[]:
				result = True
		except Exception as err:

			print('Ошибка бд: check_token::', err)
		return result

	def updateBan(self, id, exch):
		try:
			conn = sqlite3.connect(db)
			print(db)
			cursor = conn.cursor()
			cursor.execute(
				f'SELECT {exch} From tokens WHERE id={id}',
				)
			res = cursor.fetchall()
			b = res[0][0]
			if b == 'False':
				b = 'True'
			else:
				b = 'False'
			print(b)
			cursor.execute(
				f'UPDATE tokens SET {exch}=? WHERE (id=?) ',
				(b,id))
			conn.commit()
		except Exception as err:
			print('Ошибка бд: check_para::', err)
		pass

	def insert_Newtoken(self,token:str):
		try:
			now = time.time()
			conn = sqlite3.connect(db)
			cursor = conn.cursor()
			false = str('"False",' * len(DB.get_exchs()))[:-1]

			zapros = f'INSERT INTO tokens VALUES( NULL, "{token}",{false} ) '
			cursor.execute(
				zapros
			)
			conn.commit()
			cursor.execute('SELECT last_insert_rowid();')
			res = cursor.fetchall()
			print(res)
			return res[0][0]
		except Exception as err:
			print('Ошибка бд: insert::', err)
			return -1

	def getList_id_token(self):
		result = {}
		try:
			conn = sqlite3.connect(db)
			cursor = conn.cursor()
			cursor.execute(
			'SELECT id,token FROM tokens',
			)
			res = cursor.fetchall()
			#print(res)
			return res

		except:
			return result
			print(' Ошибка бд')
	def getTokensFull(self):
			result = {}
			try:
				conn = sqlite3.connect(db)
				cursor = conn.cursor()
				cursor.execute(
				'SELECT * FROM tokens',
				)
				res = cursor.fetchall()
				#print(res)
				return res

			except:
				return result
				print(' Ошибка бд')
	def getToken(self, token):
				result = {}
				try:
					conn = sqlite3.connect(db)
					cursor = conn.cursor()
					cursor.execute(
					f'SELECT * FROM tokens Where token="{token}"',
					)
					res = cursor.fetchall()
					#print(res)
					return res

				except:
					return result
					print(' Ошибка бд')



	def getAllTokenBan(self):
		result = {}
		try:
			conn = sqlite3.connect(db)
			cursor = conn.cursor()
			cursor.execute(
			'SELECT * FROM tokens',
			)
			res = cursor.fetchall()
			#print(res)
			exch = DB.get_exchs()
			for r in res:
				temp = r
				temp = temp[2:]
				result.update({r[1]:{}})
				for t in range(0,len(temp)):
					result[r[1]].update({exch[t]:temp[t]})
			return result

		except:
			return result
			print(' Ошибка бд')

	def getAllToken(self):
		result = {}
		try:
			conn = sqlite3.connect(db)
			cursor = conn.cursor()
			cursor.execute(
			'SELECT * FROM tokens',
			)
			res = cursor.fetchall()
			#print(res)
			exch = DB.get_exchs()
			for r in res:
				temp = r
				temp = temp[2:]
				result.update({r[1]:{}})
				for t in range(0,len(temp)):
					result[r[1]].update({exch[t]:temp[t]})
			return result

		except:
			return result
			print(' Ошибка бд')

	def getTokens(self, token:str):
		try:
			conn = sqlite3.connect(db)
			cursor = conn.cursor()
			cursor.execute(
				'SELECT * FROM tokens WHERE token=?',
				(token,))
			res = cursor.fetchall()
			print(res)

		except Exception as err:
			print('ОШибка получения токека,', err)

	def getTokenID(self, id):
		try:
			conn = sqlite3.connect(db)
			cursor = conn.cursor()
			cursor.execute(
				'SELECT * FROM tokens WHERE id=?',
				(id,))
			res = cursor.fetchall()
			print(res)
			return res[0][2:]
		except Exception as err:
			print('ОШибка получения токека,', err)


	def getTokenName_ID(self, id):
		try:
			conn = sqlite3.connect(db)
			cursor = conn.cursor()
			cursor.execute(
				'SELECT * FROM tokens WHERE id=?',
				(id,))
			res = cursor.fetchall()
			print(res)
			return res[0][1]
		except Exception as err:
			print('ОШибка получения токека,', err)


	def deleteToken(self, id, token):
			try:
				conn = sqlite3.connect(db)
				cursor = conn.cursor()
				cursor.execute(
					'Delete FROM tokens WHERE id=? and token=?',
					(id,token))
				res = conn.commit()
				print('coomit:',res)
				return res
			except Exception as err:
				print('ОШибка получения токека,', err)

	def insert_token(self,token:str):
		try:
			now = time.time()
			conn = sqlite3.connect(db)
			cursor = conn.cursor()
			cursor.execute(
				'INSERT INTO TOKEN(token,date) VALUES(?, ? ) ' ,
				(token,now))
			conn.commit()
			return True
		except Exception as err:
			print('Ошибка бд: insert::', err)
			return False
	def check_token(self,token:str):
		result = False
		try:
			conn = sqlite3.connect(db)
			cursor = conn.cursor()
			cursor.execute(
				'SELECT * FROM TOKEN WHERE token=?  ' ,
				(token,))
			res = cursor.fetchall()
			if not res==[]:
				result = True
		except Exception as err:
			print('Ошибка бд: check_para::', err)
		return result

	def deleteOldTime_token(self):
		print('')
		try:
			conn = sqlite3.connect(db)
			cursor = conn.cursor()
			cursor.execute(
				'SELECT * FROM TOKEN',

			)

			res = cursor.fetchall()
			for r in res:
				now = time.time()
				oldTime = float(r[1])
				if math.fabs(oldTime - now) > MAXTIMEDELETE:
					cursor = conn.cursor()
					cursor.execute(
						'DELETE from TOKEN WHERE token=?',
						(r[0],)
					)
					conn.commit()

		except Exception as err:
			raise
			print('Ошибка бд: deleteTime::', err)


DB = DBClass()
print(DB.deleteToken("654","Ррр"))



"""
cur.execute("SELECT Name, Price FROM Cars WHERE Id=:Id", 
        {"Id": uId}) 
"""

"""
	def updateTime_token(self,token:str,):
		now = time.time()
		try:
			conn = sqlite3.connect('database.db')
			cursor = conn.cursor()
			cursor.execute(
				'UPDATE TOKEN SET date=? WHERE token=? A ',
				(now, token))
			conn.commit()
		except Exception as err:
			print('Ошибка бд: check_para::', err)1
			
		def check_token(self,token:str):
		result = False
		try:
			conn = sqlite3.connect('database.db')
			cursor = conn.cursor()
			cursor.execute(
				'SELECT * FROM TOKEN WHERE token=?  ' ,
				(token,))
			res = cursor.fetchall()
			if not res==[]:
				result = True
		except Exception as err:
			print('Ошибка бд: check_para::', err)
		return result		
			
	
		def tokenInsert(self,token):
		try:
			now = time.time()
			conn = sqlite3.connect('database.db')
			cursor = conn.cursor()
			cursor.execute(
				f'INSERT INTO tokens ({token},) VALUES(?, ? ,?,?) ',
				)
			conn.commit()
			return True
		except Exception as err:

			print('Ошибка бд: insert token:', err)
			return False

	
		def tokenUpdate(self,table, token, last):
		try:
			conn = sqlite3.connect('database.db')
			cursor = conn.cursor()
			cursor.execute(
				'UPDATE '+table+' SET last=?, date=?,dateStr=?  WHERE token=? ',
				(last,time.time(),time.ctime(),token,))
			conn.commit()
		except Exception as err:
			raise
			print('Ошибка бд: update_token::', err)

	def tokenAdd(self, table, token, price):
		if self.tokenCheck(table,token):
			self.tokenUpdate(table,token,price)
		else:
			self.tokenInsert(table,token,price)
	
		def deleteOldTime(self):
		print('')
		try:
			conn = sqlite3.connect('database.db')
			cursor = conn.cursor()
			cursor.execute(
				'SELECT * FROM pair ' ,

			)

			res = cursor.fetchall()
			for r in res:
				now = time.time()
				oldTime = float(r[5])
				if math.fabs(oldTime - now) > MAXTIMEDELETE:
					cursor = conn.cursor()
					cursor.execute(
						'DELETE from pair WHERE (market=? AND pair=?)',
						(r[0],r[1])
					)
					conn.commit()

		except Exception as err:
			raise
			print('Ошибка бд: deleteTime::', err)

	def deleteOldTime_token(self):
		print('')
		try:
			conn = sqlite3.connect('database.db')
			cursor = conn.cursor()
			cursor.execute(
				'SELECT * FROM TOKEN' ,

			)

			res = cursor.fetchall()
			for r in res:
				now = time.time()
				oldTime = float(r[1])
				if math.fabs(oldTime - now) > MAXTIMEDELETE:
					cursor = conn.cursor()
					cursor.execute(
						'DELETE from TOKEN WHERE token=?',
						(r[0],)
					)
					conn.commit()

		except Exception as err:
			raise
			print('Ошибка бд: deleteTime::', err)
	
"""