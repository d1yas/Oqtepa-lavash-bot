from aiogram.dispatcher.filters.state import State, StatesGroup


class OqtepaState(StatesGroup):
    start_state = State()
    language_state = State()
    contact_state = State()
    location_state = State()
    category_state = State()
    lavash_state = State()