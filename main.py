from utils import chatgpt_response,generate_image
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

# Flask app initialization
app = Flask(__name__)

# Define a route for receiving incoming messages
@app.route('/sms', methods=['POST'])
def receive_message():
    # Get the incoming message and sender's phone number
    msg = request.form['Body'].lower()
#    sender_phone_number = request.form['From']
    user_name=request.form['ProfileName']
    responded = False
    print("Incoming message :",msg)
    # Create a Twilio MessagingResponse object
    resp = MessagingResponse()
    resp_msg = resp.message()
    if "hello" in msg.lower() and len(msg.split(" "))<5:
        resp_msg.body(f'Hey {user_name}!! Hope you are doing good. :)')
        responded =True
    elif "image" in msg:
        dalle_resp=generate_image(msg)
        resp_msg.body(f'Hey {user_name}!! Here is your image. :)')
        resp_msg.media(dalle_resp,caption=msg)
        responded=True
    else:  
        message_response=chatgpt_response(msg)
        resp_msg.body(message_response)
        responded = True
#        print("Response from ChatGPT : \n",resp)
    if not responded:
        resp_msg.body("We will get back online in some time. Appologize for the inconvenience.")
    # Send the response message to the sender
#        send_whatsapp_message(message_response,sender_phone_number)
    # Return an empty response
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True, port=5000)