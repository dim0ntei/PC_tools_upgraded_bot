from aiogram.dispatcher.filters import Text
from aiogram import types
from loader import dp
from data import keyboards


@dp.message_handler()
async def unknown_text(message: types.Message):
    await message.answer("Неизвестная команда. Пользуйтесь кнопками или обратитесь к справочнику /help",
                         reply_markup=keyboards.main_menu_keyboard_ru)
