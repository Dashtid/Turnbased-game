# Game Model
# V3.1
# 2023-08-13

import random as rand
import character, combat, tests

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
  """
  # Checking if the character is still alive
  # If the character is dead, set end_condition = True and end the game
  # Otherwise, set end_condition = False and continue the game
  """
  if combat.calculate_health(character) <= 0: 
    return True  
  return False 

def run_event(character): # TODO: Find a better way of going about events
  random_number = rand.random()
  if random_number >= 0.5:
    combat.attack(character, 'Torso', 'Normal') # TODO: Change this to not be hardcoded. 
    return None # TODO: Maybe return tuple of character and status of what happened?
  else:
    return None # TODO: Find a chest with an item?


def run_game(test_mode = False):
  """
  """
  ongoing_game = True 
  if test_mode is False:
    player = create_character() 
    while ongoing_game:
      run_event(player) # Think this is not quite right...
      if end_condition(player):
        print("You have died") 
        ongoing_game = False # Ends the game
  else:
    tests.all_tests() 
  return None

# 1.Attack 2.Summary 3.New turn

# ----

# Contributing a bit of code

def setup_characters(level=None):
  """
  Constructs characters for a given level:

  - Player
  - Player's support
  - Enemies
  - (Other NPCs)
  """
  _named = lambda dicts : { _dict['name']: _dict for _dict in dicts }
  level['characters'] = {
    'player': ( player := Character() ),
    'support': ( support := [
      Character(),
      Character(),
      Character(...),
    ] ),
    'team': ( team := lambda : _named(support.append(player)) ),
    'enemies': ( enemies := [Character(), Character()] ),
    'npc': ( npc := lambda : _named() ),
    'characters': lambda : npc().append(team),
  }
  return level