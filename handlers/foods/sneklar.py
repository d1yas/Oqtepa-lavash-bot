from loader import dp
from aiogram import types
from keyboards.inline.sneklar_buttons import *
from keyboards.inline.savat_bitton_for_sneklar import *
from keyboards.inline.category_buttons import *
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db_file import *
from states.oqtepa_states import OqtepaState


@dp.callback_query_handler(text="sneklar_menu_call")
async def sneklar_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/sneklar.jpg", "rb"),caption="🍟 Sneklar",reply_markup=snek)

@dp.callback_query_handler(text="kartoshka_fri_orta_call")
async def kartoshka_fri_orta_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/fri_orta.jpg", "rb"),caption="""
Kartoshka fri o'rta
Narxi:   16 000 so'm
Tavsif: O'simlik yog'ida qovurilgan va ozgina tuzlangan kartoshka tayoqchalari
Miqdorini tanlang yoki kiriting""",reply_markup=savat_sneklar)

@dp.callback_query_handler(text="kartoshka_fri_katta_call")
async def kartoshka_fri_katta_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/fri_katta.jpg", "rb"),caption="""
Kartoshka fri katta
Narxi:   22 000 so'm
Tavsif: O'simlik yog'ida qovurilgan va ozgina tuzlangan kartoshka tayoqchalari
Miqdorini tanlang yoki kiriting""",reply_markup=savat_sneklar)

@dp.callback_query_handler(text="joja_boks_call")
async def joja_boks_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/joja_box.jpg", "rb"),caption="""
jo'ja box
Narxi:   35 000 so'm
Tavsif: To'yimli jo'ja boks! Mayin stripslar - 3 dona va o'rtacha kartoshka fri!
Miqdorini tanlang yoki kiriting""",reply_markup=savat_sneklar)

@dp.callback_query_handler(text="strips_5_dona_call")
async def strips_5_dona_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/strips_5.jpg", "rb"),caption="""
Strips 5 dona
Narxi:   33 000 so'm
Tavsif: Qarsildoq, mazali va mayin jo'jalar. Xech qanday suyaklarsiz faqat eng yumshoq tovuq filesi!
Miqdorini tanlang yoki kiriting""",reply_markup=savat_sneklar)

@dp.callback_query_handler(text="strips_3_dona_call")
async def strips_3_dona_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/strips_3.jpg", "rb"),caption="""
Strips 3 dona
Narxi:   21 000 so'm
Tavsif: Qarsildoq, mazali va mayin jo'jalar. Xech qanday suyaklarsiz faqat eng yumshoq tovuq filesi!
Miqdorini tanlang yoki kiriting""",reply_markup=savat_sneklar)

@dp.callback_query_handler(text="kartoshka_fri_kichik_call")
async def kartoshka_fri_kichik_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/fri_kichik.jpg", "rb"),caption="""
Kartoshka fri kichik
Narxi:   10 000 so'm
Tavsif: Osimlik yog'ida qovurilgan va ozgina tuzlangan kartoshka tayoqchalari
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_sneklar)

@dp.callback_query_handler(text="baytslar_call")
async def baytslar_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/baytslar.jpg", "rb"),caption="""
Baytslar
Narxi:   23 000 so'm
Tavsif: Qarsildoq jo'ja baytslari - mazali, mayin va ozgina achchiqli
Miqdorini tanlang yoki kiriting""",reply_markup=savat_sneklar)
    
@dp.callback_query_handler(text="jaydari_kartoshka_call")
async def jaydari_kartoshka_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/jaydari_kartoshka.jpg", "rb"),caption="""
Jaydari kartoshka
Narxi:   18 000 so'm
Tavsif: Osimlik yog'ida ziravorlar bilan qovurilgan kartoshka bo'laklari 
Miqdorini tanlang yoki kiriting""",reply_markup=savat_sneklar)

@dp.callback_query_handler(text="non_call")
async def non_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/non.jpg", "rb"),caption="""
Non
Narxi:   4 000 so'm
Tavsif: Yumshoq non
Miqdorini tanlang yoki kiriting""",reply_markup=savat_sneklar)

@dp.callback_query_handler(text="nagetlar_5_call")
async def nagetlar_5_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/naggets5.jpg", "rb"),caption="""
Naggets 5 dona
Narxi:   16 000 so'm
Tavsif: Panirovkalangan yog'da qovurilgan tovuq filesining qarsildoq bo'laklari
Miqdorini tanlang yoki kiriting""",reply_markup=savat_sneklar)

@dp.callback_query_handler(text="nagetslar_boks_call")
async def nagetslar_boks_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/naggets_box.jpg", "rb"),caption="""
Naggets boks
Narxi:   37 000 so'm
Tavsif: Panirovkalangan qovurilgan tovuq filesining qarsildoq bo'laklari, fri kartoshkasi va ketchup bilan bir to'plamda
Miqdorini tanlang yoki kiriting""",reply_markup=savat_sneklar)


@dp.callback_query_handler(text="nagetlar_8_call")
async def nagetlar_8_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/naggets8.jpg", "rb"),caption="""
Naggetslar 8 dona 
Narxi:   22 000 so'm
Tavsif: Panirovkalangan yog'da qovurilgan tovuq filesining qarsildoq bo'laklari
Miqdorini tanlang yoki kiriting""",reply_markup=savat_sneklar)

@dp.callback_query_handler(text="nagetlar_15_call")
async def nagetlar_15_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/naggets15.jpg", "rb"),caption="""
Naggets 15 dona 
Narxi:   39 000 so'm
Tavsif: Panirovkalangan yog'da qovurilgan tovuq filesining qarsildoq bo'laklari
Miqdorini tanlang yoki kiriting""",reply_markup=savat_sneklar)
    
@dp.callback_query_handler(text="orqaga5_savat_call")
async def orqaga5_savat_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/sneklar.jpg", "rb"),caption="🍟 Sneklar",reply_markup=snek)



