import instaloader
from instaloader.exceptions import ConnectionException
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import SendMessageRequest
import os
from dotenv import load_dotenv

load_dotenv()

# Get api environment variables
tele_api_id = os.getenv('API_ID')
tele_api_hash = os.getenv("API_HASH")
session_name = "teleinstabot"
channel_id = os.getenv("CHANNEL_ID")


# create an instance of the Instaloader class
L = instaloader.Instaloader(filename_pattern='{profile}_reel')

# Create a telethon Client
print("Creating Telegram Client...")
client = TelegramClient(session_name, tele_api_id, tele_api_hash)
print("Telegram Client Created...")


# Starting the Client
client.start()
print*("Starting Telegram Client... \nWaiting to recieve message")


# Defining Message Format
message_format = """
Details for {}
Reel Owner: {}
Reel Caption : {}
Reel location : {}
Reel tagged_accounts : {}
"""

failed_message = """
Failed to get details for {}
Please Contant Admin or Try again later.

"""

# Creates an event handler that waits to recieve messages from telegram.

@client.on(events.NewMessage(chats=channel_id))
async def handler(event):
    # Get the message text from the event
    message_text = event.message.message
    print(message_text)

    # Check if the message contains an Instagram reel shortcode
    if 'instagram.com/reel/' in message_text:
        # Extract the shortcode from the message text
        shortcode = message_text.split('instagram.com/reel/')[1].split('/')[0]
        print(shortcode)

        # Get the post from Instagram using the shortcode
        try:
            post = instaloader.Post.from_shortcode(L.context, shortcode)

        except ConnectionException:
            await client(SendMessageRequest(channel_id, failed_message.format(message_text)))

        else:

        #Download the post
            print("Downloading media. please wait...")
            L.download_post(post, target='downloads')
            # send the media to the Telegram channel
            with open(f"downloads/{post.owner_username}_reel.mp4", 'rb') as f:
                if post.is_video:
                    print("Sending Video to Telegram. Please wait...")
                    sent_message = await client.send_file(channel_id, f,
                                           caption=message_format.format(message_text,
                                                                         post.owner_username,
                                                                         post.caption,
                                                                         post.location,
                                                                         post.tagged_users),
                                           supports_streaming=True,
                                           parse_mode='html',
                                           reply_to=None)
                    # Check if the message was succesfully sent 
                    if sent_message:
                        print("Succesfully sent message to Telegram!")
                    else:
                        print("Failed to send message to telegram.")


            # Delete the Downloaded Files
            dir_path = "downloads/"

            files = os.listdir(dir_path)

            for file in files:
                if file.startswith(f"{post.owner_username}_reel"):
                    os.remove(os.path.join(dir_path, file))

        # # Send the data back to the Telegram channel
        # await client(SendMessageRequest(channel_id, message_format.format(post.owner_username,
        #                                                                   post.caption,
        #                                                                   post.location,
        #                                                                   post.tagged_users)))


client.run_until_disconnected()
