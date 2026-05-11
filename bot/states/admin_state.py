from aiogram.fsm.state import State, StatesGroup


class Broadcast(StatesGroup):
    text = State() # текст для рассылки

class AddSub(StatesGroup):
    id = State() # id кому выдать
    time = State() # на сколько выдать