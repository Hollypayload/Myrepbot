from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
import datetime
import re

# Ganti dengan nilai yang sesuai dari akun Twilio Anda
TWILIO_ACCOUNT_SID = 'AC535dde1df278b29f715c7b67fd44aef3'
TWILIO_AUTH_TOKEN = 'ff9d6418052c1f46294fec316b8f2a9f'
TWILIO_PHONE_NUMBER = '+6283166565603'

app = Flask(__name__)
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_bot():
    incoming_message = request.values.get('Body', '').lower()
    response = MessagingResponse()

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%H:%M")
    formatted_date = current_time.strftime("%Y-%m-%d")

    name = detect_name(incoming_message)

    welcome_message = f"Halo {name}! Selamat datang di WhatsApp Bot. Saat ini jam {formatted_time} dan tanggal {formatted_date}. Silakan pilih salah satu opsi:"
    menu = response.message(welcome_message)
    menu.append(MessagingResponse().message("1. Opsi pertama"))
    menu.append(MessagingResponse().message("2. Opsi kedua"))
    menu.append(MessagingResponse().message("3. Opsi ketiga"))

    return str(response)

def detect_name(message):
    words = message.split()
    name = None
    for word in words:
        if word[0].isupper():
            name = word
            break
    return name if name else "Pengguna"

if __name__ == "__main__":
    app.run(debug=True)
