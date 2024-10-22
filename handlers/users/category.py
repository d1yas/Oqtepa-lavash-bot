from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.default_buttons import for_start
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards.default.default_buttons import shaharlar, borib_buyurtma, borib_buyurtma_ortga, send_nomer
from keyboards.inline.inline_buttons import menu, sozlamalar_buttons, soz_shahar_buttons
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.category_buttons import *
from db_file import *
from states.oqtepa_states import OqtepaState

@dp.message_handler(content_types=types.ContentType.LOCATION)
async def location_handler(message: types.Message):
    await message.answer("Manzil qabul qilindi")
    await message.answer("Kategoriyalardan birini tanlang. (https://telegra.ph/Taomnoma-09-30)", reply_markup=category_buttons)