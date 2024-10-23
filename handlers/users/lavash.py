from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards.inline.lavashlar import *
from keyboards.inline.savat_buttons import *
from keyboards.inline.category_buttons import *
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db_file import *
from states.oqtepa_states import OqtepaState


@dp.callback_query_handler(text="lavashlar_call")
async def lavashlar_func(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        open("images/lavashlar.jpg", "rb"), 
        caption="🌯 Lavashlar", 
        reply_markup=lavashlar_buttons
    )
    
@dp.callback_query_handler(text="orqaga_call")
async def orqaga_func(call: types.CallbackQuery):
    await call.message.answer("🍔 Buyurtma qilish", reply_markup=category_buttons)

    

@dp.callback_query_handler(text="original_katta_lavash")
async def original_katta_lavash_func(callback: types.CallbackQuery):
    await callback.message.answer_photo(open("images/original_katta_lavash.jpg", "rb"),caption="""
Original katta lavash
Narxi:   32 000 so'm
Tavsif: Lavash xamiri, "Oqtepa" tomat sousi, donar go‘shti, pomidor, chips, mayonez
Miqdorini tanlang yoki kiriting        
""", reply_markup=savat)

@dp.callback_query_handler(text="original_kichik_lavash")
async def original_kichik_lavash_func(callback: types.CallbackQuery):
    await callback.message.answer_photo(open("images/original_katta_lavash.jpg", "rb"),caption="""
Original kichik lavash
Narxi:   27 000 so'm
Tavsif: Kichik lavash xamiri, "Oqtepa" tomat sousi, donar go‘shti, pomidor, chips, mayonez
Miqdorini tanlang yoki kiriting                                
""", reply_markup=savat)
# fix

@dp.callback_query_handler(text="pishloqli_katta_lavash")
async def pishloqli_katta_lavash_func(callback: types.CallbackQuery):
    await callback.message.answer_photo(open("images/pishloqli_katta_lavash.jpg", "rb"),caption="""
Pishloqli katta lavash
Narxi:   35 000 so'm
Tavsif: Lavash xamiri, "Oqtepa" tomat sousi, donar go'shti, pomidor, chips, mayonez, pishloq
Miqdorini tanlang yoki kiriting    
""", reply_markup=savat)
    
@dp.callback_query_handler(text="pishloqli_kichik_lavash")
async def pishloqli_kichik_lavash_func(callback: types.CallbackQuery):
    await callback.message.answer_photo(open("images/pishloqli_kichik_lavash.jpg", "rb"),caption="""
Pishloqli kichik lavash
Narxi:   30 000 so'm
Tavsif: Kichik lavash xamiri, "Oqtepa" tomat sousi, donar go'shti, pomidor, chips, mayonez, pishloq
Miqdorini tanlang yoki kiriting
""", reply_markup=savat)

@dp.callback_query_handler(text="tandir_lavash")
async def tandir_lavash_func(call: types.CallbackQuery):
    await call.message.answer_photo(open("images/tandir_lavash.jpg", "rb"),caption="""
Tandir lavash
Narxi:   34 000 so'm
Tavsif: Lavash xamiri, "Oqtepa" tomat sousi, donar go‘shti, pomidor, chips, mayonez, sedana. Tandirda pishiriladi
Miqdorini tanlang yoki kiriting
""", reply_markup=savat)
    
@dp.callback_query_handler(text="pishloqli_tandir_lavash")
async def pishloqli_tandir_lavash_func(call: types.CallbackQuery):
    await call.message.answer_photo(open("images/pishloqli_tandir_lavash.jpg", "rb"),caption="""
Pishloqli tandir lavash
Narxi:   37 000 so'm
Tavsif: Lavash xamiri, "Oqtepa" tomat sousi, donar go‘shti, pomidor, chips, mayonez, pishloq, sedana. Tandirda pishiriladi
Miqdorini tanlang yoki kiriting
""", reply_markup=savat)
