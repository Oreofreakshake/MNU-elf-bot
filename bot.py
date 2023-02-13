import telebot
import asyncio
from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot("TOKEN")


if __name__ == "__main__":
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        print("I am online\n")
        asyncio.run(bot.infinity_polling())
    except Exception as e:
        print("run time error\n", e)