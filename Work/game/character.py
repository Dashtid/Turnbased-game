# Character Model
# V3.1
# 2023-08-09

# TODO: Create a body file!

def calculate_health(character):
  """
  Function that sums the health of all bodyparts in a character.
  Returns the characters overall health as a single value.
  
  Example:
  calculate_health('test_character') -> 200
  """
  health = sum(bodypart['health'] for bodypart in character['body']) 
  return health

def Body():
  """
  Factory function that a list and contains bodyparts which individually are dictionaries.
  Bodyparts are created by the factory function Bodypart().
  There are 6 bodyparts that constitute a body and are given in the example below. 

  Example:
  Body() -> [
    {'name': 'Head', 'health': 10},
    {'name': 'Torso', health': 20},
    {'name': ..., 'health': ...},
  ] 
  """
  body = [
          Bodypart('Head'),
          Bodypart('Neck'),          
          Bodypart('Torso'),
          Bodypart('Arms'),
          Bodypart('Legs'),
          Bodypart('Groin'),
         ]
  return body

def Character(name, body=Body, armor=None):
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

def Bodypart(name):
  """
  Factory function that returns a bodypart in the form of a dictionary. 
  Each bodypart has a name and a health value.
  
  Example:
  Bodypart('Head') -> {
    'name': 'Head',
    'health': 10,
  }
  """
  # Default hitpoint values for any starting character. They all add to 200. 
  starting_hitpoints = {
    'Head': 10,
    'Neck': 20,
    'Torso': 60,
    'Arms': 40,
    'Legs': 40,
    'Groin': 30,
  }
  # Taking the appropriate health value for that bodypart
  health = starting_hitpoints[name] 
  bodypart = {
    'name': name,
    'health': health
  }
  return bodypart
