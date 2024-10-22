from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


sendvich_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Klab sendvich frisiz", callback_data="klab_sendvich_frisiz_call"),
            InlineKeyboardButton("Klab sendvich fri bilan", callback_data="klab_sendvich_fri_bilan_call")
        ],
        [
            InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga_call")
        ]
    ], resize_keyboard=True
    
)