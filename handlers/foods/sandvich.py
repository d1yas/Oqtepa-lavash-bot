from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards.inline.sendvich import *
from keyboards.inline.savat_button_for_sendvich import *
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db_file import *
from states.oqtepa_states import OqtepaState

@dp.callback_query_handler(text="sandvichlar_call")
async def sandvich_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/sandvichlar.jpg", "rb"),caption="🥪 Sandvichlar",reply_markup=sendvich_buttons)


@dp.callback_query_handler(text="klab_sendvich_frisiz_call")
async def klab_sendvich_frisiz_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/klab_sendvich_frisiz.jpg", "rb"),caption="""
Klab-sendvich frisiz
Narxi:   32 000 so'm
Tavsif: Toster non, maxsus sous, bodring, pomidor, tovuq filesi, aysberg salati, pishloq. 
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_sendvich)
    
@dp.callback_query_handler(text="klab_sendvich_fri_bilan_call")
async def klab_sendvich_fri_bilan_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/klab_sendvich_fri_bilan.jpg", "rb"),caption="""
Klab sendvich fri bilan
Narxi:   36 000 so'm
Tavsif: Toster non, maxsus sous, bodring, pomidor, tovuq filesi, salat bargi, pishloq, kartoshka fri
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_sendvich)
    
@dp.callback_query_handler(text="orqaga4_savat_call")
async def orqaga_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/sandvichlar.jpg", "rb"),caption="🥪 Sandvichlar",reply_markup=sendvich_buttons)
