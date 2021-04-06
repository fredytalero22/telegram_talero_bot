import requests  
import os
from flask import Flask, request

BOT_URL = f'https://api.telegram.org/bot{os.environ["BOT_KEY"]}/'  # <-- add your telegram token as environment variable


app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():  
    data = request.json
    
    print(data)  # Comment to hide what Telegram is sending you
    
    if "message" in data:
        chat_id = data['message']['chat']['id']
        message = data['message']['text']
        json_data = {
            "chat_id": chat_id,
            "text": message,
        }

        message_url = BOT_URL + 'sendMessage'
    elif "callback_query" in data:
        json_data = {
            "callback_query_id": data["callback_query"]["id"],
            "text": "Mi primer answer callback query",
        }

        message_url = BOT_URL + 'answerCallbackQuery'

    requests.post(message_url, json=json_data)

    return ''


if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
