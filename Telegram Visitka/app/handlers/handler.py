from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import aiogram.utils.markdown as fmt
import random
import configparser
from configparser import ConfigParser

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, ParseMode


CHAT_ID = -1001761279032
LOGO_FILE_ID = 'AgACAgIAAxkBAAOAY11bBKpUPV5qfl46x52OdbFVMWIAAuLHMRuOS_FKip-nQjfj0NABAAMCAANzAAMqBA'

class OrderState(StatesGroup):
   pass
switch_back = types.InlineKeyboardMarkup()
switch_back.add(types.InlineKeyboardButton(
        text="🔙 Главное меню",
        callback_data='menuback'
    ))

async def menu(message: types.Message, state: FSMContext):
    await message.bot.send_photo(message.chat.id,LOGO_FILE_ID,reply_markup=types.ReplyKeyboardRemove())

    switch_keyboard = types.InlineKeyboardMarkup()
    switch_keyboard.add(types.InlineKeyboardButton(
        text="Прайс на мои услуги💲",
        callback_data='menu1',
        request_contact=True
    ))
    switch_keyboard.add(types.InlineKeyboardButton(
        text='Как выполняется заказ💰',
        callback_data='menu2'
    ))
    switch_keyboard.add(types.InlineKeyboardButton(
        text='Поддержка и обслуживание🛡',
        callback_data='menu3'
    ))
    switch_keyboard.add(types.InlineKeyboardButton(
        text='Пример договоров🧾',
        callback_data='menu4'
    ))

    switch_keyboard.add(types.InlineKeyboardButton(
        text='Местоположение📌',
        callback_data='menu7'
    ))

    switch_keyboard.add(types.InlineKeyboardButton(
            text='Контакты☎️',
            callback_data='menu5'
        ))

    switch_keyboard.add(types.InlineKeyboardButton(
            text='Заказать звонок☎️',
            callback_data='menu6'
        ))
    switch_keyboard.add(types.InlineKeyboardButton(
        text='Выкуп нерабочего оборудования💰',
        callback_data='111'
    ))
    await message.answer(
        text='<b>Наш канал: t.me/createbizbotchannel \nПодписывайтесь и следите за новостями. </b>',
        reply_markup=switch_keyboard, parse_mode='HTML')




async def menu1(cb: types.CallbackQuery,state: FSMContext):
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

async def menu2(cb: types.CallbackQuery,state: FSMContext):
    switch = types.InlineKeyboardMarkup()
    switch.add(types.InlineKeyboardButton(
        text="🔙 Главное меню",
        callback_data='menuback'
    ))

    switch.add(types.InlineKeyboardButton(
        text='Контакты☎️',
        callback_data='menu5'
    ))

    switch.add(types.InlineKeyboardButton(
        text='Заказать звонок☎️',
        callback_data='menu6'
    ))

    await cb.message.answer(text="""📋Этапы разработки проекта:
    
    ☑️Личное общение минут 20, за которое у меня появляется понимание, что вам необходимо, для увеличения клиентов с помощью бота.
    ☑️Составление техническое задание, согласование.
    ☑️Предоплата.
    ☑️Реализация программы, проверка и внесения правок.
    ☑️Внедрение бота на ваш аккаунт телеграмма и установка его на хостинг 24/7.
    ☑️Оплата сданного проекта.
    
 ⏳По времени:
    🤖Бот-визитка:
        Разработка до 5 рабочих дней. Без учёта правок и тестирования с вашей стороны
    🤖Разработка бота:
        От 5 рабочих дней, в зависимости от сложности, в тех задании будет уточнено время разработки.

📞Позвоните, а остальное – я сделаю сам!
    """, reply_markup=switch)

async def menu3(cb: types.CallbackQuery,state: FSMContext):
    await cb.message.answer(text=f"""Поддержка и обслуживание:
Ежемесячная оплата 500 руб. 
В оплату обслуживания входит:
    Аренда ежемесячного хостинга
    Поддержка работоспособности 99.9% upload бота
    Изменение текстовых данных в боте

    """, reply_markup=switch_back, parse_mode='HTML')


async def menu4(cb: types.CallbackQuery,state: FSMContext):
    #await cb.bot.send_message('Пример отправки документов, разных форматов')
    await cb.bot.send_document(chat_id=cb.message.chat.id,document='BQACAgIAAxkBAANhY11Rn4UGMVuoWUaNPS8XT71fU-8AAmMfAAKOS_FKoZU1NSlcKgABKgQ',caption = 'Здесь текст, дополнения к документу',reply_markup=types.ReplyKeyboardRemove())
    await cb.bot.send_document(chat_id=cb.message.chat.id,document='BQACAgIAAxkBAANjY11SC1egDmH6CGsJ-gMa4Llxq7gAAmgfAAKOS_FKelZcg3NAzcYqBA',caption = 'Здесь уже другой текст, для второго документа',reply_markup=switch_back)

"""{"message_id": 99, "from": {"id": 128719420, "is_bot": false, "first_name": "Сергей", "last_name": "Софт", "username": "ScrojeeMagdak", "language_code": "ru"}, "chat": {"id": 128719420, "first_name": "Сергей", "last_name": "Софт", "username": "ScrojeeMagdak", "type": "private"}, "date": 1667085435, "document": {"file_name": "Пример PDF.pdf", "mime_type": "application/pdf", "thumb": {"file_id": "AAMCAgADGQEAA2NjXVILV6AOYfoIawn6AxrguXGruAACaB8AAo5L8Up6VlyDc0DNxgEAB20AAyoE", "file_unique_id": "AQADaB8AAo5L8Upy", "file_size": 8851, "width": 226, "height": 320}, "file_id": "BQACAgIAAxkBAANjY11SC1egDmH6CGsJ-gMa4Llxq7gAAmgfAAKOS_FKelZcg3NAzcYqBA", "file_unique_id": "AgADaB8AAo5L8Uo", "file_size": 6870151}}"""




async def menu5(cb: types.CallbackQuery,state: FSMContext):
    switch_keyboard = types.InlineKeyboardMarkup()
    switch_keyboard.add(types.InlineKeyboardButton(
        text='Заказать звонок☎️',
        callback_data='menu6'
    ))
    switch_keyboard.add(types.InlineKeyboardButton(
        text="🔙 Главное меню",
        callback_data='menuback'
    ))

    await cb.message.answer(text="""Контакты:
<b>По всем интересующим вопросам, пишите и звоните по контактам указанным ниже:
Технический отдел:</b> 
☎️ 8-923-273-xxxx 
<b>Условия сотрудничества/Абонентское обслуживание:</b>
☎️ 8-960-766-xxxx
<b>Заявки на ремонт/Общие вопросы:</b>
☎️ 8-923-344-xxxx
    """, reply_markup=switch_keyboard,parse_mode='HTML')


async def menu6(cb: types.CallbackQuery,state: FSMContext):
    markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
    )
    await cb.message.answer(text="""Чтобы мы вам перезвонили, нажмите кнопку "Отправить свой контакт ☎️" под полем ввода""", reply_markup=markup_request)

    await cb.message.answer(text = 'Вернуться в меню:', reply_markup=switch_back)


async def menu7(cb: types.CallbackQuery,state: FSMContext):
    #markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    #    KeyboardButton('Яндекс карты', url='https://yandex.ru/maps/-/CCUBZYqg-C')
   # )

    switch_keyboard = types.InlineKeyboardMarkup()
    switch_keyboard.add(types.InlineKeyboardButton(
        text="Яндекс карты📌",
        url='https://yandex.ru/maps/-/CCUZ7RSBxA'
    ))
    switch_keyboard.add(types.InlineKeyboardButton(
        text="2gis📌",
        url='https://go.2gis.com/arbjfy'
    ))
    switch_keyboard.add(types.InlineKeyboardButton(
        text="Google map📌",
        url='https://g.page/moscowcityru?share'
    ))
    switch_keyboard.add(types.InlineKeyboardButton(
        text="🔙 Главное меню",
        callback_data='menuback'
    ))

    await cb.message.answer(text="""Адрес: г. Москва, Московский международный деловой центр Москва-Сити""", reply_markup=switch_keyboard)


async def menuback(cb: types.CallbackQuery,state: FSMContext):
    await menu(cb.message,state)

async def sendContact(message: types.Message, state: FSMContext):
    await message.send_copy(CHAT_ID)


async def loadPhoto(message: types.Message, state: FSMContext):
    print(message)
async def loadDoc(message: types.Message, state: FSMContext):
    print(message)


def register_handlers_handler(dp: Dispatcher):
    pass
    dp.register_message_handler(menu, commands="start", state='*')
    dp.register_message_handler(menu, commands="menu", state='*')
    dp.register_message_handler(sendContact,  state='*', content_types='contact')
    #dp.register_message_handler(loadPhoto,  state='*', content_types='document')
    dp.register_message_handler(loadPhoto,  state='*', content_types='photo')
    dp.register_message_handler(loadDoc,  state='*', content_types='file')
    #dp.register_message_handler(test,state='*')
    dp.register_callback_query_handler(menu1, lambda c: c.data.find('menu1') != -1, state='*')
    dp.register_callback_query_handler(menu2, lambda c: c.data.find('menu2') != -1, state='*')
    dp.register_callback_query_handler(menu3, lambda c: c.data.find('menu3') != -1, state='*')
    dp.register_callback_query_handler(menu4, lambda c: c.data.find('menu4') != -1, state='*')

    dp.register_callback_query_handler(menu5, lambda c: c.data.find('menu5') != -1, state='*')
    dp.register_callback_query_handler(menu6, lambda c: c.data.find('menu6') != -1, state='*')
    dp.register_callback_query_handler(menu7, lambda c: c.data.find('menu7') != -1, state='*')
    dp.register_callback_query_handler(menuback, lambda c: c.data.find('menuback') != -1, state='*')



