# Armor Model
# V3.1
# 2023-08-09

def Armor(name=None, protections=None):
  """
  Factory function that returns an armor-piece with protection to a bodypart or multiple bodyparts in the form of a dictionary. Protections is given in percentage for each bodypart.
  
  Example:
  {
  'name': 'Kevlar helmet', 
  'protections': [('Head', 50), ('Neck', 30)]
  }
  """
  armor = {
    'name': name,
    'protections': protections or [],
  }
  return armor

def Protection(body_part, percentage):
  """
  Factory function that return a protection to a specific bodypart in the form of a tuple. The tuple contains the bodypart affected of the protection and the protection value given in percentage.

  Example:
  ('Head', 30)
  """
  assert percentage in range(100) # Checks that percentage is in a range of 0 to 99
  return body_part, percentage

available_items = { 
  Armor('Steel helmet', Protection('Head', 30)),
  Armor('Kevlar helmet', Protection('Head', 50), Protection('Neck', 30)),
  Armor('Flak vest', Protection('Torso', 50)),
  Armor('Interceptor body armor', Protection('Torso', 70), Protection('Groin', 30),        Protection('Neck', 10))
  }
