import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(token="5904496692:AAF002HcOuCw4CMmxt-6HKeJdtjVb2F07uo", parse_mode=types.ParseMode.HTML)
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)
logging.basicConfig(level=logging.INFO)

def only_numerics(p):
    seq_type= type(p)
    return seq_type().join(filter(seq_type.isdigit, p))
