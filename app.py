from aiogram.contrib.fsm_storage.memory import MemoryStorage
from PIL import Image, ImageGrab, ImageDraw
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher
from subprocess import Popen, PIPE
from pySmartDL import SmartDL
from aiogram import types
from data import keyboards
from data import config
import PIL.ImageGrab
import webbrowser
import platform
import requests
import shutil
import ctypes
import mouse
import time
import os

API_TOKEN = config.token
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


async def on_startup(dp):
    from utils.notify_admin import on_startup_notify
    await on_startup_notify(dp)


user_dict = {}


class User:
    def __init__(self):
        keys = ['urldown', 'fin', 'curs']

        for key in keys:
            self.key = None


User.curs = 50

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True)
