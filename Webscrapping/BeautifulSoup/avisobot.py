import requests
from mlconbotardo import precioactual
from mlconbotardo import preciodeseado


def telegram_bot_sendtext(bot_message):
    
    bot_token = '5814224860:AAEaoNbdJazhMojAxwv9NzFCVEfeTogsAzw'
    bot_chatID = '5469359631'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    
if precioactual < preciodeseado:
    test = telegram_bot_sendtext(f" ATENCION! Hay OFERTA, bajo el precio Esta en: {'$'+str(precioactual)}\n Enlace: https://listado.mercadolibre.com.ar/filamentos-pla")
else:
    test = telegram_bot_sendtext(f"Esta mas caro, esta en: {'$'+str(precioactual)}")


