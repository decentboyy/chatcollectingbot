import telebot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token obtained from the BotFather
bot = telebot.TeleBot('6101196560:AAE9Te6XfIfldcJcqdnh6Yb7SHPVi_z3hRc')

# Replace 'LOG_GROUP_ID' with the ID of the log group where you want to save the conversations
log_group_id = '-1001832126466'

@bot.message_handler(func=lambda message: True)
def save_chat(message):
    chat_id = message.chat.id
    chat_type = message.chat.type

    # Check if the message is from a group
    if chat_type == 'group' or chat_type == 'supergroup':
        # Format the chat message in 'question: answer' format
        chat_message = f"{message.text}: {message.reply_to_message.text}"

        # Send the formatted chat message to the log group
        bot.send_message(log_group_id, chat_message)

# Run the bot
bot.polling()
