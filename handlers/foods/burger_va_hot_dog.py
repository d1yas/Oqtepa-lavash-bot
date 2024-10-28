from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards.inline.burger_va_hot_doglar import *
from keyboards.inline.savat_buttons import *
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db_file import *
from states.oqtepa_states import OqtepaState


@dp.callback_query_handler(text="burger_hotdog_call")
async def burger_va_hot_doglar_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/burger_va_hot_doglar.jpg", "rb"),caption="🍔 Burger va Hot-doglar",reply_markup=burger_va_hot_doglar_buttons)

@dp.callback_query_handler(text="gamburger_call")
async def gamburger_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/gamburger.jpg", "rb"),caption="""
Hamburger
Narxi:   25 000 so'm
Tavsif: Yumshoq bulochka, maxsus sous, aysberg salati, tuzlangan bodring, barra mol go'shtidan kotlet, pomidor, pishloq, Brunsvik shirin piyoz halqalari
Miqdorini tanlang yoki kiriting
""",reply_markup=savat)
    
@dp.callback_query_handler(text="chizburger_call")
async def chizburger_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/chizburger.jpg", "rb"),caption="""
Chizburger
Narxi:   25 000 so'm
Tavsif: Yumshoq bulochka, maxsus sous, aysberg salati, tuzlangan bodring, barra mol go'shtidan kotlet, pomidor, pishloq, Brunsvik shirin piyoz halqalari
Miqdorini tanlang yoki kiriting
""",reply_markup=savat)
    
@dp.callback_query_handler(text="big_burger_call")
async def big_burger_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/big_burger.jpg", "rb"),caption="""
Big Burger
Narxi:   37 000 so'm
Tavsif: Yumshoq bulochka, maxsus sous, aysberg salati, tuzlangan bodring, 2ta barra mol go'shtidan kotlet, pomidor, pishloq, Brunsvik shirin piyoz halqalari
Miqdorini tanlang yoki kiriting
""",reply_markup=savat)
    
@dp.callback_query_handler(text="big_chizburger_call")
async def big_chizburger_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/big_chizburger.jpg", "rb"),caption="""
Big Chizburger
Narxi:   41 000 so'm
Tavsif: Yumshoq bulochka, maxsus sous, aysberg salati, pishloq, tuzlangan bodring, barra mol go'shtidan kotlet (2dona), pomidor, pishloq, Brunsvik shirin piyoz halqalari
Miqdorini tanlang yoki kiriting
""",reply_markup=savat)
    
@dp.callback_query_handler(text="hot_dog_call")
async def hot_dog_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/hot_dog.jpg", "rb"),caption="""
Hot-dog
Narxi:   14 000 so'm
Tavsif: Yumshoq bulochka, sosiska, bodring, pomidor, ketchup, mayonez, ikra
Miqdorini tanlang yoki kiriting
""",reply_markup=savat)
    
@dp.callback_query_handler(text="pishloqli_hot_dog_call")
async def pishloqli_hot_dog_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/pishloqli_hot_dog.jpg", "rb"),caption="""
Pishloqli Hot-dog
Narxi:   17 000 so'm
Tavsif: Yumshoq bulochka, sosiska, tuzlangan bodring, pomidor, aysberg salati va pishloq sousi
Miqdorini tanlang yoki kiriting
""",reply_markup=savat)
    
@dp.callback_query_handler(text="shohona_hot_dog_call")
async def shohona_hot_dog_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/shohona_hot_dog.jpg", "rb"),caption="""
Shoxona Hot-dog
Narxi:   25 000 so'm
Tavsif: Yumshoq bulochka, 2ta sosiska, tuzlangan bodring, pomidor, xalapenyo, pishloq sousi, pishloq va aysberg salati
Miqdorini tanlang yoki kiriting
""",reply_markup=savat)
    
@dp.callback_query_handler(text="orqaga_savat_call")
async def orqaga_savat_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/burger_va_hot_doglar.jpg", "rb"),caption="🍔 Burger va Hot-doglar",reply_markup=burger_va_hot_doglar_buttons)
    
@dp.callback_query_handler(text="orqaga_call")
async def orqaga_burger_hotdog_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(reply_markup=burger_va_hot_doglar_buttons)