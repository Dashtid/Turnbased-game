# Game Model
# V3.1
# 2023-08-09

import random as rand
import character
import combat

def end_condition(character):
  if game.calculate_health(character) <= 0: # Checking if the character is still alive
    return True # If the character is dead, set end_condition = True and end the game
  return False # Otherwise, continue the game

  ## Task 2
  ## Either find a chest and get a piece of armor OR become attacked
  ## Some % chance for a chest or attack
  ## If it's a chest what does it have?
  ## If it's an attack which attack

def event(character): # TODO: Find a better way of going about events
  random_number = rand.random()
  if random_number >= 0.5:
    combat.attack(character, 'Torso', 'Normal') # TODO: Change this to not be hardcoded. 
    return None
  else:
    return None # Find a chest with an item?
    
def run_game():
  ongoing_game = True # Game is running 
  character = None    # No character exists in the beggining of the game
  while ongoing_game:
    if character is None:
      character.character_creation() # Creating a character if none exists
    if end_condition(character): # Checks if the character is dead
      print("You have died") 
      ongoing_game = False # Ends the game
    event(character) # Think this is not quite right
  return None
  
# Todo
# 1. Give different health values to body parts
# 2. Take armor into account when calculating damage
# 3. Add `damage_taken` to body parts

# Attack a character and print is the character dead or not?

# Example 1: 100 damage to the head wo. armor
# Example 2: 100 damage to the head w. armor

# 1.Attack 2.Summary 3.New turn