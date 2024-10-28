from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.savat_uchun_func import count

# Define the keyboard with the correct argument name
savat_kofe = InlineKeyboardMarkup(
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
            InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga8_savat_call")
        ]
    ],
    resize_keyboard=True
)
