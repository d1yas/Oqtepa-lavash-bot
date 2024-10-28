from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

snek = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Kartoshka fri o'rta",callback_data="kartoshka_fri_orta_call"),
            InlineKeyboardButton("Kartoshka fri katta",callback_data="kartoshka_fri_katta_call")
        ],
        [
            InlineKeyboardButton("Jo'ja boks",callback_data="joja_boks_call"),
            InlineKeyboardButton("Strips 5 dona",callback_data="strips_5_dona_call")
        ],
        [
            InlineKeyboardButton("Strips 3 dona",callback_data="strips_3_dona_call"),
            InlineKeyboardButton("Kartoshka fri kichik",callback_data="kartoshka_fri_kichik_call")
        ],
        [
            InlineKeyboardButton("Baytslar",callback_data="baytslar_call"),
            InlineKeyboardButton("Jaydari kartoshka",callback_data="jaydari_kartoshka_call")
        ],
        [
            InlineKeyboardButton("Non", callback_data="non_call"),
            InlineKeyboardButton("Nagetlar 5 dona", callback_data="nagetlar_5_call")
        ],
        [
            InlineKeyboardButton("Nagetslar boks", callback_data="nagetslar_boks_call"),
            InlineKeyboardButton("Nagetlar 8 dona", callback_data="nagetlar_8_call")

        ],
        [
            InlineKeyboardButton("Nagetlar 15 dona", callback_data="nagetlar_15_call")
        ],
        [
            InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga_call"),
            InlineKeyboardButton("🛒 Savatcha", callback_data="savatcha_call")
        ],

    ],

)
