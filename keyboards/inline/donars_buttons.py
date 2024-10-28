from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

donarlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Haggi", callback_data="haggi_call"),
            InlineKeyboardButton("Big Donner", callback_data="big_donner_call")
        ],
        [
            InlineKeyboardButton("Shaurma", callback_data="shaurma_call"),
            InlineKeyboardButton("Pita Donner", callback_data="pita_donner_call")
        ],
        [
            InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga_call")
        ]
    ], resize_keyboard=True
)