from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import aiogram.utils.markdown as fmt
import json
import pprint

import app.data
from app.data import text_start
from app.data import *

import random
import configparser
from configparser import ConfigParser

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, ParseMode


def getStruct():
    from app.data import struct_files
    js = json.loads(struct_files)
    return js

CHAT_ID = -1001761279032
LOGO_FILE_ID = 'AgACAgIAAxkBAAOAY11bBKpUPV5qfl46x52OdbFVMWIAAuLHMRuOS_FKip-nQjfj0NABAAMCAANzAAMqBA'

class OrderState(StatesGroup):
   pass
switch_back = types.InlineKeyboardMarkup()
switch_back.add(types.InlineKeyboardButton(
        text="🔙 Главное меню",
        callback_data='menuback'
    ))

def extract_time(json):
    try:
        # Also convert to int since update_time will be string.  When comparing
        # strings, "10" is smaller than "2".
        return str(json['name'])
    except KeyError:
        return 0

def create_keyboard(js:dict):
    switch_keyboard = types.InlineKeyboardMarkup()
    print(js)

    for file in js:

        if file['type'] == 'file':
            if file['data'] == '':
                continue
            file_text = file['name']
            if str(file_text).find('.') != -1:
                file_text = file_text[0:file_text.find('.')]
            switch_keyboard.add(types.InlineKeyboardButton(
                #text='читать: ' + file['name'],
                text=file_text,
                callback_data='f:' + file['name'],
                request_contact=True
            ))
    for dir in js:
        if dir['type'] == 'directory':
            if dir['children'] == []:
                continue
            switch_keyboard.add(types.InlineKeyboardButton(
                text=dir['name'],
                callback_data='d:' + dir['name'],
                request_contact=True
            ))
    #Назад
    switch_keyboard.add(types.InlineKeyboardButton(
        #text='⬅️Назад' ,
        text='🔙Назад' ,
        callback_data=':back',
        request_contact=True
    ))
    switch_keyboard.add(types.InlineKeyboardButton(
        text='📄Главное меню' ,
        callback_data=':main' ,
        request_contact=True
    ))
    return switch_keyboard

async def main(cb: types.CallbackQuery,state: FSMContext):
    await  menu(cb.message,state)


async def menuBack(cb: types.CallbackQuery,state: FSMContext):
    try:
        post = cb.data
        print('post', post)
        dir  = await state.get_data('path')
        if 'path' in dir: dir = dir['path']
        if str(dir) == '{}': dir = ''

        #Назад только в Главное меню
        if len(dir.split('\\')) == 1:
            await menu(cb.message,state)
            return
        dir = str(dir).rsplit('\\',1)[0]
        await state.update_data({'path':dir})
        new = await state.get_data('path')

        await sendButton(cb, state, '')
        pass
    except Exception as err:
        await cb.message.answer('Произошла ошибка. Попробуйте с начала, нажмите -> /start')



async def start(message: types.Message, state: FSMContext):
    await message.answer(
        text=app.data.text_start,
         parse_mode='HTML')

    state.reset_data()
    from app.data import struct_files
    js = json.loads(struct_files)
    switch_keyboard :types.InlineKeyboardMarku
    switch_keyboard = create_keyboard(js)
    switch_keyboard.inline_keyboard.pop(-1)
    switch_keyboard.inline_keyboard.pop(-1)
    await message.answer(
        text='Меню:',
        reply_markup=switch_keyboard, parse_mode='HTML')


    #await menu(message,state)
    pass

async def menu(message: types.Message, state: FSMContext):
    try:
        await state.reset_data()
        from app.data import struct_files
        js = json.loads(struct_files)
        switch_keyboard :types.InlineKeyboardMarku
        switch_keyboard = create_keyboard(js)
        switch_keyboard.inline_keyboard.pop(-1)
        switch_keyboard.inline_keyboard.pop(-1)
        await message.edit_text(
            text='Меню:',
            reply_markup=switch_keyboard, parse_mode='HTML')
    except Exception as err:
        await message.answer('Произошла ошибка. Попробуйте с начала, нажмите -> /start')

async def getJsonInDir(state: FSMContext):
    dir = await getDir(state)
    #js = await getJsonInDir(state)
    js = getStruct()
    if dir == '':
        return js
    print(js)
    path = dir
    pathlist = path.split('\\')
    print(pathlist)
    chl = None
    temp = js
    for pth in pathlist:
        for tmp in temp:
            if tmp['name'] == pth:
                chl = tmp['children']
        temp = chl
        pass
    print(temp)
    return temp


async def fileSend(cb: types.CallbackQuery, state: FSMContext):
    fullDir = ''
    post = cb.data[cb.data.find(':') + 1:]
    state_data = await state.get_data('path')
    if 'path' in state_data: state_data = state_data['path']
    if str(state_data) == '{}': state_data = ''

    if state_data == '':
        fullDir = post
    if state_data != '':
        fullDir = state_data + '\\' + post
    temp = getStruct()
    jsDir = await getJsonInDir(state)
    print(jsDir)
    for tmp in jsDir:
        if tmp['name'] == post:
            #await cb.message.answer(text=tmp['data'])
            #await sendButton(cb, state, '')

            js = await getJsonInDir(state)
            print('js', js)
            print('keyBorad')

            switch_keyboard = types.InlineKeyboardMarkup()
            switch_keyboard.add(types.InlineKeyboardButton(
                # text='⬅️Назад' ,
                text='🔙Назад',
                callback_data=':back',
                request_contact=True
            ))
            switch_keyboard.add(types.InlineKeyboardButton(
                text='📄Главное меню',
                callback_data=':main',
                request_contact=True
            ))

            #reply_markup = create_keyboard((await getJsonInDir(state))[0]['children'])
            await cb.message.edit_text(text=tmp['data'], reply_markup=switch_keyboard, parse_mode='HTML')

    pass

async def getDir(state:FSMContext):
    state_data = await state.get_data('path')
    if 'path' in state_data: state_data = state_data['path']
    if str(state_data) == '{}': state_data = ''
    dir = state_data
    return dir

async def sendButton(cb: types.CallbackQuery,state: FSMContext, post:str):
    #post -> Это нажатая кнопка
    #dir -> Текущяя позиция в бд
    #dir = getDir(state)
    #temp = getStruct()

    # create_keyboard((await getJsonInDir(state))[0]['children'])
    jsDir = await getJsonInDir(state)
    switch_keyboard = types.InlineKeyboardMarkup()
    dir = ''
    if post != '':
        for tmp in jsDir:
            if tmp['name'] == post:
                switch_keyboard = create_keyboard(tmp['children'])
                dir = await getDir(state)
                dir = str(dir) +'\\' + post
                dir = dir.replace('\\' , ' ➡️ ')
                break
    if post == '':
        switch_keyboard = create_keyboard(jsDir[0]['children'])
        dir = await getDir(state)
    await cb.message.edit_text(text='Раздел: ' + dir, reply_markup=switch_keyboard, parse_mode='HTML')



async def nextDir(cb: types.CallbackQuery,state: FSMContext):
    try:
        fullDir = ''
        post = cb.data[cb.data.find(':')+1:]

        dir = await getDir(state)
        if dir == '':
            fullDir = post
        if dir != '':
            fullDir = dir + '\\' + post
        await sendButton(cb, state, post)
        await state.update_data({'path': fullDir})
    except Exception as err:
        await cb.message.answer('Произошла ошибка. Попробуйте с начала, нажмите -> /start')









async def deleteF():
    print('stop')
    text = fmt.text(
            fmt.text(fmt.hunderline("Яблоки"), ", вес 1 кг."),
            fmt.text("Старая цена:", fmt.hstrikethrough(50), "рублей"),
            fmt.text("Новая цена:", fmt.hbold(25), "рублей"),
            fmt.text(fmt.hspoiler('test')),
            sep="\n",
        )
    print(fmt.hspoiler('213'))
    oldText = f"""Разрабатываю ботов под заказ
🤖Разработка бот-визитка:
    📊Где есть основная информация вашей компании
    💲Цены
    📜Услуги
    ❗️Акции
    ☎️Контакты
    🗺Местоположение
    📲Кнопка отправить свой контакт.
Цена: от {fmt.hspoiler('3990')}руб.


🤖Разработка бота под ваш заказ:
    Примеры: Опросник, калькулятор цены, мини-игра.
Цена: от {fmt.hspoiler('15000')}руб.
    
    """
    await cb.message.answer(text=oldText, reply_markup=switch_back,parse_mode="HTML" )



def register_handlers_handler(dp: Dispatcher):
    pass
    dp.register_message_handler(start, commands="start", state='*')
    #dp.register_message_handler(start, commands="menu", state='*')

    dp.register_callback_query_handler(fileSend, lambda c: c.data.find('f:') != -1, state='*')
    dp.register_callback_query_handler(nextDir, lambda c: c.data.find('d:') != -1, state='*')
    dp.register_callback_query_handler(menuBack, lambda c: c.data.find(':back') != -1, state='*')
    dp.register_callback_query_handler(main, lambda c: c.data.find(':main') != -1, state='*')




