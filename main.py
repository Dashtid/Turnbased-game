# # Contents in this file are executed when we hit “Run”
from enum import Enum
import random as rand
import work as work

class AttackType(Enum):
  NORMAL = 25
  HEAVY = 50

def end_condition(character):
  # Checking if the character is still alive
  if work.calculate_health(character) <= 0:
    return True
  return False


  ## Task 2
  ## Either find a chest and get a piece of armor OR become attacked
  ## Some % chance for a chest or attack
  ## If it's a chest what does it have?
  ## If it's an attack which attack

def event(character):
  random_number = rand.random()
  if random_number >= 0.5:
    work.attack(character, 'Torso', AttackType.NORMAL)
    return None
  else:
    return None # Find a chest with an item?
    
    
# Just some hardcorded booleans for now.
ongoing_game = True
character = None


while ongoing_game:
  if character is None:
    work.character_creation() # Creating a character if none exists
  event(character) # Think this is not quite right
  if end_condition:
    print("You have died")
  
ongoing_game = False