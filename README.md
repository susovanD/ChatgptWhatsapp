![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Twilio](https://img.shields.io/badge/Twilio-F22F46?style=for-the-badge&logo=Twilio&logoColor=white)
![Whatsapp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)
# Introduction
This project contains a Flask application that uses OpenAI's GPT-3 language model to respond to user queries received through Twilio's API on Whatsapp.

[Image](https://github.com/susovanD/ChatgptWhatsapp/blob/main/ezgif.com-resize.gif)


## Prerequisites
Make sure that you have the following installed:

- Python 3.x
- Flask
- Twilio
- OpenAI

## Setup
1. Clone the repository to your local machine
2. Install the required packages using pip install -r requirements.txt
3. Add your OpenAI secret API key to the openai.api_key variable in the main.py file
4. Start the Flask application by running the command python main.py
5. Download and extract ngrok from this link based on your operating system
6. Start ngrok by navigating to the extracted ngrok folder in a separate terminal window and running the command ./ngrok http 5000
7. Copy the HTTPS forwarding URL generated by ngrok
8. Create a Twilio account and sign in to the Twilio Console
9. Navigate to the Messaging Services page and create a new Messaging Service
10. In the new Messaging Service, navigate to the Sandbox section and add the ngrok HTTPS URL to the "Request URL" field, with "/sms" appended to the end (e.g. https://abcd1234.ngrok.io/sms)
11. Save the changes and send a message to the Twilio number associated with the Messaging Service to test the application
Usage

## Usage
Once the setup is complete, the Flask application will be running and ngrok will be forwarding incoming messages to the application. The application will respond to user queries using OpenAI's GPT-3 language model. To modify the language model, refer to the OpenAI API documentation.

## License

[GNU](https://choosealicense.com/licenses/gpl-3.0/)

📫 How to reach me: [deysusovan93@gmail.com](mailto:deysusovan93@gmail.com)
