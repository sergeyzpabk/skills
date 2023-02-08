from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import  json
from  DataBase import DB

import random
import configparser
from configparser import ConfigParser
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


CHAT_ID = -1001615625178
LOGO_FILE_ID = 'AgACAgIAAxkBAAMDYkavG5dbcQOl_yB7XgG2POHnKdMAAv-6MRuCKTFKgtn4paWhLsgBAAMCAANzAAMjBA'

class OrderState(StatesGroup):
    waiting_tokenAdd = State()
    waiting_editTokenName = State()

switch_back = types.InlineKeyboardMarkup()
switch_back.add(types.InlineKeyboardButton(
        text="🔙 Главное меню",
        callback_data='menuback'
    ))

async def menu(message: types.Message, state: FSMContext):
    switch_keyboard = types.InlineKeyboardMarkup()
    #switch_keyboard.add(types.InlineKeyboardButton(
    #    text='Список токенов',
    #    callback_data='tokenList'
    #))
    switch_keyboard.add(types.InlineKeyboardButton(
            text='Добавить токен',
            callback_data='tokenAdd'
        ))
    switch_keyboard.add(types.InlineKeyboardButton(
            text='Изменить токен',
            callback_data='tokenEdit'
        ))



    await message.answer(
        text='Выберите пункт из меню',
        reply_markup=switch_keyboard, parse_mode='HTML')



async def addToken(cb: types.CallbackQuery,state: FSMContext):
    await cb.message.answer('Напишите название токена:')
    await OrderState.waiting_tokenAdd.set()


async def addToken_answer(message: types.Message, state: FSMContext):
    text = message.text
    print(text)
    if (len(text)<2) or (len(text)>10):
        await message.answer('Имя токена, либо длинное, либо короткое. Попробуйте ещё раз')
        return

    await  state.update_data({'token' : text})
    data = await state.get_data()
    print(data)
    id = DB.insert_Newtoken(text)

    if id == -1:
        message.answer('Ошибка добавления. Попробуйте ещё раз через главное меню')
        return 0

    btns = []

    keyword: types.InlineKeyboardMarkup
    keybord = getKeybord(id)
    keybord.add(
        types.InlineKeyboardButton(
            text='Удалить токен',
            callback_data=str(data)
        )
    )

    res = await message.answer(text = 'Token: ' + text, reply_markup = keybord)
    await  state.update_data({'message_id':res['message_id']})
    res = await state.get_data()
    print(res)



def getKeybord(id):
    res = DB.getTokenID(id)
    token = DB.getTokenName_ID(id)
    exchs = DB.get_exchs()
    switch_keyboard = types.InlineKeyboardMarkup()
    for i in range(0,len(exchs)):
        print(exchs[i])
        data = {'ban': {
            'exch': exchs[i],
            'id': id,
            'token':token
        }}
        #data = f'com=ban;id={id};token={name}'
        if (res[i] == 'True') or (str(res[i]) =='1'):
            b = 'Banned!!!'
        else:
            b = 'UnBanned'

        switch_keyboard.add(types.InlineKeyboardButton(
            text=exchs[i] + ':'+b,
            callback_data=json.dumps(data)
        ))
    return switch_keyboard




async def ban(cb: types.CallbackQuery,state: FSMContext):
    res = cb.data.replace("'",'"')
    res = json.loads(res)
    print(res)
    id = res['ban']['id']
    print('ID token:',id)
    exch = res['ban']['exch']
    DB.updateBan(id,exch)
    print(getKeybord(id))
    await  cb.message.edit_reply_markup(reply_markup=getKeybord(id))
   # res = await  cb.message.edit_text(cb.message.text,reply_markup=getKeybord(id))
    #res = await  cb.message.edit_text(cb.message.text,reply_markup=getKeybord(id))
    print(res)
    print(res)

async def test(cb: types.CallbackQuery,state: FSMContext):
    print(cb.data)



async def tokenList(cb: types.CallbackQuery,state: FSMContext):
    tokens = DB.getList_id_token()
    msg = 'Список всех токенов: \n'
    for token in tokens:
        msg = msg + token[1] + ', '
        if len(msg) > 4080:
            print('len msg:', len(msg))
            await  cb.message.answer(msg)
            msg = ''
    msg = msg[:-1]
    print('len msg:', len(msg))
    if len(msg) > 0:
        await  cb.message.answer(text=msg)
    pass

async def tokenEdit(cb: types.CallbackQuery,state: FSMContext):
    tokens = DB.getList_id_token()
    msg = 'Список всех токенов: \n'
    for token in tokens:
        msg = msg + token[1] + ', '
        if len(msg) > 4080:
            print('len msg:', len(msg))
            await  cb.message.answer(msg)
            msg = ''
    msg = msg[:-1]
    print('len msg:', len(msg))
    if len(msg) > 0:
        await  cb.message.answer(text=msg)
    pass
    await cb.message.answer('Напишите токен')
    await OrderState.waiting_editTokenName.set()
    pass

print(DB.getToken('ALGO'))

async def editToken_name_waiting(message: types.Message, state: FSMContext):
    tokens = {}
    token = message.text.upper()
    res = DB.getToken(message.text)
    if res == []:
        await message.answer('Данный токен не найден. Введите повторно \n Укажите токен для редактирования')
        return

    for r in res:
        msg = 'Token: '+ r[1] + '\nID:'+str(r[0])
        switch_keyboard = types.InlineKeyboardMarkup()
        print('Token: ', r[1])
        print('id: ', r[0])
        keybord = getKeybord(r[0])
        #print('keyBoard:', key)
        keybord.add(types.InlineKeyboardButton(
            text='Удалить',
            callback_data=f'tokenDel:{r[0]}_{r[1]}'
        ))
        await message.answer(text = msg, reply_markup= keybord)


async def delToken(cb: types.CallbackQuery,state: FSMContext):
    print('cd.data', cb.data)
    data = cb.data
    id = data[data.find(':')+1 : data.find('_')]
    token = data[data.find('_')+1 : ]
    print('id:', id)
    print('token:', token)
    DB.deleteToken(id,token)
    await cb.message.answer('Удалили токен: '+token+'\n'+'Id: '+id )









def register_handlers_handler(dp: Dispatcher):
    dp.register_message_handler(menu, commands="start", state='*')
    dp.register_message_handler(menu, commands="menu", state='*')

    dp.register_callback_query_handler(addToken, lambda c: c.data.find('tokenAdd') != -1, state='*')
    dp.register_callback_query_handler(tokenList, lambda c: c.data.find('tokenList') != -1, state='*')
    dp.register_callback_query_handler(tokenEdit, lambda c: c.data.find('tokenEdit') != -1, state='*')
    dp.register_callback_query_handler(delToken, lambda c: c.data.find('tokenDel') != -1, state='*')
    dp.register_callback_query_handler(ban, lambda c: c.data.find('ban') != -1, state='*')
    dp.register_message_handler(addToken_answer, state = OrderState.waiting_tokenAdd)
    dp.register_message_handler(editToken_name_waiting, state = OrderState.waiting_editTokenName)



