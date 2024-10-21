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
    ]
)
