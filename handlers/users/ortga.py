# from aiogram import types
# from aiogram.dispatcher import FSMContext
# from loader import dp
# from keyboards.inline.souslar_buttons import *
# from keyboards.inline.savat_button_for_sous import *
# from keyboards.inline import category_buttons
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from db_file import *
# from states.oqtepa_states import OqtepaState


# @dp.callback_query_handler(text="orqaga_savat_call")
# async def orqaga6_savat_call(call: types.CallbackQuery):
#     await call.message.edit_reply_markup(reply_markup=category_buttons)
#     await call.answer()