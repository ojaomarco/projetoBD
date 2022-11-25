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
            
            
            
    


    