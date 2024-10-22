from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


burger_va_hot_doglar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Gamburger", callback_data="gamburger_call"),
            InlineKeyboardButton("Chizburger", callback_data="chizburger_call")
        ],
        [
            InlineKeyboardButton("Big burger", callback_data="big_burger_call"),
            InlineKeyboardButton("Big chizburger", callback_data="big_chizburger_call")
        ],
        [
            InlineKeyboardButton("Hot dog", callback_data="hot_dog_call"),
            InlineKeyboardButton("Pishloqli hot dog", callback_data="pishloqli_hot_dog_call")
        ],
        [
            InlineKeyboardButton("Shohona hot dog", callback_data="shohona_hot_dog_call")
        ],
        [
            InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga_call")
        ]
    ], resize_keyboard=True
)