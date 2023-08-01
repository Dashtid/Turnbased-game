from enum import Enum
# Armor System Modeling
# V2.1
# 2023-07-21

# Could be a class and have parts as parameters?
def Body():
  """
  Body parts:

  Example:
  [{'name': 'Head'},
  {'name':  'Neck'},
  {'name':  'Torso'},
  {'name':  'Arms'},
  {'name':  'Legs'},
  {'name':  'Groin'},
  {'name':  'etc.'},]
  """
  body = [Bodypart('Head'),
          Bodypart('Neck'),          
          Bodypart('Torso'),
          Bodypart('Arms'),
          Bodypart('Legs'),
          Bodypart('Groin'),]
  return body


def Character(name=None, body=Body, health=100):
  character = {
    'name': name,
    'body': body(),
    'health': health,
  }
  return character

def Bodypart(name=None, health=100):
  """
  In the simplest implementation we'll return the given    String as name inside a dict:

  assert Bodypart('Head') == {'name': 'Head'}
  """
  bodypart = {
    'name': name,
    'health': health,
  }
  return bodypart

def Armor(name=None, protections=None):
  """
  Armor-piece with protection to bodypart or parts,     
  given in percentage
  One armor-piece can protect multiple body parts
  
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
  Offers 30% protection to the Head:

  Example:
  ('Head', 30)
  """
  assert percentage in range(100)
  return body_part, percentage

# Attack a character and print is the character dead or not?

# Example 1: 100 damage to the head wo. armor
# Example 2: 100 damage to the head w. armor

# 1.Attack 2.Summary 3.New turn

class AttackType(Enum):
  NORMAL = 25
  HEAVY = 50

def attack(victim, attack_type):
  health = victim['health'] 

  ## What about armor?
  ## Which bodypart are we attacking?
  new_health = health - attack_type
  victim['health'] = new_health

  print(f'New health is {new_health}!')
  return None



# tom = Character("Tom")

# attack(tom, AttackType.Heavy)

def search_dictionaries(key, value, list_of_dictionaries):
  for element in list_of_dictionaries:
    if element[key] == value:
      return element
      
# value_we_looking_for = search_dictionaries('name', 'Torso', jones['body'])
# print(value_we_looking_for)
    # ##element for element in list_of_dictionaries if element[key] == value]`