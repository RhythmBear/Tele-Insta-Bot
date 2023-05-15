# Tele-Insta-Bot
To run this bot you will need a telagram api_id and api_hash

To obtain an api_id and api_hash for Telegram, you will need to follow these steps:

- Open the Telegram website (https://telegram.org/) in your browser and sign in to your account.
- Go to the Telegram API development tools page (https://my.telegram.org/apps).
- Click on the "Create a new application" button.
- Fill in the required details, including the name of your application, a short description, the platform you will be using the API on, and the website URL of your application. You can leave the other fields blank.
- Click on the "Create Application" button.
- You will be redirected to a page with your api_id and api_hash. Save these values somewhere safe, as you will need them later to access the Telegram API.
- Please note that you will need to have a valid phone number registered with Telegram to create an API application.

### Once That has been created Please pass in the following as env Variables
- API_ID= Telegram api_id
- API_HASH= Telegram Api-Hash
- TELEGRAM_TOKEN= Telegram token.
- CHANNEL_ID= Id to the public telegram channel where the reels will be sent.

Add the telegram bot to the telegram channel and you are good to go.

TO start Bot,
  - python main.py 
