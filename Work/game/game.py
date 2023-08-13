# Game Model
# V3.1
# 2023-08-13

import random as rand
import character
import combat

def create_character():
  """
  creates a character 
  TODO: add more here
  
  """
  character_name = input('Enter your characters name: ')
  character = character.Character(character_name)
  print(character) # TODO: Look more into this, right now it is printing the character which is wrong
  return character

def end_condition(character):
  # Checking if the character is still alive
  if combat.calculate_health(character) <= 0: 
    # If the character is dead, set end_condition = True and end the game
    return True 
  # Otherwise, set end_condition = False and continue the game  
  return False 

def event(character): # TODO: Find a better way of going about events
  random_number = rand.random()
  if random_number >= 0.5:
    combat.attack(character, 'Torso', 'Normal') # TODO: Change this to not be hardcoded. 
    return None # TODO: Maybe return tuple of character and status of what happened?
  else:
    return None # TODO: Find a chest with an item?

# IF testing then you can have hardcoded character, so create a testing mode

def run_game(test_mode = False):
  ongoing_game = True # Game is running
  if test_mode is True:
    player = character.Character('Test')
  else:
    player = create_character() # Creating a character if none exists
  while ongoing_game:
      event(player) # Think this is not quite right...
      if end_condition(player): # Checks if the character is dead
        print("You have died") 
        ongoing_game = False # Ends the game
  return None # Return a status that the game is over

# 1.Attack 2.Summary 3.New turn