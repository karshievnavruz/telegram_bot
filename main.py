from telegram import Bot
import os 

# Get the token from the environment variables
TOKEN = os.environ['TOKEN']
# Create a bot object
bot = Bot('5503823244:AAFNZ-echSZpypl7dIKeeMLroXN7OBraNHo')
# Print the bot info


# Send a message to the bot
bot.sendMessage(123456789,"Hello World")