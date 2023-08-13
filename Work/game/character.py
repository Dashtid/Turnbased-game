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

