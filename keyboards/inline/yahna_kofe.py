from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


yahna_kofe_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Yahna shok...kapuchino", callback_data="yahna_shok_kapuchino_call"),
            InlineKeyboardButton("Yahna tuz...kapuchino", callback_data="yahna_tuz_kapuchino_call")
        ],
        [
            InlineKeyboardButton("Yahna iris-tofi kapuchino", callback_data="yahna_iris_tofi_kapuchino_call"),
            InlineKeyboardButton("Yahna klassic kapuchino", callback_data="yahna_shok_latte_call")
        ],
        [
            InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga_call")
        ]
    ], resize_keyboard=True
)