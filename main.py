# THIS IS A PROGRAM THAT JUST REPLICATES WHAT DOUGDOUG'S SOFTWARE DOES IN THIS STREAM
# https://youtu.be/xWvemlg1qYg (Squeex video)

#IMPORTANT - THIS PROGRAM MAY NOT FUNCTION WHEN PLAYING DOLPHIN EMULATOR ON KEYBOARD



import game_setup
from funcs import tts


SKIP_GREETING = True
GREETING = "The froggin' smash program is running. Ensure you are tabbed into your game before proceeding."
SETUP_KEY = '='

if not SKIP_GREETING:
    tts(GREETING) 


tts("Enter the number of games you will be playing")    
while True:
    num_games = input("Enter number of games: ")
    game_setup.run(int(num_games), SETUP_KEY)
