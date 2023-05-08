import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = '5814224860:AAEaoNbdJazhMojAxwv9NzFCVEfeTogsAzw'
    bot_chatID = '5469359631'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

test = telegram_bot_sendtext("Testing Telegram bot")
print(test)

# ID = 5469359631
# API = 5814224860:AAEaoNbdJazhMojAxwv9NzFCVEfeTogsAzw
# Username = MercadoCarcel_bot
# botardo
# https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e
#de aca podria agregar que se haga todos los dias a tal hora