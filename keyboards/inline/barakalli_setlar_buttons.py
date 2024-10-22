from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


barskali_setlar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Tandie lavash seti", callback_data="tandie_lavash_seti_call"),
            InlineKeyboardButton("Lavash seti", callback_data="lavash_seti_call")
        ],
        [
            InlineKeyboardButton("Pita doner seti", callback_data="pita_doner_seti_call"),
            InlineKeyboardButton("Gamburger seti", callback_data="gamburger_seti_call")
        ],
        [
            InlineKeyboardButton("Shohona hot dog seti", callback_data="shohona_hot_dog_seti_call"),
            InlineKeyboardButton("Hod dog seti", callback_data="_call")
        ]
    ]
)