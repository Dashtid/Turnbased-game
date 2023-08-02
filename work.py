from enum import Enum
# Armor System Modeling
# V2.1
# 2023-07-21

# Could be a class and have parts as parameters?
def Body():
  """
  Creates a body which is a list and contains bodyparts 
  which are individually dictionaries. Bodyparts are    
  created by the constructor function Bodypart().

  Example:
  [{'name': 'Head'},
  {'name':  'Neck'},
  {'name':  'Torso'},
  {'name':  'Arms'},
  {'name':  'Legs'},
  {'name':  'Groin'},]
  """
  body = [Bodypart('Head'),
          Bodypart('Neck'),          
          Bodypart('Torso'),
          Bodypart('Arms'),
          Bodypart('Legs'),
          Bodypart('Groin'),]
  return body


def Character(name=None, body=Body, health=100, items=None):
  character = {
    'name': name,
    'body': body(),
    'health': health,
    'items':  items or [],
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
  Creates an armor-piece with protection to a bodypart 
  or multiple bodyparts. Protections is given in 
  percentage for each bodypart.
  
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

def attack(victim, attack_type, bodypart):
  health = victim['body'][bodypart] 
  items = victim['items']
  for item in items:
    protections = item['proctetions']
    sum(protections for protection in protections)
  ## TODO:
  ## What about armor?
  ## Which bodypart are we attacking?
  
  
  new_health = health - attack_type
  victim['health'] = new_health

  print(f'New health is {new_health}!')
  return None