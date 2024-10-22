from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


yozgi_ichimliklar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Pepsi", callback_data="pepsi_call"),
            InlineKeyboardButton("Sochnaya dolina", callback_data="sochnaya_dolina_call")
        ],
        [
            InlineKeyboardButton("Suv 0.5L", callback_data="suv_05_call"),
            InlineKeyboardButton("Mirinda 0.4L", callback_data="mirinda_04_call")
        ],
        [
            InlineKeyboardButton("Lipton 0.5L", callback_data="lipton_05_call")
        ],
        [
            InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga_call")
        ]
    ], resize_keyboard=True
)