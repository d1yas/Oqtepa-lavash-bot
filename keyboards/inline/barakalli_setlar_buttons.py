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
        ],
        [
            InlineKeyboardButton("Tandir lavash juftligi", callback_data="tandir_lavash_juftligi_call"),
            InlineKeyboardButton("Lavash juftligi", callback_data="lavash_juftligi_call")
        ],
        [
            InlineKeyboardButton("Shaurma juftligi", callback_data="shaurma_juftligi_call"),
            InlineKeyboardButton("juftlik seti", callback_data="juftlik_seti_call")
        ],
        [
            InlineKeyboardButton("Lavashdan baraka", callback_data="lavashdan_baraka_call"),
            InlineKeyboardButton("Chizda baraka", callback_data="chizda_baraka_call")
        ],
        [
            InlineKeyboardButton("Shaurmadan baraka", callback_data="shaurmadan_baraka_call")
        ],
        [
            InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga_call")
        ]
    ], resize_keyboard=True
)