from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ichimliklar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Yozgi ichimliklar", callback_data="yozgi_ichimliklar_call"),
            InlineKeyboardButton("Qaynoq ichimliklar", callback_data="qaynoq_ichimliklar_call")
        ],
        [
            InlineKeyboardButton("Yahna ichimliklar", callback_data="yahna_ichimliklar_call")
        ],
        [
            InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga_ichimliklar_call")
        ]
    ], resize_keyboard=True
    
)


yozgi_ichimliklar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Ice Tea", callback_data="ice_tea_call"),
            InlineKeyboardButton("Tarxun", callback_data="tarxun_call")
        ],
        [
            InlineKeyboardButton("Mohito classic", callback_data="mohito_classic_call"),
            InlineKeyboardButton("Mohito qulupnay", callback_data="mohito_qulupnay_call")
        ],
        [
            InlineKeyboardButton("Limonad shaftoli", callback_data="limonad_shaftoli_call"),
            InlineKeyboardButton("Limonad qulupnay", callback_data="limonad_qulupnay_call")
        ],
        [
            InlineKeyboardButton("Limonad kivi", callback_data="limonad_kivi_call"),
        ],
        [
            InlineKeyboardButton("⬅️ Ortga ", callback_data="ortga_yozgi_call")
        ]
    ], resize_keyboard=True
)

qaynoq_ichimliklar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Qora choy", callback_data="qora_choy_call"),
            InlineKeyboardButton("Ko'k choy", callback_data="kok_choy_call")
        ],
        [
            InlineKeyboardButton("🍋 Limonli qora choy", callback_data="limonli_qora_choy_call"),
            InlineKeyboardButton("🍋 Limonli ko'k choy", callback_data="limonli_kok_choy_call")
        ],
        [
            InlineKeyboardButton("Kapuchino 300 ml ", callback_data="kapuchino300_call"),
            InlineKeyboardButton("Late 300 ml ", callback_data="late300_call")
        ],
        [
            InlineKeyboardButton("Kapuchino 200 ml ", callback_data="kapuchino200_call"),
            InlineKeyboardButton("Americano 200 ml ", callback_data="americano200_call")
        ],
        [
            InlineKeyboardButton("Dabl expresso 200 ml", callback_data="dabl_expresso200_call"),
            InlineKeyboardButton("Late 400 ml ", callback_data="late400_call")
        ],
        [
            InlineKeyboardButton("Americano 300 ml ", callback_data="americano300_call"),
            InlineKeyboardButton("Kappuchino 400 ml ", callback_data="kappuchino400_call")
        ],
        [
            InlineKeyboardButton("Latte 200 ml ", callback_data="latte200_call"),
            InlineKeyboardButton("Americano 400 ml ", callback_data="americano400_call")
        ],
        [
            InlineKeyboardButton("⬅️ Ortga ", callback_data="ortga_qaynoq_call")
        ]
    ], resize_keyboard=True
)

yahna_ichimliklar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Pepsi", callback_data="pepsi_call"),
            InlineKeyboardButton("Sochnaya dolina", callback_data="sochnaya_dolina_call")

        ],
        [
            InlineKeyboardButton("Suv 0,5L", callback_data="suv05_call"),
            InlineKeyboardButton("Mirinda 0,4L", callback_data="mirinda04_call")
        ],
        [
            InlineKeyboardButton("Lipton 0,5L", callback_data="lipton05_call")
        ],
        [
            InlineKeyboardButton("⬅️ Ortga ", callback_data="ortga_yahna_call")
        ]
    ], resize_keyboard=True
)
pepsi_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Pepsi 0,4L", callback_data="pepsi04_call"),
            InlineKeyboardButton("Pepsi 0,3L", callback_data="pepsi03_call")
        ],
        [
            InlineKeyboardButton("Pepsi 0,5L", callback_data="pepsi05_call"),
            InlineKeyboardButton("Pepsi 0,8L ", callback_data="pepsi08_call")
        ],
        [
            InlineKeyboardButton("Pepsi 1,5L", callback_data="pepsi15_call")
        ],
        [
            InlineKeyboardButton("⬅️ Ortga ", callback_data="ortga_pepsi_call")
        ]
    ], resize_keyboard=True
)
