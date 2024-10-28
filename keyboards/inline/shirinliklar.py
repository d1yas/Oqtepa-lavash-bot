from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


shirinliklar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Donat yongoqli", callback_data="donat_yongoqli_call"),
            InlineKeyboardButton("Donat karamelli", callback_data="donat_karamelli_call")
        ],
        [
            InlineKeyboardButton("Maffin shokoladli", callback_data="maffin_shokoladli_call"),
            InlineKeyboardButton("Donat qulupnayli", callback_data="maffin_karamelli_call")
        ],
        [
            InlineKeyboardButton("Maffin ormon mevalari", callback_data="maffin_ormon_mevalari_call"),
            InlineKeyboardButton("Klasssic shok...pechanyasi", callback_data="klasssic_shok_pechanyasi_call")
        ],
        [
            InlineKeyboardButton("Brauni peshenyesi", callback_data="orqaga_call")
        ],
        [
            InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga_call")
        ]
    ], resize_keyboard=True
)