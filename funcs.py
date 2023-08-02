import playsound
import os
from gtts import gTTS
import pydirectinput as pd

SAVE_LOCATION = 'tts_files'
FILE_NAME = 'audio.mp3'

# converts provided string into mp3 file
def create_sound_file(text_to_convert: str, save_location: str, file_name: str):
    tts = gTTS(text_to_convert, tld='com.au', lang='en', slow=False)
    tts.save(save_location +'/'+ file_name)

# plays back specified mp3 file
def playback_mp3(file_location: str, file_name: str):
    playsound.playsound(file_location)
    
# creates a file and instantly plays it back, then deleting it
def tts(text_to_convert: str, save_location = SAVE_LOCATION, file_name = FILE_NAME):
    create_sound_file(text_to_convert, save_location, file_name)
    playback_mp3(save_location + '/' + file_name, file_name)
    os.remove(save_location + '/' + file_name)
    
def save_state(slot: int):
    func_key = 'f'+str(slot)
    pd.keyDown('shift')
    pd.keyDown(func_key)
    pd.keyUp(func_key)
    pd.keyUp('shift')

def load_state(slot: int):
    func_key = 'f'+str(slot)
    pd.keyDown(func_key)
    pd.keyUp(func_key)
    