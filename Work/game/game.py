# Game Model
# V3.1
# 2023-08-09

import random as rand
import character
import combat

def character_creation():
  """
  creates a character 
  TODO: add more here
  
  """
  character_name = input('Enter your characters name: ')
  character = Character(character_name)
  print(character) # TODO: Look more into this, right now it is printing the character which is wrong
  return character

def end_condition(character):
  # Checking if the character is still alive
  if combat.calculate_health(character) <= 0: 
    # If the character is dead, set end_condition = True and end the game
    return True 
  # Otherwise, set end_condition = False and continue the game  
  return False 

  ## Task 2
  ## Either find a chest and get a piece of armor OR become attacked
  ## Some % chance for a chest or attack
  ## If it's a chest what does it have?
  ## If it's an attack which attack

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
    player = character_creation() # Creating a character if none exists
  while ongoing_game:
      event(player) # Think this is not quite right...
    if end_condition(player): # Checks if the character is dead
      print("You have died") 
      ongoing_game = False # Ends the game
  return None # Return a status that the game is over
  
# Todo
# 1. Give different health values to body parts
# 2. Take armor into account when calculating damage
# 3. Add `damage_taken` to body parts

# Attack a character and print is the character dead or not?

# Example 1: 100 damage to the head wo. armor
# Example 2: 100 damage to the head w. armor

# 1.Attack 2.Summary 3.New turn