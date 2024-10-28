from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards.inline.news_buttons import yangiliklar_buttons
from keyboards.inline.savat_button_for_news import savat_news
from keyboards.inline.category_buttons import category_buttons
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db_file import *
from states.oqtepa_states import OqtepaState

@dp.callback_query_handler(text="yangiliklar_call")
async def yangiliklar_func(call: types.CallbackQuery):
    await call.message.delete()
    with open("images/yangiliklar.jpg", "rb") as photo:
        await call.message.answer_photo(photo, caption="🆕 YANGILIKLAR", reply_markup=yangiliklar_buttons)

@dp.callback_query_handler(text="orqaga13_savat_call")
async def orqaga_func(call: types.CallbackQuery):
    await call.message.delete()
    with open("images/yangiliklar.jpg", "rb") as photo:
        await call.message.answer_photo(photo, caption="🆕 YANGILIKLAR", reply_markup=yangiliklar_buttons)


@dp.callback_query_handler(text="orqaga_news__call")
async def orqaga_yangiliklar_func(call: types.CallbackQuery):
    await call.message.delete()
    with open("images/yangiliklar.jpg", "rb") as photo:
        await call.message.answer_photo(photo, caption="🆕 YANGILIKLAR", reply_markup=category_buttons)

@dp.callback_query_handler(text="sezar_vrap_call")
async def sezar_vrap_func(call: types.CallbackQuery):
    await call.message.delete()
    with open("images/sezar_vrap.jpg", "rb") as photo:
        await call.message.answer_photo(photo, caption="""
Sezar Vrap
Narxi: 24 000 so'm
Tavsif: Sezar sousi va yangi sabzavotlar bilan to'ldirilgan tortilya, ichida tovuq, pomidor, pishloq va salat aysberg mavjud.
Miqdorini tanlang yoki kiriting
""", reply_markup=savat_news)

@dp.callback_query_handler(text="bbq_vrap_call")
async def bbq_vrap_func(call: types.CallbackQuery):
    await call.message.delete()
    with open("images/bbq_vrap.jpg", "rb") as photo:
        await call.message.answer_photo(photo, caption="""
BBQ vrap
Narxi: 24 000 so'm
Tavsif: Mazali BBQ sousi bilan to'ldirilgan tortilya ichida tovuq, pomidor, tuzlangan bodring va pishloqning ajoyib kombinatsiyasi.
Miqdorini tanlang yoki kiriting
    """, reply_markup=savat_news)

@dp.callback_query_handler(text="qisllimala_hot_dog_call")
async def qisllimala_hot_dog_func(call: types.CallbackQuery):
    await call.message.delete()
    with open("images/qirsilama_hot_dog.jpg", "rb") as photo:
        await call.message.answer_photo(photo, caption="""
Qirsillama hot dog
Narxi: 12 000 so'm
Tavsif: Mini hot-dog nonida Kanada sosiskasi, pomidor, pishloq, gam sousi va quritilgan piyoz, mazali va qoniqarli ta'm.
Miqdorini tanlang yoki kiriting
""", reply_markup=savat_news)

@dp.callback_query_handler(text="kenja_hot_dog_call")
async def kenja_hot_dog_func(call: types.CallbackQuery):
    await call.message.delete()
    with open("images/kenja_hot_dog.jpg", "rb") as photo:
        await call.message.answer_photo(photo, caption="""
Kenja hot dog
Narxi: 12 000 so'm
Tavsif: Kanada sosiskasi, pishloq va pomidor bilan to'ldirilgan mini hot-dog noni, original va mazali.
Miqdorini tanlang yoki kiriting
""", reply_markup=savat_news)

@dp.callback_query_handler(text="tovuqli_looonger_call")
async def tovuqli_looonger_func(call: types.CallbackQuery):
    await call.message.delete()
    with open("images/tovuqli_loonzer.jpg", "rb") as photo:
        await call.message.answer_photo(photo, caption="""
Tovuqli looonger
Narxi: 25 000 so'm
Tavsif: Mazali longer nonida, sabzavotlar, pishloq va gam sousi bilan to'ldirilgan tovuq, sizni qoniqtiradigan va to'yimli ta'm bilan hayratda qoldiradi.
Miqdorini tanlang yoki kiriting
""", reply_markup=savat_news)

@dp.callback_query_handler(text="qizil_karamli_salat_call")
async def qizil_karamli_salat_func(call: types.CallbackQuery):
    await call.message.delete()
    with open("images/qizil_karamli_salat.jpg", "rb") as photo:
        await call.message.answer_photo(photo, caption="""
Qizil karamli salat
Narxi: 8 000 so'm
Tavsif: Qizil karam, sabzi va kashnich bilan tayyorlangan, Grek sousi bilan aralashtirilgan yengil salat, yangi va sog'lom tanlov.
Miqdorini tanlang yoki kiriting
""", reply_markup=savat_news)

@dp.callback_query_handler(text="vrap_master_call")
async def vrap_master_func(call: types.CallbackQuery):
    await call.message.delete()
    with open("images/vrap_master.jpg", "rb") as photo:
        await call.message.answer_photo(photo, caption="""
Vrap master
Narxi: 30 000 so'm
Tavsif: Yumshoq tortilya nonida oq sous, Hohland pishlog'i, pomidor, aysberg salati, tovuq stripslari va qarsildoq hashbraun. Mazali va to'yimli taom!
Miqdorini tanlang yoki kiriting
""", reply_markup=savat_news)

@dp.callback_query_handler(text="kanadalik_fri_call")
async def kanadalik_fri_func(call: types.CallbackQuery):
    await call.message.delete()
    with open("images/kanadalik_fri.jpg", "rb") as photo:
        await call.message.answer_photo(photo, caption="""
Canada fri
Narxi: 25 000 so'm
Tavsif: Qarsildoq fri, maxsus ziravorlar, pishloqli sous va quritilgan piyoz bilan bezatilgan. Har bir luqma mazali va lazzatli!
Miqdorini tanlang yoki kiriting
""", reply_markup=savat_news)

@dp.callback_query_handler(text="pishloqli_3_call")
async def pishloqli_3_func(call: types.CallbackQuery):
    await call.message.delete()
    with open("images/pishloqli_3.jpg", "rb") as photo:
        await call.message.answer_photo(photo, caption="""
Pishloqli Yostiqchalar 3 dona
Narxi: 16 000 so'm
Tavsif: 3 ta yumshoq xamir yostiqchasi, erigan pishloq bilan to'ldirilgan. Har bir yostiqcha pishloqning haqiqiy lazzatini va yumshoq teksturasini taqdim etadi!
Miqdorini tanlang yoki kiriting
""", reply_markup=savat_news)

@dp.callback_query_handler(text="pishloqli_5_call")
async def pishloqli_5_func(call: types.CallbackQuery):
    await call.message.delete()
    with open("images/pishloqli_5.jpg", "rb") as photo:
        await call.message.answer_photo(photo, caption="""
Pishloqli yostiqchalar 5 dona
Narxi: 23 000 so'm
Tavsif: 5 ta yumshoq xamir yostiqchasi, erigan pishloq bilan to'ldirilgan. Har bir yostiqcha pishloqning haqiqiy lazzatini va yumshoq teksturasini taqdim etadi!
Miqdorini tanlang yoki kiriting
""", reply_markup=savat_news)

@dp.callback_query_handler(text="pishloqli_8_call")
async def pishloqli_8_func(call: types.CallbackQuery):
    await call.message.delete()
    with open("images/pishloqli_8.jpg", "rb") as photo:
        await call.message.answer_photo(photo, caption="""
Pishloqli yostiqchalar 8 dona
Narxi: 36 000 so'm
Tavsif: 8 ta yumshoq xamir yostiqchasi, erigan pishloq bilan to'ldirilgan. Har bir yostiqcha pishloqning haqiqiy lazzatini va yumshoq teksturasini taqdim etadi!
Miqdorini tanlang yoki kiriting
""", reply_markup=savat_news)

@dp.callback_query_handler(text="qirsillama_3_call")
async def qirsillama_3_func(call: types.CallbackQuery):
    await call.message.delete()
    with open("images/qirsillama_3.jpg", "rb") as photo:
        await call.message.answer_photo(photo, caption="""
Qirsillama Halqachalar 3 dona
Narxi: 10 000 so'm
Tavsif: Maxsus ziravorlar bilan tayyorlangan 3 ta qarsildoq piyoz halqalari. Har bir halqa o'ziga xos lazzat va yoqimli qarsillashni hadya etadi!
Miqdorini tanlang yoki kiriting
""", reply_markup=savat_news)

@dp.callback_query_handler(text="qirsillama_5_call")
async def qirsillama_5_func(call: types.CallbackQuery):
    await call.message.delete()
    with open("images/qirsillama_5.jpg", "rb") as photo:
        await call.message.answer_photo(photo, caption="""
Qirsillama halqachalar 5 dona
Narxi: 15 000 so'm
Tavsif: Maxsus ziravorlar bilan tayyorlangan 5 ta qarsildoq piyoz halqalari. Har bir halqa o'ziga xos lazzat va yoqimli qarsillashni hadya etadi!
Miqdorini tanlang yoki kiriting
""", reply_markup=savat_news)
        

