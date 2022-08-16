import datetime
import os
import time
from boto.s3.connection import S3Connection
s3 = S3Connection(os.environ['S3_COISA'], os.environ['S3_SECRET'])
print(s3)


from telegramBot import TelegramBot

bot = TelegramBot()
HORA_MIN = 8
HORA_MAX = 20
print("BOT TELEGRAM ALIVE")
while(True):
    time.sleep(60)
    bot.getMessages()
    hora = datetime.datetime.now().time().hour
    if(hora > HORA_MIN and hora << HORA_MAX):
        print(hora)
        bot.sendMessage()
        time.sleep((60*60)*2)