from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards.inline.shirinliklar import *
from keyboards.inline.savat_for_shirinliklar import *
from keyboards.inline.category_buttons import *
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db_file import *
from states.oqtepa_states import OqtepaState

@dp.callback_query_handler(text="shirinliklar_call")
async def shirinliklar_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/shirinliklar.jpg", "rb"),caption="🍰 Shirinliklar", reply_markup=shirinliklar_buttons)

@dp.callback_query_handler(text="donat_yongoqli_call")
async def donat_yongoqli_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/donat_yongoqli.jpg", "rb"),caption="""
Donat yong'oqli
Narxi:   18 000 so'm
Tavsif: To'yimli yong'oqli donat -  o'rmon yong'oqlarining betakror ta'mi.
Miqdorini tanlang yoki kiriting
""", reply_markup=savat_for_shirinliklar)
    
@dp.callback_query_handler(text="donat_karamelli_call")
async def donat_karamelli_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/donat_karamelli.jpg", "rb"),caption="""
Donat  karamelli
Narxi:   18 000 so'm
Tavsif: Yumshoq karamelli donat - har bir bo'lagida lazzatli ta'm
Miqdorini tanlang yoki kiriting
""", reply_markup=savat_for_shirinliklar)
    
@dp.callback_query_handler(text="maffin_shokoladli_call")
async def maffin_shokoladli_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/maffin_shokoladli.jpg", "rb"),caption="""
Maffin shokoladli
Narxi:   18 000 so'm
Tavsif: Shokoladli nachinka bilan to'ldirilgan xushbo'y maffin
Miqdorini tanlang yoki kiriting
""", reply_markup=savat_for_shirinliklar)
    
@dp.callback_query_handler(text="maffin_karamelli_call")
async def donat_qulupnayli_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/donat_qulupnayli.jpg", "rb"),caption="""
Donat  qulupnayli
Narxi:   18 000 so'm
Tavsif: Qulupnayli donat - har bir bo'lagida reza mevalarning go'zalligi
Miqdorini tanlang yoki kiriting
""", reply_markup=savat_for_shirinliklar)
    
@dp.callback_query_handler(text="maffin_ormon_mevalari_call")
async def maffin_ormon_mevalari_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/maffin_ormon_mevali.jpg", "rb"),caption="""
Maffin o'rmon mevalari
Narxi:   18 000 so'm
Tavsif: Reza mevalar nachinkasi bilan to'ldirilgan mazali maffin
Miqdorini tanlang yoki kiriting
""", reply_markup=savat_for_shirinliklar)
    

@dp.callback_query_handler(text="klasssic_shok_pechanyasi_call")
async def klasssic_shok_pechanyasi_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/klasssic_shok_pechanasi.jpg", "rb"),caption="""
Klassik shokolad-parchalari pechenyesi
Narxi:   9 000 so'm
Tavsif: Klassik shokolad-parchalari pechenyesi
Miqdorini tanlang yoki kiritingy
""", reply_markup=savat_for_shirinliklar)
    
@dp.callback_query_handler(text="brauni_peshenyesi_call")
async def klasssic_karamelli_pechanyasi_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/brauni.jpg", "rb"),caption="""
Brauni peshenyesi
Narxi:   9 000 so'm
Tavsif: Brauni peshenyesi
Miqdorini tanlang yoki kiriting
""", reply_markup=savat_for_shirinliklar)
    
@dp.callback_query_handler(text="orqaga11_savat_call")
async def orqaga11_savat_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/shirinliklar.jpg", "rb"),caption="🍰 Shirinliklar",reply_markup=shirinliklar_buttons)


@dp.callback_query_handler(text="orqaga_call")
async def orqaga_func(call: types.CallbackQuery):
    await call.message.delete() 
    await call.message.answer_photo(open("images/shirinliklar.jpg", "rb"),caption="🍰 Shirinliklar",reply_markup=category_buttons)