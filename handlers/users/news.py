from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards.inline.news_buttons import *
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db_file import *
from states.oqtepa_states import OqtepaState


@dp.callback_query_handler(text="yangiliklar_call")
async def yangiliklar_func(call: types.CallbackQuery):
    await call.message.answer_photo(open("images/yangiliklar.jpg", "rb"),caption="🆕 YANGILIKLAR",reply_markup=yangiliklar_buttons)
