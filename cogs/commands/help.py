from cogs import commandnames

async def help(bot, message):
    message_text = "Here are the commands you can use!\nYou can also use the menu button to navigate through the bot!\n\n"
    
    commands_with_descriptions = {
        "help": "• Bot's guide - You are here!",
        "links": "• Get useful links for your studies",
        "table": "• View your personalized class schedule",
        "exam": "• Check the final exam timetable"
    }
    
    for command, description in commands_with_descriptions.items():
        message_text += f"/{command}\n{description}\n"
    
    await bot.send_message(message.chat.id, message_text)











#     from cogs import commandnames

# async def help(bot, message):
#     message_text = "Here are the commands you can use!\n\n" + \
#                   f"/help        👈 You are here\n" + \
#                   f"/links        - Useful links\n" + \
#                   f"/table       - Class schedule\n" + \
#                   f"/exam      - Final exam schedule\n\n" + \
#                   "You can also use the menu button to navigate through the bot!"

#     await bot.send_message(message.chat.id, message_text)