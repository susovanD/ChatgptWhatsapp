import openai
import requests
from io import BytesIO
from PIL import Image
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from api_key import key,account_sid,auth_token
# OpenAI API credentials
openai.api_key = key
dalle_model = 'image-alpha-001'  # DALL-E 2 API model
text_model='text-davinci-002'
# Twilio API credentials
account_sid = account_sid
auth_token =auth_token
twilio_client = Client(account_sid, auth_token)

# Sandbox WhatsApp number
sandbox_number = 'whatsapp:+14155238886'
#your_number = 'whatsapp:+919940420960'

# Generate an image using the DALL-E 2 API
def generate_image(prompt):
    response = openai.Image.create(
        model=dalle_model,
        prompt=prompt,
        size="1024x1024",
        response_format="url"
    )
#    image_data = requests.get(response.url).content
#    print(response)
    return response.data[0].url#Image.open(BytesIO(image_data))


def chatgpt_response(text):
    response = openai.Completion.create(
            engine=text_model,
            prompt=text,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
    return response.choices[0].text.strip()

# Send a message to your WhatsApp number
def send_whatsapp_message(message,your_number):
    message = twilio_client.messages.create(
        from_=sandbox_number,
        body=message,
        to=your_number,
    )
    return message.sid

# Prompt the user for input, generate an image using the DALL-E 2 API, and send the image to the user's WhatsApp number
#while True:
#    user_input = input('You: ')
#    if 'image' in user_input:
#        image = generate_image(user_input)
#        image.show()
#        send_whatsapp_message('Here is your image!')
#    else:
#        response = openai.Completion.create(
#            engine='text-davinci-002',
#            prompt=user_input,
#            max_tokens=1024,
#            n=1,
#            stop=None,
#            temperature=0.5,
#        )
#        send_whatsapp_message(response.choices[0].text.strip())
