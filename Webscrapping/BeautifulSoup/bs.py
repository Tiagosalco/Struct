from bs4 import BeautifulSoup
import requests

website='https://subslikescript.com/movie/Titanic-120338'
result=requests.get(website)
content=result.text

soup= BeautifulSoup(content,'lxml')

box=soup.find('article', class_='main-article')

title=box.find('h1').get_text()
#print(title)

transcript=soup.find('div', class_='full-script').get_text(strip='true',separator=' ')
#print(transcript)


# Crear archivo txt con el texto extraido de la pagina 
with open('Webscrapping/BeautifulSoup/titanic.txt','w', encoding='utf-8') as file: #El encoding es para que no se trabe solo nidea
    file.write(transcript)
    

