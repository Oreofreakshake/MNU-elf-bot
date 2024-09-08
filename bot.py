import os
import asyncio
from telebot.async_telebot import AsyncTeleBot
from telebot.types import BotCommand
from dotenv import load_dotenv

load_dotenv()

# my lib
from cogs import cog__init__, commandnames

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = AsyncTeleBot(BOT_TOKEN)

name = commandnames
command = cog__init__.Commands(bot)

async def set_commands():
    await bot.delete_my_commands(scope=None, language_code=None)

    commands = [
        BotCommand(name, description)
        for name, description in zip(name.commandsname, name.commanddescript)
    ]

    await bot.set_my_commands(commands[:3]) 

    cmd = await bot.get_my_commands(scope=None, language_code=None)
    print([c.to_json() for c in cmd])

@bot.message_handler(commands=["hello", "start"])
async def start_command(message):
    await command.start_text(message)

@bot.message_handler(commands=["help"])
async def help_command(message):
    await command.help(message)

@bot.message_handler(commands=["table"])
async def timetable_command(message):
    await command.timetable(message)

@bot.message_handler(commands=["exam"])
async def exam_command(message):
    await command.exam(message)

@bot.callback_query_handler(func=lambda call: True)
async def callback_query(call):
    await command.handle_timetable_callback(call)

@bot.message_handler(func=lambda message: True)
async def message_handler(message):
    await command.handle_timetable_message(message)

async def main():
    print("Bot is starting...")
    await set_commands()
    print("Commands set. Bot is now polling...")
    await bot.infinity_polling()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Runtime error: {e}")
# ==========================================================================================================================
