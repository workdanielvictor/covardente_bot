import datetime
import time

from telegramBot import TelegramBot

bot = TelegramBot("5709111053:AAGnHL5ZJei7kAJEA89oM1Y_EyfpuKByfqs")
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