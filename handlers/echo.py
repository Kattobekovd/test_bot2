from aiogram import Router, types


echo_router = Router()

@echo_router.message()
async def echo(message: types.Message):
    # logging.info(message)
    await message.answer("Я не понимаю вас, поробуйте следующие команды: \n"
    "/start - начать диалог\n"
    "/picture - отправить картинку")