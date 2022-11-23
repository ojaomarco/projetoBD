import requests
import json 

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
                

