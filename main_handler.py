from datetime import datetime


from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from asyncio import sleep


from keyboards import inline, default
from misc import dp, bot, only_numerics
import fakedraw

class Settings(StatesGroup):
    qiwi = State()
    sber = State()
    yandex = State()
    qiwi_balance = State()
    qiwi_transfer = State()
    sber_balance = State()
    yandex_money_balance = State()

@dp.message_handler(lambda message: message.text == "Главное меню", content_types=types.ContentTypes.TEXT, state="*")
async def main(message: types.Message, state: FSMContext):
    await message.answer("<b>Главное меню</b>", reply_markup=default.Start())
    await state.finish()


@dp.message_handler(lambda message: message.text == "QIWI", content_types=types.ContentTypes.TEXT, state="*")
async def qiwi(message: types.Message, state: FSMContext):
    await message.answer("<b>Выберите действие с помощью клавиатуры</b>", reply_markup=default.Qiwi())
    await Settings.qiwi.set()


@dp.message_handler(lambda message: message.text == "Баланс", content_types=types.ContentTypes.TEXT, state=Settings.qiwi)
async def qiwi(message: types.Message, state: FSMContext):
    await message.answer_photo(fakedraw.fake_qiwi_balance(message), caption="""<b>
Введите необходимые данные:
1️⃣ - баланс

Пример:
500
</b>""")
    await Settings.qiwi_balance.set()



@dp.message_handler(content_types=types.ContentTypes.TEXT, state=Settings.qiwi_balance)
async def qiwi(message: types.Message, state: FSMContext):
    await message.answer_photo(fakedraw.fake_qiwi_balance(message), reply_markup=inline.Exit())
    await Settings.qiwi.set()



@dp.message_handler(lambda message: message.text == "Перевод на другой кошелек", content_types=types.ContentTypes.TEXT, state=Settings.qiwi)
async def qiwi(message: types.Message, state: FSMContext):
    await message.answer_photo(fakedraw.fake_qiwi_transfer(message), caption="""<b>
Введите необходимые данные:

1️⃣ - сумма перевода
2️⃣ - номер перевода
3️⃣ - дату и время

Пример:
432
+78954328507
08.03.2021 в 21:30
</b>""")
    await Settings.qiwi_transfer.set()


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=Settings.qiwi_transfer)
async def qiwi(message: types.Message, state: FSMContext):
    await message.answer_photo(fakedraw.fake_qiwi_transfer(message), reply_markup=inline.Exit())
    await Settings.qiwi.set()

@dp.message_handler(lambda message: message.text == "Сбер", content_types=types.ContentTypes.TEXT, state="*")
async def sber(message: types.Message, state: FSMContext):
    await message.answer("<b>Выберите действие с помощью клавиатуры</b>", reply_markup=default.Sber())
    await Settings.sber.set()

@dp.message_handler(lambda message: message.text == "Баланс", content_types=types.ContentTypes.TEXT, state=Settings.sber)
async def qiwi(message: types.Message, state: FSMContext):
    await message.answer_photo(fakedraw.fake_sber_balance(message), caption="""<b>
Введи необходимые данные:

1️⃣ - системное время
2️⃣ - баланс
3️⃣ - последние 4 цифры карты

Пример:
14:37
25000
5324
</b>""")
    await Settings.sber_balance.set()


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=Settings.sber_balance)
async def qiwi(message: types.Message, state: FSMContext):
    await message.answer_photo(fakedraw.fake_sber_balance(message), reply_markup=inline.Exit())
    await Settings.sber.set()


@dp.message_handler(lambda message: message.text == "ЮMoney", content_types=types.ContentTypes.TEXT, state="*")
async def yandex_money(message: types.Message, state: FSMContext):
    await message.answer("<b>Выберите действие с помощью клавиатуры</b>", reply_markup=default.Yandex())
    await Settings.yandex.set()


@dp.message_handler(lambda message: message.text == "Баланс", content_types=types.ContentTypes.TEXT, state=Settings.yandex)
async def qiwi(message: types.Message, state: FSMContext):
    await message.answer_photo(fakedraw.fake_yandex_balance(message), caption="""<b>
Введи необходимые данные:

1️⃣ - системное время
2️⃣ - Имя пользователя
3️⃣ - Баланс

Пример:
23:19
shpex
50 000,51
</b>""")
    await Settings.yandex_money_balance.set()


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=Settings.yandex_money_balance)
async def qiwi(message: types.Message, state: FSMContext):
    await message.answer_photo(fakedraw.fake_yandex_balance(message), reply_markup=inline.Exit())
    await Settings.yandex.set()


@dp.message_handler(lambda message: message.text == "📈 Информация", content_types=types.ContentTypes.TEXT, state="*")
async def info(message: types.Message, state: FSMContext):
    await message.answer(f"<b>По вопросам - <em>@teDDy_pereXod | Донат - https://my.qiwi.com/OLGA-SoguLcdPcU</em></b>")

