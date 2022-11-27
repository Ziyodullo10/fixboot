from datetime import datetime, timedelta


import aiogram
import pytz


def Exit():
    ExitKeyBoard = aiogram.types.InlineKeyboardMarkup(row_width=1)
    ExitKeyBoard_key = aiogram.types.InlineKeyboardButton('Закрыть', callback_data='del_message')
    ExitKeyBoard.add(ExitKeyBoard_key)
    return ExitKeyBoard
