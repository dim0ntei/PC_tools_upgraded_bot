from aiogram.dispatcher.filters import Text
from data import keyboards
from aiogram import types
from loader import dp


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer(f"Привет {message.from_user.first_name}!\n\n"
                         f"Что бы вывести список всех функций нажми /help", reply_markup=keyboards.main_menu_keyboard_ru)

