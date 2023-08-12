# Armor Model
# V3.1
# 2023-08-09
import utils

def Armor(name, protections):
  """
  Factory function that returns an armor-piece with protection.
  The protection applies to a bodypart or multiple bodyparts.
  Protections is given as a list of tuples in the form of ('name', percentage_value).
  
  Example:
  Armor() -> {
    'name': 'armor_name', 
    'protections': [
      ('Head', 50),
      ('Neck', 30),
      (..., ...)
    ]
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
  # Checks that percentage is in a range of 0 to 99
  assert percentage in range(100) 
  return body_part, percentage  

def generate_available_items():
  available_items = [ 
  Armor('Steel helmet', [Protection('Head', 30)]),
  Armor('Kevlar helmet', [Protection('Head', 50), Protection('Neck', 30)]),
  Armor('Flak vest', [Protection('Torso', 50)]),
  Armor('Interceptor body armor', [Protection('Torso', 70), Protection('Groin', 30), Protection('Neck', 10)])
  ] # There must be a way of doing this better? 
  available_items_dict= utils.list_to_dict(available_items)
  return available_items_dict
