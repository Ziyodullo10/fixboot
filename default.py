from aiogram import types

def Start():
    StartKeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    qiwi = types.KeyboardButton("QIWI")
    sber = types.KeyboardButton("Сбер")
    yandex = types.KeyboardButton("ЮMoney")
    info = types.KeyboardButton("📈 Информация")
    StartKeyboard.add(qiwi, sber, yandex)
    StartKeyboard.add(info)
    return StartKeyboard

def Qiwi():
    Qiwi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    balance = types.KeyboardButton("Баланс")
    transfer = types.KeyboardButton("Перевод на другой кошелек")
    back = types.KeyboardButton("Главное меню")
    Qiwi.add(balance)
    Qiwi.add(transfer)
    Qiwi.add(back)
    return Qiwi

def Sber():
    Sber = types.ReplyKeyboardMarkup(resize_keyboard=True)
    balance = types.KeyboardButton("Баланс")
    back = types.KeyboardButton("Главное меню")
    Sber.add(balance)
    Sber.add(back)
    return Sber

def Yandex():
    Yandex = types.ReplyKeyboardMarkup(resize_keyboard=True)
    balance = types.KeyboardButton("Баланс")
    back = types.KeyboardButton("Главное меню")
    Yandex.add(balance)
    Yandex.add(back)
    return Yandex