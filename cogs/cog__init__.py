
# commands
from cogs.commands.help import help



class Commands:
    def __init__(self, bot):
        self.bot = bot

    async def start_text(self, message):  # ✅
        await self.bot.send_message(
            message.chat.id,
            f"""Hello 👋\nYou can use /help for every command details""",
        )

    # -----------------------------------------------------------------------------------------------

    async def help(self, message):
        await help(self.bot, message)

print("Commands successfully initialized!\n")