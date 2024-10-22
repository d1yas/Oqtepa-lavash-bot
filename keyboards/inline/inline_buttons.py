from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🛒 Buyurtma berish", callback_data="buyurtma_berish")
        ],
        [
            InlineKeyboardButton("ℹ️ Biz haqimizda", callback_data="info"),
            InlineKeyboardButton("🛍 Buyurtmalarim", callback_data="my_tovar")
        ],
        [
            InlineKeyboardButton("🏘 Filiallar", callback_data="filial")
        ],
        [
            InlineKeyboardButton("✍️ Fikr Bildirish", callback_data="fikr"),
            InlineKeyboardButton("⚙️ Sozlamalar", callback_data="sozlamalar")
        ]
    ], resize_keyboard=True
)


sozlamalar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Muloqat tili", callback_data="Muloqat_tili_call"),
            InlineKeyboardButton("Telefon", callback_data="telefon_call"),
            InlineKeyboardButton("Shaharlar", callback_data="shaharlar_call")
        ],
        [
            InlineKeyboardButton("🔙 Asosiy menu", callback_data="asosiy_menu_call")
        ]
    ], resize_keyboard=True
)


soz_shahar_buttons = InlineKeyboardMarkup(
   inline_keyboard=[
        [
            InlineKeyboardButton("Toshkent", callback_data="toshkent_call")
        ],
        [
            InlineKeyboardButton("Nukus", callback_data="nukus_call")
        ],
        [
            InlineKeyboardButton("Namangan", callback_data="namangan_call")
        ],
        [
            InlineKeyboardButton("Qoqon", callback_data="qoqon_call")
        ],
        [
            InlineKeyboardButton("Adijon", callback_data="adijon_call"),
        ],
        [
            InlineKeyboardButton("Fagona", callback_data="fagona_call")
        ],
        [
           InlineKeyboardButton("Samarqand", callback_data="samarqand_call")
        ],
        [
            InlineKeyboardButton("Gazalkent", callback_data="gazalkent_call")
        ],
        [
            InlineKeyboardButton("Urgench", callback_data="urgench_call")
        ]
    ], resize_keyboard=True
)