# Body Model
# V3.1
# 2023-08-13

def Body():
  """
  Factory function that a list and contains bodyparts which individually are dictionaries.
  Bodyparts are created by the factory function Bodypart().
  There are 6 bodyparts that constitute a body.

  Example:
  Body() -> [
    {'name': 'Head', 'health': 10},
    {'name': 'Torso', health': 20},
    {'name': '...', 'health': ...},
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