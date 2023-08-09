# Character Model
# V3.1
# 2023-08-09

def character_creation():
  character_name = input('Enter your characters name: ')
  character = Character(character_name)
  print(character) # TODO: Look more into this, right now it is printing the character which is wrong
  return character

def Body():
  """
  Factory function that a list and contains bodyparts which individually are dictionaries. Bodyparts are created by the factory function Bodypart(). There are 6 bodyparts that constitute a body and are given in the example below. 

  Example:
  [
  {'name': 'Head'},
  {'name':  'Neck'},
  {'name':  'Torso'},
  {'name':  'Arms'},
  {'name':  'Legs'},
  {'name':  'Groin'},
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

def Character(name, body=Body, health=calculate_health, armor=None):
  """
  Constructor function that return a dictionary represtenting a character. Both body and armor keys contain a list where body is a list from the Constructor function Body(). 

  Example: 
  {
  'name': 'David'
  'body': [{'name': 'Head'}, {'name':  'Neck'}, {'name':  'Torso'}, {'name':  'Arms'}, {'name':  'Legs'}, {'name':  'Groin'},]
  'health': 100
  'armor' = []
  }
  """
  character = {
    'name': name,
    'body': body(),
    'health': health(),
    'armor':  armor or [],
  }
  return character

def Bodypart(name):
  """
  Factory function that returns a bodypart in the form of a dictionary. 

  Example:
  {
  'name': 'Head'
  'health': 100
  }
  """
  # Dictionary containing the default hitpoint values for any starting character. They all add to 200. 
  starting_hitpoints = {
  'Head': 10,
  'Neck': 20,
  'Torso': 60,
  'Arms': 40,
  'Legs': 40,
  'Groin': 30,
  }
  health = bodypart_values[name] # Taking the appropriate health value for that bodypart
  bodypart = {
    'name': name,
    'health': health
  }
  return bodypart

def calculate_health(character):
  """
  Function that goes through all bodyparts of a character and returns the characters overall health as a single value.
  """
  health = sum(bodypart['health'] for bodypart in character['body']) # Goes through all bodyparts and sums their health
  return health