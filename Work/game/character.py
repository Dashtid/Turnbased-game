# Character Model
# V3.1
# 2023-08-09
import body as body_model

def calculate_health(character):
  """
  Function that sums the health of all bodyparts in a character.
  Returns the characters overall health as a single value.
  
  Example:
  calculate_health('test_character') -> 200
  """
  health = sum(bodypart['health'] for bodypart in character['body']) 
  return health

def Character(name, body=body_model.Body, armor=None):
  """
  Constructor function that return a dictionary represtenting a character. 
  Both body and armor keys contain a list. 
  Body is a list from the Constructor function Body(). 
  Health is the sum of the health of all bodyparts.
  
  Example: 
  Character('character_name') -> {
    'name': 'character_name',
    'body': [
      {'name': 'Head', 'health': 10}, 
      {'name':  'Neck', 'health': 20}, 
      {'name':  ..., 'health': ...},
    ],
    'health': 200,
    'armor' : [...],
  }
  """
  character = {
    'name': name,
    'body': body(),
    'health': None,
    'armor':  armor or [],
  }
  # Attach health now that `character` exists
  character['health'] = calculate_health(character)
  return character

# ----

# Contributing a bit of code
# Mainly shows how to:
# 
# - Break functionality into small functions
# - Return objects from functions
# - Weave together public and _private functions

# Seems reasonable
# import health, is_alive from character
# Not a good idea
# import _killed from character

# import character
# This looks good
# character.health()
# Don't do this
# character._killed()

def health(character):
  """
  Calculates current health of character

  Health  : Total hitpoints, might change when leveling up
  Damaged : Damage sustained since last full health, changes when hurt
  """
  health = character['health'] - character['damaged']
  return health

def is_dead(character):
  """
  Once a character has died they're permanently dead
  """
  has_died = character.get('died') # might be `None`
  return has_died and has_died() or False

def is_alive(character):
  """
  A character is alive when:

  - They haven't died
  - Their health is above zero
  """
  alive = not is_dead(character) and health(character) > 0
  # Watch the difference:
  # alive = health(character) > 0 and not is_dead(character) 
  # Boolean operators short-circuit, so `is_dead(character)` never runs
  # Would allow us to revive a dead character by healing ;)
  return alive

def _hurt(character, damaged):
  """
  Hurting a character will damage, and might kill them
  """
  character, damaged = _damaged(character, damaged)
  if not is_alive(character):
    character = killed(character)
  return character, damaged

def _killed(character):
  """
  Attach function to mark a character's death
  """
  def died():
    return True
  character['died']: died
  return character

def _damaged(character, damaged):
  """
  Damaging a character increases their damage
  """
  character['damaged'] += damaged
  return character, damaged

def _healed(character, healed):
  """
  Damaging a character decreases their damage, down to zero
  """
  character['damaged'] = max(0, character['damaged'] - healed)
  return character, healed