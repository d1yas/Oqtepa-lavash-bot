from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards.inline.pitsa import *
from keyboards.inline.savat_button_for_pizza import *
from keyboards.inline.category_buttons import *
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db_file import *
from states.oqtepa_states import OqtepaState



@dp.callback_query_handler(text="pizza_call")
async def pizza_func(call: types.CallbackQuery):
    await call.message.answer_photo(open("images/pizza.jpg", "rb"),caption="🍕 Katta pitsalar",reply_markup=pitsa_buttons)


@dp.callback_query_handler(text="assorti_35sm_call")
async def assorti_35sm_func(call: types.CallbackQuery):
    await call.message.answer_photo(open("images/assorti_35sm.jpg", "rb"),caption="""
Assorti pitsa
Narxi:   105 000 so'm
Tavsif: "Achchiq pepperoni, oq sous, zaytun, shampinyon, bulg'or qalampir, pomidor, dudlangan kurka, dudlangan kolbasa, mol go'shti, sosiska, Mozzarella va Akbel pishlog'i qo'shilgan eng mashhur pitsa"
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_pizza)
    
@dp.callback_query_handler(text="pepperoni_35sm_call")
async def pepperoni_35sm_func(call: types.CallbackQuery):
    await call.message.answer_photo(open("images/pepperoni_35sm.jpg", "rb"),caption="""
Pepperoni pitsa
Narxi:   90 000 so'm
Tavsif: Amerika klassikasi pepperoni, maxsus tomat sousi Mozzarella va Akbel pishloqi.
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_pizza)
    

@dp.callback_query_handler(text="goshtli_35sm_call")
async def goshtli_35sm_func(call: types.CallbackQuery):
    await call.message.answer_photo(open("images/goshtli_35sm.jpg", "rb"),caption="""
Go'shtli pitsa
Narxi:   115 000 so'm
Tavsif: Sergosht pitsa. Maxsus tomat sousi, tovuq go'shti, bulg'or qalampiri, mol go'shti, pomidor, Mozzarella va Akbel pishloqi.
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_pizza)
    
@dp.callback_query_handler(text="qizil_35sm_call")
async def qizil_45sm_func(call: types.CallbackQuery):
    await call.message.answer_photo(open("images/qizil_45sm.jpg", "rb"),caption="""
Qazili pitsa
Narxi:   120 000 so'm
Tavsif: Qazi bo'lakchalari, maxsus tomat sousi, Brunsvik shirin piyoz halqalari, Mozzarella va Akbel pishloqi.
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_pizza)
    

@dp.callback_query_handler(text="tovuqli_35sm_call")
async def tovuqli_35sm_func(call: types.CallbackQuery):
    await call.message.answer_photo(open("images/tovuqli_35sm.jpg", "rb"),caption="""
Tovuqli pitsa
Narxi:   95 000 so'm
Tavsif: Yumshoq tovuq, maxsus tomat sousi, kurka go'shti, qo'ziqorin, zaytun, pishloq va oregano
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_pizza)
    
@dp.callback_query_handler(text="orqaga_call")
async def orqaga_func(call: types.CallbackQuery):
    await call.message.answer_photo(open("images/pizza.jpg", "rb"),caption="",reply_markup=category_buttons)


@dp.callback_query_handler(text="orqaga6_savat_call")
async def orqaga6_savat_func(call: types.CallbackQuery):
    await call.message.answer_photo(open("images/pizza.jpg", "rb"),caption="",reply_markup=pitsa_buttons)