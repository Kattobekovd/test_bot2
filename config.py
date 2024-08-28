from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
from pathlib import Path
from db.database import Database

load_dotenv()

token = getenv('BOT_TOKEN')

bot = Bot(token=token)
dp = Dispatcher()

database = Database(Path(__file__).parent / "db.sqlite3")

database.create_tables()
