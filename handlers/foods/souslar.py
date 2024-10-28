from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards.inline.souslar_buttons import *
from keyboards.inline.savat_button_for_sous import *
from keyboards.inline import category_buttons
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db_file import *
from states.oqtepa_states import OqtepaState


@dp.callback_query_handler(text="souslar_call")
async def souslar_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/souslar.jpg", "rb"),caption="🍅️️ Souslar",reply_markup=souslar_buttons)


@dp.callback_query_handler(text="orqaga_souslar_call")
async def orqaga_souslar_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/souslar.jpg", "rb"),caption="🍅️️ Souslar",reply_markup=category_buttons)

@dp.callback_query_handler(text="ketchup_call")
async def ketchup_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/ketchup.jpg", "rb"),caption="""
Ketchup
Narxi:   4 000 so'm
Tavsif: Tabiiy mahsulotlardan tayyorlangan Tanho ketchupi har qanday sneklaringizni (fri, baytslar va stripslar) bilan zo'r ketadi!
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_for_sous)
    
@dp.callback_query_handler(text="chili_souse_call")
async def chili_souse_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/chili_souse.jpg", "rb"),caption="""
Chili sous
Narxi:   4 000 so'm
Tavsif: Taomga ziravorlar qo'shadigan klassik Tailand sousi. 
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_for_sous)
    
@dp.callback_query_handler(text="pishloqli_souse_call")
async def pishloqli_souse_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/pishloqli_souse.jpg", "rb"),caption="""
Pishloqli sous
Narxi:   4 000 so'm
Tavsif: Pishloq sousi qarsildoq joja va jaydari kartoshka bilan ayni muddao
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_for_sous)
    
@dp.callback_query_handler(text="oq_souse_call")
async def oq_souse_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/oq_souse.jpg", "rb"),caption="""
Oq sous
Narxi:   4 000 so'm
Tavsif: Nozik sarimsoq ta'mli Oq sous. U har qanday sneklaringizni (fri, baytlar va chiziqlar) to'ldiradi
Miqdorini tanlang yoki kiriting
    """,reply_markup=savat_for_sous)
    
@dp.callback_query_handler(text="souslar_kvarteti_call")
async def souslar_kvarteti_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/souslar_kvarteti.jpg", "rb"),caption="""
Souslar kvarteti
Narxi:   12 000 so'm
Miqdorini tanlang yoki kiriting
    """,reply_markup=savat_for_sous)
    
@dp.callback_query_handler(text="souslar_dueti_call")
async def souslar_dueti_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/souslar_dueti.jpg", "rb"),caption="""
Souslar dueti
Narxi:   6 000 so'm
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_for_sous)
    
@dp.callback_query_handler(text="orqaga12_savat_call")
async def orqaga12_savat_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/souslar.jpg", "rb"),caption="🍅️️ Souslar",reply_markup=souslar_buttons)

@dp.callback_query_handler(text="orqaga_call ")
async def orqaga_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/souslar.jpg", "rb"),caption="🍅️️ Souslar",reply_markup=category_buttons)