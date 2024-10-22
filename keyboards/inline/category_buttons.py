from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


category_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🆕 YANGILIKLAR",callback_data="yangiliklar_call"),
            InlineKeyboardButton("🍱 Barakali setlar",callback_data="barakali_setlar_call"),
        ],
        [
            InlineKeyboardButton("🌯 Lavashlar",callback_data="lavashlar_call"),
            InlineKeyboardButton("🍔 Burgerlar va Hot-doglar",callback_data="burger_hotdog_call"),
        ],
        [
            InlineKeyboardButton("🥙 Donarlar",callback_data="donarlar_call"),
            InlineKeyboardButton("🥪 Sandvichlar",callback_data="sandvichlar_call"),
        ],
        [
            InlineKeyboardButton("🍟 Sneklar",callback_data="sneklar_call"),
            InlineKeyboardButton("🍕 Katta pitsalar",callback_data="pizza_call"),
        ],
        [
            InlineKeyboardButton("🥗 Salatlar",callback_data="salatlar_call"),
            InlineKeyboardButton("🧊 Yaxna cofe", callback_data="ice_cofe_call")
        ],
        [
            InlineKeyboardButton("🥤 Ichimliklar",callback_data="ichimliklar_call"),
            InlineKeyboardButton("🍰 Shirinliklar",callback_data="shirinliklar_call")
        ],
        [
            InlineKeyboardButton("🍅 Souslar",callback_data="souslar_call")
        ],
        [
            InlineKeyboardButton("🔙 Asosiy menu",callback_data="asosiy_menu_call")
        ]
    ], resize_keyboard=True
)