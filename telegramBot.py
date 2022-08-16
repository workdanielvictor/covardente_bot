import requests
import json
class TelegramBot():
    def __init__(self,token):
        self.token = token
        self.url_base = f'https://api.telegram.org/bot{token}'
        self.last_update_id = 0
        self.chat_id_list = []
    def sendMessage(self):
        for i in self.chat_id_list:
            req = f'{self.url_base}/sendMessage?chat_id={i}&text=Cova o dente ai parça'
            res = requests.get(req)
            resq = json.loads(res.content)
    def getMessages(self):
        req = f'{self.url_base}/getUpdates?offset='+str(self.last_update_id + 1)
        msg = requests.get(req)
        msgpoc = json.loads(msg.content)
        mensagens = msgpoc['result']
        for i in mensagens:
            self.last_update_id = i['update_id']

            chatid = int(i['message']['from']['id'])
            if chatid not in self.chat_id_list:
                self.sendMessage()
                self.chat_id_list.append(chatid)
