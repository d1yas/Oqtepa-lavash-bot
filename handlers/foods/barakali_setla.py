from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards.inline.barakalli_setlar_buttons import *
from keyboards.inline.savat_button_for_baraka import savat_baraka
from keyboards.inline.category_buttons import category_buttons
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db_file import *
from states.oqtepa_states import OqtepaState

# Handler for displaying the Barakali setlar menu with an image

@dp.callback_query_handler(text="barakali_setlar_call")
async def barakali_setlar1_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/baytslar.jpg", "rb"),caption="🍱 Barakali setlar",reply_markup=barakali_setlar_buttons)

@dp.callback_query_handler(text="tandir_lavash_set_call")
async def tandie_lavash_seti_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/tandir_lavash.jpg", "rb"),caption="""
Tandir lavash seti
Narxi:   55 000 so'm
Tavsif: Tandir lavash, kichik fri, 2 dona naggets, ketchup, pepsi 0.3L
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_baraka)

@dp.callback_query_handler(text="orqaga_call")
async def orqaga_barakali_setlar_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/barakali_setlar.jpg", "rb"),caption="🍱 Barakali setlar",reply_markup=category_buttons)

@dp.callback_query_handler(text="lavash_seti_call")
async def lavash_seti_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/lavash_set.jpg", "rb"),caption="""
Lavash seti
Narxi:   50 000 so'm
Tavsif: Katta original Pita noni, kichik fri, naggetslar 2 dona, ketchup, Pepsi 0,3l
Miqdorini tanlang yoki kiriting
                                    """,reply_markup=savat_baraka)
    

@dp.callback_query_handler(text="pita_doner_seti_call")
async def pita_doner_seti_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/pita_doner_set.jpg", "rb"),caption="""
Pita doner seti
Narxi:   50 000 so'm
Tavsif: Katta original Pita noni, kichik fri, naggetslar 2 dona, ketchup, Pepsi 0,3l
Miqdorini tanlang yoki kiriting
                                    """,reply_markup=savat_baraka)
    

@dp.callback_query_handler(text="gamburger_seti_call")
async def gamburger_seti_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/gamburger_seti.jpg", "rb"),caption="""
Gamburger seti
Narxi:   40 000 so'm
Tavsif: "Gamburger, kichkina fri, naggetslar 2 dona, ketchup, Pepsi 0,3 L, "
Miqdorini tanlang yoki kiriting
                                    """,reply_markup=savat_baraka)
    

@dp.callback_query_handler(text="shohona_hot_dog_seti_call")
async def shohona_hot_dog_seti_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/shohona_hot_dog_seti.jpg", "rb"),caption="""
Shohona hot-dog seti
Narxi:   35 000 so'm
Tavsif: "Shohona xot dog, kichkina fri, naggetslar 2 dona, ketchup, Pepsi 0,3 L, "
Miqdorini tanlang yoki kiriting
                                    """,reply_markup=savat_baraka)
    
@dp.callback_query_handler(text="_call")
async def hod_dog_seti_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/hod_dog_seti.jpg", "rb"),caption="""
Hot-dog seti
Narxi:   30 000 so'm
Tavsif: "Xot dog, kichkina fri, naggetslar 2 dona, ketchup, Pepsi 0,3L, "
Miqdorini tanlang yoki kiriting
                                    """,reply_markup=savat_baraka)
    

@dp.callback_query_handler(text="tandir_lavash_juftligi_call")
async def tandir_lavash_juftligi_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/tandir_lavash_juftligi.jpg", "rb"),caption="""
Tandir lavash juftligi
Narxi:   95 000 so'm
Tavsif: 2 dona tandir lavash, 2 dona kichik fri, 2 dona ketchup, 2 dona pepsi 0.3L iborat bo'lgan ikki kishilik to'plam
Miqdorini tanlang yoki kiriting
                                    """,reply_markup=savat_baraka)
    

@dp.callback_query_handler(text="lavash_juftligi_call")
async def lavash_juftligi_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/lavash_juftligi.jpg", "rb"),caption="""
Lavashlar juftligi
Narxi:   90 000 so'm
Tavsif: Ikki kishilik to'plam: ikkita katta original katta lavash, ikkita ketchup, ikkita kichik fri, ikkita Pepsi 0,3 l
Miqdorini tanlang yoki kiriting
                                    """,reply_markup=savat_baraka)
    

@dp.callback_query_handler(text="shaurma_juftligi_call")
async def barakali_setlar_back_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/shaurma_juftlik.jpg", "rb"),caption="""
Shaurma juftligi
Narxi:   85 000 so'm
Tavsif: 2 dona shaurma,2 dona ketchup, 2 dona kichik fri, limonad kivi va qulupnaylik limonadlardan iborat bo'lgan ikki kishilik to'plam 
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_baraka)
    

@dp.callback_query_handler(text="juftlik_seti_call")
async def juftlik_seti_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/juftlik_seti.jpg", "rb"),caption="""
Juftlik seti 
Narxi:   75 000 so'm
Tavsif: "Klab sendvich, stripslar 3 dona, ketchup 2 dona, qulupnayli va kivili limonadlardan, iborat ikki kishilik to'plam."
Miqdorini tanlang yoki kiriting
                                    """,reply_markup=savat_baraka)
    
@dp.callback_query_handler(text="lavashdan_baraka_call")
async def lavashdan_baraka_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/lavashdan_baraka.jpg", "rb"),caption="""
Lavashdan baraka
Narxi:   55 000 so'm
Tavsif: Kichik lavash, kichik fri, 2 dona naggets, 2 dona ketchup, Pepsi 0,3L
Miqdorini tanlang yoki kiriting
                                    """,reply_markup=savat_baraka)
    
@dp.callback_query_handler(text="chizda_baraka_call")
async def chizda_baraka_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/chizdan_baraka.jpg", "rb"),caption="""
Chiz-da Baraka
Narxi:   165 000 so'm
Tavsif: Katta jamoa uchun set: 4-chizburger, 4-kichik fri, 4-Pepsi 0,3l
Miqdorini tanlang yoki kiriting
                                    """,reply_markup=savat_baraka)
    
@dp.callback_query_handler(text="shaurmadan_baraka_call")
async def lavashda_baraka_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/shaurmadan_baraka.jpg", "rb"),caption="""
Lavashda baraka
Narxi:   175 000 so'm
Tavsif: Katta jamoa uchun set: 4-katta original lavash, 4-kichik fri, 4-Pepsi 0,3l
Miqdorini tanlang yoki kiriting
                                    """,reply_markup=savat_baraka)
    
@dp.callback_query_handler(text="orqaga_call")
async def orqaga_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/barakali_setlar.jpg", "rb"),caption="🍱 Barakali setlar",reply_markup=category_buttons)
   
@dp.callback_query_handler(text="orqaga1_savat_call")
async def orqaga1_savat_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/barakali_setlar.jpg", "rb"),caption="🍱 Barakali setlar",reply_markup=barakali_setlar_buttons)