from bs4 import BeautifulSoup
import requests
import time
import webbrowser

#i=input('Quieres acceder a la Web?: si o no = ')
#if i=='si':
#    print('accediendo a la web')
#    time.sleep(0)
#    pag="https://listado.mercadolibre.com.ar/filamentos-pla"
#    
#    webbrowser.open_new_tab(pag)

url=requests.get("https://listado.mercadolibre.com.ar/filamentos-pla")
soup= BeautifulSoup(url.content, "html.parser")
resultado=soup.find('span',{'class':'price-tag-fraction'})
precioactual_text=resultado.text

precioactual=float(precioactual_text)
print(precioactual)

preciodeseado=3.000

