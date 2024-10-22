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
            InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga_call")
        ]
    ], resize_keyboard=True
)
