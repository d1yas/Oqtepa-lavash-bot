from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

yahna_ichimliklar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Ice tea", callback_data="ice_tea_call"),
            InlineKeyboardButton("Tarxun", callback_data="tarxun_call")
        ],
        [
            InlineKeyboardButton("Mohito klassik", callback_data="mohito_klassik_call"),
            InlineKeyboardButton("Mohito qulupnay", callback_data="mohito_qulupnay_call")
        ],
        [
            InlineKeyboardButton("Limonad shaftoli", callback_data="limonad_shaftoli_call"),
            InlineKeyboardButton("Limonad qulupnay", callback_data="limonad_qulupnay_call")
        ],
        [
            InlineKeyboardButton("Limonad kivi", callback_data="limonad_kivi_call")
        ],
        [
            InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga_call")
        ]
    ], resize_keyboard=True
)
