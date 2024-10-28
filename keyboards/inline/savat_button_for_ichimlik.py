from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.savat_uchun_func import count

# Define the keyboard with the correct argument name
savat_ichimlik = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("➖", callback_data="minus_count_call") if count > 0 else InlineKeyboardButton(" ", callback_data="ignore"),
            InlineKeyboardButton(str(count), callback_data="count_call"),
            InlineKeyboardButton("➕", callback_data="plus_count_call")
        ],
        [
            InlineKeyboardButton("🛒 Savatga qo'shish", callback_data="savatga_qoshish_call"),
        ],
        [
            InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga9_savat_call")
        ]
    ],
    resize_keyboard=True
)


savat_ichimlik_qaynoq = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("➖", callback_data="minus_count_call") if count > 0 else InlineKeyboardButton(" ", callback_data="ignore"),
            InlineKeyboardButton(str(count), callback_data="count_call"),
            InlineKeyboardButton("➕", callback_data="plus_count_call")
        ],
        [
            InlineKeyboardButton("🛒 Savatga qo'shish", callback_data="savatga_qoshish_call"),
        ],
        [
            InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga10_savat_call")
        ]
    ],
    resize_keyboard=True
)

savat_ichimlik_yahna = InlineKeyboardMarkup(    
   inline_keyboard=[
        [
            InlineKeyboardButton("➖", callback_data="minus_count_call") if count > 0 else InlineKeyboardButton(" ", callback_data="ignore"),
            InlineKeyboardButton(str(count), callback_data="count_call"),
            InlineKeyboardButton("➕", callback_data="plus_count_call")
        ],
        [
            InlineKeyboardButton("🛒 Savatga qo'shish", callback_data="savatga_qoshish_call"),
        ],
        [
            InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga11_savat_call")
        ]
    ],
    resize_keyboard=True
)