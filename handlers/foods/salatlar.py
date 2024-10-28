from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards.inline.salatlar_buttons import *
from keyboards.inline.savat_button_for_salat import savat_salat
from keyboards.inline.category_buttons import category_buttons
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db_file import *
from states.oqtepa_states import OqtepaState


@dp.callback_query_handler(text="salatlar_call")
async def salatlar_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/salatlar.jpg", "rb"),caption="🥗 Salatlar",reply_markup=salatlar_list)

@dp.callback_query_handler(text="mujskoy_kapriz_call")
async def mujskoy_kapriz_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/mujskoy_kapriz.jpg", "rb"),caption="""
Mujskoy Kapriz
Narxi:   31 000 so'm
Tavsif: Dudlangan kolbasa, kurka, qazi, pishloq, mayonez
Miqdorini tanlang yoki kiriting""",reply_markup=savat_salat)

@dp.callback_query_handler(text="sezar_call")
async def sezar_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/sezar.jpg", "rb"),caption="""
Sezar
Narxi:   26 000 so'm
Tavsif: Qarsildoq aysberg salati, cherry pomidorlari, parmezan pishloqi va yumshoq tovuq filesi
Miqdorini tanlang yoki kiriting""",reply_markup=savat_salat)
    

@dp.callback_query_handler(text="orqaga7_savat_call")
async def orqaga7_savat_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/salatlar.jpg", "rb"),caption="🥗 Salatlar",reply_markup=salatlar_list)


@dp.callback_query_handler(text="orqaga_call")
async def orqaga_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/salatlar.jpg", "rb"),caption="🥗 Salatlar",reply_markup=category_buttons)

