from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.default_buttons import for_start
from loader import dp
from keyboards.default.default_buttons import shaharlar, borib_buyurtma, borib_buyurtma_ortga, send_nomer
from keyboards.inline.inline_buttons import menu, sozlamalar_buttons, soz_shahar_buttons
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db_file import *

@dp.message_handler(commands="start")
async def bot_start(message: types.Message):
    await message.answer(f"""
Assalomu alaykum {message.from_user.first_name}. Men Oqtepa Lavash yetkazib berish xizmati botiman!
Привет {message.from_user.first_name}! Я бот службы доставки Oqtepa Lavash!
Hi {message.from_user.first_name}! I am Oqtepa Lavash delivery service bot
""", reply_markup=for_start)
    await message.answer("""
Muloqot tilini tanlang
Выберите язык
Select Language
""")



@dp.message_handler(text="🇺🇿 O'zbekcha")
async def uzbek(message: types.Message):
    await message.answer("📞 Iltimos, nomeringizni yuboring! ",reply_markup=send_nomer)
    global til
    til = message.text
    print(til)


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def contact_handler(message: types.Message):
    global telefon_nomer
    telefon_nomer = message.contact.phone_number
    await message.answer(f"Raqamingiz qabul qilindi: {telefon_nomer}",reply_markup=shaharlar)
    await message.answer("Shaharlar ro'yhatini ko'rish uchun tugmani bosing", reply_markup=shaharlar)
    print(telefon_nomer)



@dp.message_handler(text="Toshkent")
async def tashkent(message: types.Message):
    global shahar
    shahar = message.text
    print(shahar)
    await message.answer("Toshkent shahari tanlandi")
    await message.answer("Buyurtmani birga joylashtiramizmi? 🤗")
    await message.answer(f"""
Buyurtma berishni boshlash uchun 🛒 Buyurtma qilish tugmasini bosing
Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin
<a href="https://telegra.ph/Taomnoma-09-30">Oqtepa Lavash menu:</a>                         
""", parse_mode="HTML", reply_markup=menu)
    
    

@dp.callback_query_handler(text="info")
async def oqtepa_info(callback: types.CallbackQuery):
    await callback.message.answer("""
Biz O‘zbekiston bozorida 12 yildan beri faoliyat yuritamiz va bugungi kunda butun mamlakat bo‘ylab 50 dan ortiq filiallarimiz mavjud. Mazali va to‘yimli taomlar, qulay narxlar, tez yetkazib berish xizmatidan mamnun mijozlar yana va yana bizni tanlamoqda.
Qaynoqqina va mazali lavashlarimiz, shaurmayu donerlarimiz, gamburger va pitsalarimizdan albatta tatib ko'rishingizni tavsiya qilamiz va buyurtmangizga tovuq go'shtidan yangiliklarimizni qo'shishni unutmang!
Yetkazib berish xizmati:  +998781500030
<a href="https://oqtepalavash.uz/">Sayt</a> | <a href="http://fb.me/oqtepalavash.official">Facebook</a> | <a href="https://www.instagram.com/oqtepalavash.official">Instagram</a>
""", parse_mode="HTML")

@dp.callback_query_handler(text="buyurtma_berish")
async def buyurtma_berish(callback: types.CallbackQuery):
    await callback.message.answer("Buyurtma turini tanlang", reply_markup=borib_buyurtma)

@dp.message_handler(text="🛵 Eltib berish")
async def eltib_berish(message: types.Message):
    await message.answer("Eltib berish uchun geo-joylashuvni jo'nating yoki manzilni tanlang", reply_markup=borib_buyurtma_ortga)

@dp.message_handler(text="🔙 Ortga")
async def back(message: types.Message):
    await message.answer("Buyurtma turini tanlang", reply_markup=borib_buyurtma)




@dp.callback_query_handler(text="sozlamalar")
async def sozlamalar_func(callback: types.CallbackQuery):
    await callback.message.answer(f"""
Muloqot tili: {til}
Telefon: {telefon_nomer}
Shahar: {shahar}
Quyidagilardan birini tanlang
""", reply_markup=sozlamalar_buttons)



@dp.callback_query_handler(text="shaharlar_call")
async def shaharlar_func(callback: types.CallbackQuery):
    await callback.message.answer("Shaharlar ro'yhatini ko'rish uchun tugmani bosing", reply_markup=soz_shahar_buttons)