from cogs import commandnames


async def help(bot, message):
    await bot.send_message(
        message.chat.id,
        f"""𝗛𝗲𝗿𝗲 𝗮𝗿𝗲 𝘁𝗵𝗲 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝘆𝗼𝘂 𝗰𝗮𝗻 𝘂𝘀𝗲!
/{commandnames.commandsname[0]} - 👈 You are here
/{commandnames.commandsname[1]} - Useful links
/{commandnames.commandsname[2]} - Class schedule
/{commandnames.commandsname[3]} - Final exam schedule
         """,
    )
