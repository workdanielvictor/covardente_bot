import datetime
import os
import time
import sys



from telegramBot import TelegramBot
senha = os.environ['KEY_KAKAROTO']
print(senha)
sys.stdout.flush()
bot = TelegramBot(senha)
HORA_MIN = 11
HORA_MAX = 23
print("BOT TELEGRAM ALIVE")
sys.stdout.flush()
bot.getMessages()
bot.sendMessage("covador tá on")
while(True):
    time.sleep(30)
    bot.getMessages()
    hora = datetime.datetime.now().time().hour
    if(hora > HORA_MIN and hora << HORA_MAX):
        print(hora)
        sys.stdout.flush()
        bot.sendMessage()
        time.sleep((60*60)*2)