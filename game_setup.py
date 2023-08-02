from funcs import tts, save_state, load_state
import keyboard
import random
import time

DEBUG = 0

# sets up the savestates based on number of games chosen
def run(num_games, SETUP_KEY = 'spacebar'):
    if num_games == 0:
        tts("0 games selected.")
        return
    
    if num_games > 8:
        tts("Must not be more than 8 games.")
        return
    
    tts("Load character select screen, then press " + SETUP_KEY)
    keyboard.wait(SETUP_KEY)
    save_state(1)
    
    curr_game = 2
    while(curr_game <= num_games):
        tts("Select stage and press " + SETUP_KEY)
        keyboard.wait(SETUP_KEY)
        save_state(curr_game)
        load_state(1)
        curr_game+=1
    tts("Final. Select stage and press " + SETUP_KEY + ' to begin playing')
    keyboard.wait(SETUP_KEY)
    save_state(1)
    
    begin_game(num_games, SETUP_KEY)
    

def get_rand_slot(curr_slot: int, live_games: list):
    # get random slot
    rand_slot = 0
    if len(live_games) == 1:
        return 0
    while True:
        print("Live games list: ", live_games[:])
        rand_slot = random.randint(0, len(live_games)-1)
        
        if live_games[rand_slot] == curr_slot:
            continue
        
        if(DEBUG):
            print("Swapping slot from %s -> %s \n" % (curr_slot, live_games[rand_slot]))    
        break
        
        
    return live_games[rand_slot]

# starts the game loading random save states
def begin_game(num_games, SETUP_KEY, MIN_TIME = 6, MAX_TIME = 25):
    live_games = [item for item in range(1, num_games+1)]
    print(live_games[:])
    print("Game started")
    tts("Game started")
    completed_games = 0
    rand_slot = 0
    curr_slot = 1
    
    # run while the user hasn't won
    while(completed_games < num_games):
        if DEBUG:
            print("MAX GAMES | ROUNDS COMPLETED : %s | %s" % (num_games, completed_games))
            print("Current Slot: ", curr_slot)
        start_time = time.time()
        end_time = time.time()
        round_completed = False
        rand_interval = random.randint(MIN_TIME, MAX_TIME+1)
        if DEBUG:
            print("RANDOM INTERVAL SET: ", rand_interval)
        
        
        # check if interval has gone long enough
        while((end_time - start_time) < rand_interval):
            # flag a round has been completed
            if(keyboard.is_pressed(SETUP_KEY)):
                if DEBUG:
                    print("LIVE GAMES LIST: ", live_games[:])
                    print("REMOVING " + str(curr_slot) + ' FROM LIST')
                round_completed = True    
                break
                
            end_time = time.time()
        
        
        
            
        
        # Save current state and load new one
        rand_slot = get_rand_slot(curr_slot, live_games)
        if(num_games - completed_games > 1):
            save_state(curr_slot)
            load_state(rand_slot)
            
        prev_slot = curr_slot
        curr_slot = rand_slot
        
        # manage round/game completions
        if round_completed:
            if(num_games - completed_games == 1):
                break
            tts("Round completed")
            if DEBUG:
                print("Finished round: ", prev_slot)
            index_to_pop = live_games.index(int(prev_slot))
            live_games.pop(index_to_pop)
            completed_games += 1
            round_completed = False
        
        print("\n")
    
    tts("Game completed. Congratulations.")
        
        
    