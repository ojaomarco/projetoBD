from bs4 import BeautifulSoup
import requests
import json 
from os import linesep

class Tradutor:
    
    def __init__(self):
        self.url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
        self.headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "275c0469eamsh4cc0d1d4f4864e2p1f7dbajsn3c51356236e5",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
        }   
        
        
    def tr_to_pt(self,text):
        payload = f"q={text}&target=pt&source=en"
        translated = requests.request("POST", self.url, data=payload, headers=self.headers).json()
        return str(translated['data']['translations'][0]['translatedText'])
    
    def tr_to_en(self,text):
        payload = f"q={text}&target=en&source=pt"
        translated = requests.request("POST", self.url, data=payload, headers=self.headers).json()
        return str(translated['data']['translations'][0]['translatedText'])
                

class Noticies:
    def __init__(self): 
        url = 'http://g1.com.br/'
        req = requests.get(url)
        html = req.text

        soup = BeautifulSoup(html,'html.parser')
        self.colecao = soup.find_all(class_="feed-post-link gui-color-primary gui-color-hover")
    #retorna as principais noticias do G1 e seus links
    def getNoticias(self):
        mensagem = ""
        string = None
        for i in self.colecao:
            mensagem += "<b>"+ str(i.get_text()) + "</b>\n"
            mensagem += i.get('href') + "\n\n"
        return mensagem 
    
    def get_noticias_sep(self):
        lista = []
        for i in self.colecao:
            lista.append(i.get('href'))     
        return lista           
            
      
class Clima():
    def __init__(self, cidade):
        self.url = f'https://api.openweathermap.org/data/2.5/weather?q={cidade},BR&lang=pt_br&units=metric&appid=37a9c005072920a30e4531b4991ab462'
    
    def buscar(self):
        try: 
            clima = requests.get(self.url).json()
            cidade = clima['name']
            pais = clima['sys']['country']
            temp = round(clima['main']['temp'])
            situacao = clima['weather'][0]['description']
            icon = ""
            match (situacao):
                case 'céu limpo':
                    icon = "\U00002600"
                case 'chuva leve':
                    icon = "\U0001F327"
                case 'neblina':
                    icon = "\U0001F32B"
                case 'algumas nuvens':
                    icon = "\U000026C5"
                case 'nuvens dispersas':
                    icon = "\U0001F324"
                case 'trovoadas':
                    icon = "\U0001F329"
                case 'chuva moderada':  
                    icon = "\U0001F327"
                case 'nublado':
                    icon = "\U00002601"
            vento = clima['wind']['speed']
            umidade = clima['main']['humidity']
            visibilidade = (clima['visibility'])/1000
            return str(f"{cidade},{pais} \n \U0001F321 {temp}ºC\n {icon} {situacao}\n \U0001F4A8 {vento}m/s\n \U0001F4A6 {umidade}%\n \U0001F441 {visibilidade}km")
        except:
            return str("Nome da cidade incorreta")
        
    


    