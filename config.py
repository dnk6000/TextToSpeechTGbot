from dotenv import load_dotenv
import os

load_dotenv()

elevenlabs_api_key = os.getenv('ELEVENLABS_API_KEY')

bot_token = os.getenv('BOT_TOKEN')

proxy = os.getenv('PROXY')
