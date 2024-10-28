from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards.inline.category_buttons import *
from keyboards.inline.savat_button_for_ichimlik import *
from keyboards.inline.ichimliklar_buttons import *
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db_file import *
from states.oqtepa_states import OqtepaState

@dp.callback_query_handler(text="ichimliklar_call")
async def ichimliklar_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/ichimliklar.jpg", "rb"),caption="🥤 Ichimliklar",reply_markup=ichimliklar_buttons)

@dp.callback_query_handler(text="yozgi_ichimliklar_call")
async def yozgi_ichimliklar_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/yozgi_ichimliklar.jpg", "rb"),caption="🥤 Ichimliklar > Yozgi ichimliklar",reply_markup=yozgi_ichimliklar_buttons)

@dp.callback_query_handler(text="qaynoq_ichimliklar_call")
async def qaynoq_ichimliklar_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/qaynoq_ichimliklar.jpg", "rb"),caption="🥤 Ichimliklar > Qaynoq ichimliklar",reply_markup=qaynoq_ichimliklar_buttons)

@dp.callback_query_handler(text="yahna_ichimliklar_call")
async def yahna_ichimliklar_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/yahna_ichimliklar.jpg", "rb"),caption="🥤 Ichimliklar > Yahna ichimliklar",reply_markup=yahna_ichimliklar_buttons)

@dp.callback_query_handler(text="ice_tea_call")
async def ice_tea_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/ice_tea.jpg", "rb"),caption="""
Ice Tea
Narxi:   18 000 so'm
Tavsif: To'yingan mevali ta'm uchun apelsin, yalpiz va kompot qo'shilgan tetiklantiruvchi IceTea
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik)
    
@dp.callback_query_handler(text="tarxun_call")
async def tarxun_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/tarxun.jpg", "rb"),caption="""
Tarxun
Narxi:   18 000 so'm
Tavsif: O'ziga xos va tetiklantiruvchi ta'mni yaratuvchi sirop va yalpizli xushbo'y tarxun.
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik)
    
@dp.callback_query_handler(text="mohito_classic_call")
async def mohito_classic_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/mohito_klassik.jpg", "rb"),caption="""
Mohito klassik
Narxi:   18 000 so'm
Tavsif: Ichimlikka yoqimli tsitrus notasini beruvchi yalpiz va limonli klassik moxito
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik)
    
@dp.callback_query_handler(text="mohito_qulupnay_call")
async def mohito_qulupnay_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/mohito_qulupnay.jpg", "rb"),caption="""
Mohito qulupnay
Narxi:   18 000 so'm
Tavsif: Yorqin va tetiklantiruvchi ta'm - yalpiz va limonli qulupnayli Moxito
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik)
    
@dp.callback_query_handler(text="limonad_shaftoli_call")
async def limonad_shaftoli_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/limonad_shaftoli.jpg", "rb"),caption="""
Limonad shaftoli
Narxi:   12 000 so'm
Tavsif: Har bir qultumi sizni bolalikka qaytaruvchi shaftolili limonad
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik )
    
@dp.callback_query_handler(text="limonad_qulupnay_call")
async def limonad_qulupnay_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/limonad_qulupnay.jpg", "rb"),caption="""
Limonad qulupnay
Narxi:   12 000 so'm
Tavsif: Bolalik va yoz kunlarining xotiralarini yodga soluvchi qulupnayli limonad
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik )

@dp.callback_query_handler(text="limonad_kivi_call")
async def limonad_kivi_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/limonad_kivi.jpg", "rb"),caption="""
Limonad kivi
Narxi:   12 000 so'm
Tavsif: Kivi limonadi ekzotik ta'mga ega bo'lib sevimli bolalikdagi limonadingizni eslatadi
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik )
    

@dp.callback_query_handler(text="qora_choy_call")
async def sochnaya_dolina_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/qora_choy.jpg", "rb"),caption="""
Qora choy, 0.3L
Narxi:   4 000 so'm
Tavsif: Tetiklantiruvchi issiq qora choy
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik )

@dp.callback_query_handler(text="kok_choy_call")
async def kok_choy_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/kok_choy.jpg", "rb"),caption="""
Ko'k choy, 0.3L
Narxi:   4 000 so'm
Tavsif: Quvvatlantiruvchi issiq ko'k choy
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik )

@dp.callback_query_handler(text="limonli_qora_choy_call")
async def limonli_qora_choy_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/limonli_qora_choy.jpg", "rb"),caption="""
Limonli qora choy, 0.3L
Narxi:   7 000 so'm
Tavsif: Xushbo'y limonli tetiklantiruvchi issiq qora choy
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik )
    
@dp.callback_query_handler(text="limonli_kok_choy_call")
async def limonli_kok_choy_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/limonli_kok_choy.jpg", "rb"),caption="""
Limonli ko'k choy, 0.3L
Narxi:   7 000 so'm
Tavsif: Xushbo'y limonli quvvatlantiruvchi issiq ko'k choy
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik )
    
@dp.callback_query_handler(text="kapuchino300_call")
async def kapuchino300_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/kapuchino300.jpg", "rb"),caption="""
Kapuchino 300ml
Narxi:   15 000 so'm
Tavsif: Nafis kapuchino, 300 ml, baxmal sutli ko'pikli va Lavazza donachalaridan tayyorlangan.
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik )
    
@dp.callback_query_handler(text="late300_call")
async def late300_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/latte300.jpg", "rb"),caption="""
Latte 300 ml
Narxi:   15 000 so'm
Tavsif: Klassik latte, 300 ml, to'yingan sutli ta'm va Lavazza donachalaridan tayyorlangan yengil espresso hidiga ega
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik )
    
@dp.callback_query_handler(text="kapuchino200_call")
async def kapuchino200_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/kapuchino200.jpg", "rb"),caption="""
Kapuchino 200ml
Narxi:   12 000 so'm
Tavsif: Nafis kapuchino, 200 ml, baxmal sutli ko'pikli va Lavazza donachalaridan tayyorlangan.
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik )
    
@dp.callback_query_handler(text="americano200_call")
async def americano200_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/americano200.jpg", "rb"),caption="""
Americano 200ml
Narxi:   11 000 so'm
Tavsif: Klassik Ameriкano, 200 ml, chuqur ta'm va xushbo'y hidli, Lavazza donachalari asosida yangi tayyorlangan.
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik )

@dp.callback_query_handler(text="dabl_expresso200_call")
async def espresso200_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/dabl_espresso.jpg", "rb"),caption="""
Dabl espresso 200 ml
Narxi:   12 000 so'm
Tavsif: Achchiq dabl espresso, Lavazza donachalaridan tayyorlangan quyuq ta'm va boy xushbo'y hidga ega.
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik )
    
@dp.callback_query_handler(text="late400_call")
async def late400_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/late400.jpg", "rb"),caption="""
Latte 400 ml
Narxi:   18 000 so'm
Tavsif: Klassik latte, 400 ml, to'yingan sutli ta'm va Lavazza donachalaridan tayyorlangan yengil espresso hidiga ega
Miqdorini tanlang yoki kiriting
    """,reply_markup=savat_ichimlik )
    

@dp.callback_query_handler(text="americano300_call")
async def americano300_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/americano300.jpg", "rb"),caption="""
Americano 300ml
Narxi:   14 000 so'm
Tavsif: Klassik Ameriкano, 300 ml, chuqur ta'm va xushbo'y hidli, Lavazza donachalari asosida yangi tayyorlangan.
Miqdorini tanlang yoki kiriting
            """,reply_markup=savat_ichimlik )
    
@dp.callback_query_handler(text="kappuchino400_call")
async def kappuchino400_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/kapuchino400.jpg", "rb"),caption="""
Kapuchino 400ml
Narxi:   18 000 so'm
Tavsif: Nafis kapuchino, 400 ml, baxmal sutli ko'pikli va Lavazza donachalaridan tayyorlangan.
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik )
    
@dp.callback_query_handler(text="latte200_call")
async def latte200_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/latte200.jpg", "rb"),caption="""
Latte 200 ml
Narxi:   12 000 so'm
Tavsif: Klassik latte, 200 ml, to'yingan sutli ta'm va Lavazza donachalaridan tayyorlangan yengil espresso hidiga ega
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik )
    
@dp.callback_query_handler(text="americano400_call")
async def americano400_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/americano400.jpg", "rb"),caption="""
Americano 400ml
Narxi:   17 000 so'm
Tavsif: Klassik Ameriкano, 400 ml, chuqur ta'm va xushbo'y hidli, Lavazza donachalari asosida yangi tayyorlangan.
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik )
    
@dp.callback_query_handler(text="pepsi_call")
async def pepsi_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/pepsi.jpg", "rb"),caption="""
🥤 Ichimliklar > Yahna ichimliklar > Pepsi
""",reply_markup=pepsi_buttons)
    
@dp.callback_query_handler(text="pepsi04_call")
async def pepsi04_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/pepsi04.jpg", "rb"),caption="""
Pepsi 0.4
Narxi:   9 000 so'm
Tavsif: Pepsi lazzatbaxsh sovuq salqinligidan rohatlaning
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik )
    
@dp.callback_query_handler(text="pepsi03_call")
async def pepsi03_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/pepsi03.jpg", "rb"),caption="""
Pepsi 0.3 L
Narxi:   7 000 so'm
Tavsif: Pepsi lazzatbaxsh sovuq salqinligidan rohatlaning
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik )
    
@dp.callback_query_handler(text="pepsi05_call")
async def pepsi05_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/pepsi05.jpg", "rb"),caption="""
Pepsi, 0.5L
Narxi:   11 000 so'm
Tavsif: Pepsi lazzatbaxsh sovuq salqinligidan rohatlaning
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik )
    
@dp.callback_query_handler(text="pepsi08_call")
async def pepsi08_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/pepsi08.jpg", "rb"),caption="""
Pepsi, 0.8L
Narxi:   15 000 so'm
Tavsif: Pepsi lazzatbaxsh sovuq salqinligidan rohatlaning
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik )
    
@dp.callback_query_handler(text="pepsi15_call")
async def pepsi15_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/pepsi15.jpg", "rb"),caption="""
Pepsi, 1.5L
Narxi:   21 000 so'm
Tavsif: Pepsi lazzatbaxsh sovuq salqinligidan rohatlaning
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik )

@dp.callback_query_handler(text="sochnaya_dolina_call")
async def sochnaya_dolina_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/sochnaya_dolina.jpg", "rb"),caption="""
Sochnaya dolina, 0.2L
Narxi:   5 000 so'm
Tavsif: Bolakaylar uchun mo'ljallangan yuqori sifatli Sochnaya Dolina 200mli sharbatlar liniyasi
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik )
    
@dp.callback_query_handler(text="suv05_call")
async def suv05_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/suv05.jpg", "rb"),caption="""
Gazlanganmagan suv, 0.5L
Narxi:   5 000 so'm
Tavsif: Nestle Santal tetiklantiruvchi ta'midan bahramand bo'ling 
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik )
    
@dp.callback_query_handler(text="mirinda04_call")
async def mirinda04_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/mirinda.jpg", "rb"),caption="""
Mirinda 0.4L
Narxi:   9 000 so'm
Tavsif: Mirinda 0.4L, 
Miqdorini tanlang yoki kiriting
""",reply_markup=savat_ichimlik )
    
@dp.callback_query_handler(text="lipton05_call")
async def lipton05_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/lipton.jpg", "rb"),caption="""
Lipton ko'k choyi 0.5L
Narxi:   10 000 so'm
Tavsif: Lipton tetiklantiruvchi choyi salqinligidan baxra oling
Miqdorini tanlang yoki kiriting
    """,reply_markup=savat_ichimlik )



@dp.callback_query_handler(text="orqaga_ichimliklar_call")
async def orqaga_ichimliklar_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/ichimliklar.jpg", "rb"),caption="🥤 Ichimliklar",reply_markup=category_buttons)

@dp.callback_query_handler(text="orqaga9_savat_call")
async def orqaga9_savat_func(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(open("images/ichimliklar.jpg", "rb"),caption="🥤 Ichimliklar",reply_markup=category_buttons)