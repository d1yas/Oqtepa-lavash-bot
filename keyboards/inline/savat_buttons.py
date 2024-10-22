from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


savat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("➖", callback_data="minus_count_call"),
            InlineKeyboardButton("1", callback_data="count_call"),
            InlineKeyboardButton("➕", callback_data="plus_count_call")
        ],
        [
            InlineKeyboardButton("🛒 Savatga qo'shish", callback_data="savatga_qoshish_call"),
        ],
        [
            InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga_lavash_tur_call")
        ]
    ], resize_keyboard=True
)
