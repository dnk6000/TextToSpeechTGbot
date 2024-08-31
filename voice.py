from elevenlabs import save
from elevenlabs.client import ElevenLabs
import config
import httpx

client = ElevenLabs(
    api_key=config.elevenlabs_api_key,
    httpx_client=httpx.Client(proxy=config.proxy)
)

def get_all_voices():
    voices = client.voices.get_all()
    return [{'name': voice.name, 'id': voice.voice_id} for voice in voices.voices]

def generate_audio(text: str, voice: str):
    audio = client.generate(
        text=text,
        voice=voice,
        model="eleven_multilingual_v2"
    )
    name = "audio.mp3"
    save(audio, name)
    return name