
import requests
import json
import os

class Clima():
    def __init__(self, cidade):
        self.url = f'https://api.openweathermap.org/data/2.5/weather?q={cidade},BR&lang=pt_br&units=metric&appid=37a9c005072920a30e4531b4991ab462'
    
    def buscar(self):
        clima = requests.get(self.url).json()
        return str(clima['main']['temp'])   
        
        
        

class TelegramBot:

    def __init__(self):
        token = '5716037309:AAF9noAMwPqhDpZIvxDK_0DJxuEm3F-QCvQ'
        self.url_base = f'https://api.telegram.org/bot{token}/'

  #inicia
    def Iniciar(self):
        update_id = None
        while True:
            update = self.getMessages(update_id)
            menssagens = update['result']
            if menssagens:
                for mensagem in menssagens:
                    update_id = mensagem['update_id']
                    chat_id = mensagem['message']['from']['id']
                    eh_primeira = mensagem['message']['message_id'] == 1
                    resposta = self.criarResp(mensagem, eh_primeira)
                    print(f'Resposta do Bot:{resposta}')
                    self.responder(resposta, chat_id)

  #obtem as mensagens
    def getMessages(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id+1}'
        result = requests.get(link_requisicao)
        return json.loads(result.content)

  #cria resposta
    def criarResp(self, mensagem, eh_primeira):
        chat_id=mensagem['message']['from']['id']
        mensagem=str(mensagem['message']['text'])

        if eh_primeira or mensagem=='/menu':
            return f'''Bem vindo ao nosso Bot!{os.linesep}Lista de Comandos{os.linesep}1 - Ver foto do Vinicius'''
      
        #Envia foto
        if mensagem == '1':
            self.send_image(chat_id)
            return ' '
            
        if mensagem.startswith("/clima"):
            temp = mensagem.removeprefix("/clima")
            temp = temp.strip() 
            clima = Clima(temp.strip())   
            try:
                c = str(clima.buscar())
            except:
                c="Nome da cidade invalido, tente novamente!"    
            finally:    
                return c
            
        
        
        
    def responder(self, resposta, chat_id):
        sendLink = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(sendLink)
    
    def send_image(self, chat_id) :  
        img = open("C:\\Users\\joau\\Desktop\\João Marcos\\Faculdade\\BD2\\BotTele\\imgs\\pic2.jpg", 'rb')
        TOKEN = '5716037309:AAF9noAMwPqhDpZIvxDK_0DJxuEm3F-QCvQ'
        url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={chat_id}'
        print(requests.post(url, files={'photo': img}))

bot = TelegramBot()
bot.Iniciar()
