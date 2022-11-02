from aiogram.dispatcher.filters import Text
from aiogram import types
from loader import dp
from PIL import Image, ImageGrab, ImageDraw
import PIL.ImageGrab
from data import config
import mouse
import os


@dp.message_handler(Text(equals="Сделать скриншот", ignore_case=True))
async def create_screenshot(message: types.Message):
    try:
        currentMouseX, currentMouseY = mouse.get_position()
        img = PIL.ImageGrab.grab()
        img.save("screen.png", "png")
        img = Image.open("screen.png")
        draw = ImageDraw.Draw(img)
        draw.polygon(
            (currentMouseX, currentMouseY, currentMouseX, currentMouseY + 15, currentMouseX + 10, currentMouseY + 10),
            fill="white", outline="black")
        img.save("screen_with_mouse.png", "PNG")
        await message.answer_photo(open("screen_with_mouse.png", "rb"))
        os.remove("screen.png")
        os.remove("screen_with_mouse.png")
    except:
        await message.answer(config.admins_id, "Компьютер заблокирован")


