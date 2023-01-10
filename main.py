from telegram import Bot
import os 

# Get the token from the environment variables
TOKEN = os.environ['TOKEN']
# Create a bot object
bot = Bot(TOKEN)
# Print the bot info

chat_id = 996172963
# Send a message to the bot
msg = bot.sendMessage(chat_id,"Hello World!!!")
# print(msg.text)

msg = bot.getUpdates(5)
print(msg)

photo_id = "https://random.dog/f6997cc3-31c7-41ef-a44a-e0446cb758af.jpg"
# msg = bot.sendPhoto(chat_id, photo_id)

sticker = 'CAACAgIAAxkBAAOXY70b4xwDC2UmLoQoD4SpZ8riI8EAAhEAAwJORjZYaLtih0YVpC0E'
# stic = bot.sendSticker(chat_id, sticker)

doc = 'BQACAgIAAxkBAAOhY70flPMbldSbAUOSgAl9sDsoQogAAhkkAAJKe9hJYJvJgrG4Mq0tBA'
# message_doc = bot.sendDocument(chat_id, doc)

video = 'BAACAgIAAxkBAAOpY70hTwO3mOZs8iJwCkjGhXgr04oAAiAkAAJd5lhI89cy_rqarygtBA'
# message_video = bot.sendVideo(chat_id, video)

latitude = 40.097501
longitude = 65.382395
# message_loc = bot.sendLocation(chat_id, latitude, longitude)

phone_number = '913337760'
first_name = "𓅓"
# message_cont = bot.sendContact(chat_id, phone_number, first_name)