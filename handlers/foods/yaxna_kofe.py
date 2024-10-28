from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards.inline.yahna_kofe import yahna_kofe_buttons
from keyboards.inline.savat_button_for_kofe import savat_kofe
from keyboards.inline.category_buttons import category_buttons
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db_file import *
from states.oqtepa_states import OqtepaState

 
@dp.callback_query_handler(text="ice_cofe_call")
async def ice_cofe_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/ice_cofe.jpg", "rb"),caption="🧊 Yaxna cofe",reply_markup=yahna_kofe_buttons)

@dp.callback_query_handler(text="yahna_shok_kapuchino_call")
async def yahna_shok_kapuchino_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/yahna_shok_kapuchino.jpg", "rb"),caption="""
Yahna shokolad kapuchino
Narxi:   25 000 so'm
Tavsif: Yaxna shokolad kapuchino
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_kofe)
    
@dp.callback_query_handler(text="yahna_tuz_kapuchino_call")
async def yahna_tuz_kapuchino_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/yahna_tuz_kapuchino.jpg", "rb"),caption="""
Yaxna tuzli-karamel kapuchino
Narxi:   25 000 so'm
Tavsif: Yaxna tuzli-karamel kapuchino
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_kofe)
    
@dp.callback_query_handler(text="yahna_iris_tofi_kapuchino_call")
async def yahna_iris_tofi_kapuchino_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/yahna_iris_tofi_kapuchino.jpg", "rb"),caption="""
Yahna iris-tofi kapuchino
Narxi:   25 000 so'm
Tavsif: Yahna iris-tofi kapuchino
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_kofe)


@dp.callback_query_handler(text="yahna_shok_latte_call")
async def yahna_shok_latte_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/yahna_shok_latte.jpg", "rb"),caption="""
Yahna klassik kapuchino
Narxi:   23 000 so'm
Tavsif: Yahna klassik kapuchino
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_kofe)
    
@dp.callback_query_handler(text="orqaga_call")
async def orqaga_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/category.jpg", "rb"),caption="🧊 Yaxna cofe",reply_markup=category_buttons)

@dp.callback_query_handler(text="orqaga8_savat_call")
async def orqaga8_savat_func(call: types.CallbackQuery):
    await call.message.delete()
    try:
        await call.message.answer_photo(
            photo=open("images/yaxna_kofe.jpg", "rb"),
            caption="🧊 Yaxna cofe",
            reply_markup=yahna_kofe_buttons
        )
    except FileNotFoundError:
        await call.message.answer("Kechirasiz, rasm topilmadi. Kategoriyani tanlang:", reply_markup=yahna_kofe_buttons)