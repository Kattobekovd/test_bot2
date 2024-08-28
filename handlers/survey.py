from aiogram import F, Router, types
from aiogram.filters.command import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from config import database

survey_router = Router()


class BookSurvey(StatesGroup):
    name = State()
    age = State()
    gender = State()
    occupation = State()


@survey_router.message(Command("opros"))
async def opross(message: types.Message, state: FSMContext):
    await state.set_state(BookSurvey.name)
    await message.answer("Давайте начнем опрос. Вы его можете остановить при помощи слова 'стоп'")
    await message.answer("Как Вас зовут?")


@survey_router.message(F.text.lower() == "стоп")
async def stop(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Спасибо за прохождение опроса!")


@survey_router.message(BookSurvey.name)
async def opros_age(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(BookSurvey.age)
    await message.answer("Сколько Вам лет?")


@survey_router.message(BookSurvey.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Вводите только цифры")
        return
    age = int(age)
    if age < 17:
        await message.answer("К сожалению, опрос доступен только для пользователей старше 17 лет.")
        await state.finish()
        return
    if age > 90:
        await message.answer("Вводите числа до 90!")
        return
    await state.update_data(age=age)
    await state.set_state(BookSurvey.gender)
    await message.answer("Какого Вы пола?")


@survey_router.message(BookSurvey.gender)
async def process_gender(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await state.set_state(BookSurvey.occupation)
    await message.answer("Род занятий?")


@survey_router.message(BookSurvey.occupation)
async def process_occupation(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за пройденный опрос!")

    data = await state.get_data()
    name = data.get("name")
    age = data.get("age")
    gender = data.get("gender")
    occupation = message.text

    print(f"Received data: name={name}, age={age}, gender={gender}, occupation={occupation}")

    await database.insert_survey_data(name, age, gender, occupation)

    await state.clear()
