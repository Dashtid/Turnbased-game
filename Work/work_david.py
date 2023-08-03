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


def Character(name=None, body=Body, health=100, armor=None):
  character = {
    'name': name,
    'body': body(),
    'health': health,
    'armor':  armor or [],
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
  Factory function that returns an armor-piece with protection to a bodypart 
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
  Factory function that return a protection to a specific bodypart in the       form of a tuple. The tuple contains the bodypart affected of the protection   and the protection value given in percentage.

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

def attack(victim, bodypart, attack_type):
  # health = victim['body'][bodypart] 
  # armor = victim['armor']
  # for item in armor:
  #  protections = item['protections']
  #  sum(protections for protection in protections)

  #new_health = health - attack_type
  #victim['health'] = new_health
  
  ## TODO:
  ## What about armor?
  ## Which bodypart are we attacking?
  
  victim_body = list_to_dict(victim['body'])
  bodypart_health = victim_body[bodypart]['health']
  protection = bodypart_protection(victim, bodypart)
  new_bodypart_health = bodypart_health - attack_type * (protection / 100)
  victim_body[bodypart]['health'] = new_bodypart_health
  new_health = calculate_health(victim)
  
  print(f'New health is {new_health}!')
  return None

def list_to_dict(list):
  dict = {}
  for item in list:
    dict[item['name']] = item
  return dict      

def calculate_health(character):
  health = 0
  for bodypart in character['body']: 
    health += bodypart['health']
  # health /= len(character['body'])
  return health

# Functional
# def calculate_health(character):
#   health = sum(bodypart['health'] for bodypart in character['body'])
#   return health

def bodypart_protection(character, bodypart): 
  total_protection = 0
  for armor in character['armor']:
    for name, protection in armor['protections']:
      if name == bodypart:
        total_protection += protection
  # Cap protection at 99%
  # total_protection = min(total_protection, 99)
  if total_protection > 99:
    total_protection = 99
  return total_protection

# Todo
# 1. Give different health values to body parts
# 2. Take armor into account when calculating damage
# 3. Add `damage_taken` to body parts