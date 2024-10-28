from loader import dp
from aiogram import types
from keyboards.inline.donars_buttons import *
from keyboards.inline.savat_button_for_donar import *
from keyboards.inline.category_buttons import *
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db_file import *
from states.oqtepa_states import OqtepaState


@dp.callback_query_handler(text="donarlar_call")
async def donarlar_func(call: types.CallbackQuery):
    await call.message.delete() 
    await call.message.answer_photo(open("images/donarlar.jpg", "rb"),caption="🥙 Donarlar",reply_markup=donarlar)

@dp.callback_query_handler(text="haggi_call")
async def haggi_func(call: types.CallbackQuery):
    await call.message.delete() 
    await call.message.answer_photo(open("images/xaggi.jpg", "rb"),caption="""
Xaggi
Narxi:   36 000 so'm
Tavsif: Yumshoq "Baget" noni, mol go'shti, mayonez, bodring, pomidor, pishloq, qizil sous va Brunsvik shirin piyoz halqalari
Miqdorini tanlang yoki kiriting""",reply_markup=savat_donar)

@dp.callback_query_handler(text="big_donner_call")
async def big_donner_func(call: types.CallbackQuery):
    await call.message.delete() 
    await call.message.answer_photo(open("images/big_doner.jpg", "rb"),caption="""
Big Doner
Narxi:   35 000 so'm
Tavsif: Yumshoq donar noni, donar go'shti, chips, bodiring, pomidor, sarimsoqli sous, "Oqtepa" tomat sousi.                                                                                                
Miqdorini tanlang yoki kiriting""",reply_markup=savat_donar)

@dp.callback_query_handler(text="shaurma_call")
async def shaurma_func(call: types.CallbackQuery):
    await call.message.delete() 
    await call.message.answer_photo(open("images/shaurma.jpg", "rb"),caption="""
Shaurma
Narxi:   26 000 so'm
Tavsif: Tandir noni «Pita», barra mol go'shti, bodring, pomidor, qizil sous, Brunsvik shirin piyoz halqalari
Miqdorini tanlang yoki kiriting
""",
reply_markup=savat_donar)

@dp.callback_query_handler(text="pita_donner_call")
async def pita_donner_func(call: types.CallbackQuery):
    await call.message.delete() 
    await call.message.answer_photo(open("images/pita_doner.jpg", "rb"),caption="""
Pita doner
Narxi:   30 000 so'm
Tavsif: Mazali go'sht, pomidorlar, piyoz va qizil "Oqtepa" sousi bilan to'ldirilgan pita xamiri. 
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_donar)



@dp.callback_query_handler(text="orqaga3_savat_call")
async def orqaga3_savat_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/donarlar.jpg", "rb"),caption="🥙 Donarlar",reply_markup=donarlar)
