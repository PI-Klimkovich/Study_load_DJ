from .TOKEN import token, chat_id
import requests


# def telegram_bot_send(token, chat_id, message): # Вариант с передачей в функцию токена
def telegram_bot_send(message):
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={message}'
    response = requests.get(url)
    return response.json()


# response = telegram_bot_send(token, chat_id, "Hello world")  # Вариант с передачей в функцию токена

# response = telegram_bot_send("Hello world")
# print(response)
