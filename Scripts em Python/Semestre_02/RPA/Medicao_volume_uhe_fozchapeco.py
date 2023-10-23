import requests
from bs4 import BeautifulSoup

apiToken = '6698525124:AAH6UO4jJQm-89gXBlSVetTQ1U4wtQPWbIw'
chatID = '1915158855'


def SendMessage(msg):
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': msg})
        print(response.text)
    except Exception as e:
        print(e)

def coletar_vazao_rio(url):
   
    response = requests.get(url)

    if response.status_code == 200:
        print("acesso concedido")
        soup = BeautifulSoup(response.text, 'html.parser')

        titulos_noticias = soup.find('div', class_='flex flex-col gap-6 md:gap-4')
        
        
        for titulo in titulos_noticias:
            
            contenido=titulo.text

           
            SendMessage(contenido)
    else:
        print(f"Erro ao acessar a página. Código de status: {response.status_code}")


url_site_fozchapeco = 'https://br.investing.com/commodities/brent-oil'

coletar_vazao_rio(url_site_fozchapeco)







