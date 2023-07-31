import os
from dotenv import load_dotenv
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
# Load the variables from the .env file
load_dotenv()

# Access the variables as environment variables
TOKEN: Final = os.getenv("TELEGRAM_TOKEN")
BOT_USERNAME: Final = os.getenv("TELEGRAM_BOT_USERNAME")

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('"Hello! 🍌 Thanks for chatting! I"m the Banana Bot, your fruity companion!"')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! 🍌 I'm here to assist you with banana-related facts, recipes, jokes, and more! Just ask away!")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! 🍌 Thanks for using the custom command. You're now experiencing the delightful world of bananas with me!")


# Responses
def handle_response(text: str):
    processed_text = text.lower()  # Convert input to lowercase for case-insensitive matching

    if 'hello' in processed_text:
        return "Hey there! 👋"

    if 'how are you' in processed_text:
        return 'I am good! How can I assist you? 😄'

    if 'banana' in processed_text:
        return '🍌 Yes, I love bananas too!'

    if 'recipe' in processed_text:
        return 'Sure! Here is a tasty banana bread recipe: ... 🍞🍌'

    if 'weather' in processed_text:
        return 'I\'m just a banana bot, but you can check the weather online! ☁️☀️'

    if 'help' in processed_text or 'support' in processed_text:
        return 'Of course! How can I help you today? 🤔'

    if 'thank you' in processed_text or 'thanks' in processed_text:
        return 'You\'re welcome! If you have more questions, feel free to ask! 😊🍌'

    if 'tell me a joke' in processed_text:
        return 'Why did the banana go to the party? Because it was a-peeling! 😄🎉'

    if 'your name' in processed_text:
        return 'I am the Banana Bot 🍌, your friendly banana companion!'

    if 'time' in processed_text:
        return 'I am a bot and do not have the ability to tell time. Sorry! ⏰'

    if 'bye' in processed_text or 'goodbye' in processed_text:
        return 'Goodbye! Have a great day! 🍌😊'
    
    if 'I love python' in processed_text:
        return 'Great! Remember to subscribe! 😊'

    # If no specific condition matches, provide a default response
    return "I'm here to chat about bananas! Ask me anything banana-related. 🍌😄"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type:str = update.message.chat.type
    text: str =  update.message.text
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}" ')

    if message_type=='group':
        if BOT_USERNAME in text:
            new_text:str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
          return
    else:
      response:str = handle_response(text)
    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update{update} caused error {context.error}')

if __name__=='__main__':
    app = Application.builder().token(TOKEN).build()

    # Command
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Message
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)


