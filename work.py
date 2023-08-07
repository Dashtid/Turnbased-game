from enum import Enum
# Armor System Modeling
# V3.1
# 2023-08-06

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


def Character(name=None, body=Body, health=100, armor=None):
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
    'health': health,
    'armor':  armor or [],
  }
  return character

def Bodypart(name=None):
  """
  Factory function that returns a bodypart in the form of a dictionary. 

  Example:
  {
  'name': 'Head'
  'health': 100
  }
  
  """
  health = bodypart_values[name] # Taking the appropriate health value for that bodypart
  bodypart = {
    'name': name,
    'health': health
  }
  return bodypart

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

class AttackType(Enum):
  NORMAL = 25
  HEAVY = 50

# Putting everything in a dictionary because I have no idea how to do it otherwise without something similar to AttackType above. They all add to 200. 
bodypart_values = {
  'Head': 20,
  'Neck': 20,
  'Torso': 60,
  'Arms': 40,
  'Legs': 40,
  'Groin': 20,
}



def attack(victim, bodypart, attack_type):

  # Preparing the attack
  victim_body = bodypart_list_to_dict(victim['body']) # Converts the bodypart list into a dictionary
  bodypart_health = victim_body[bodypart]['health'] # Fetches the current health of a bodypart, before the attack
  protection = bodypart_protection(victim, bodypart) # Fetches the protections that apply to that bodypart
  
  # Performing the attack
  new_bodypart_health = bodypart_health - attack_type * (protection / 100) # Changes protections value to a multiplier of the attack and then applies the attack
  victim_body[bodypart]['health'] = new_bodypart_health # Updates the victims bodypart with the new health value after the attack

  # Updating user on the status of the character after the attack
  victim_damage = damage_taken(new_bodypart_health, bodypart_health)
  new_health = calculate_health(victim)
  print(f'Damage taken is {victim_damage}!')
  print(f'New health is {new_health}!')
  return None

def damage_taken(new_bodypart_health, bodypart_health):
  damage = new_bodypart_health - bodypart_health
  return damage

def character_creation():
  character_name = input('Enter your characters name: ')
  character = Character(character_name)
  print(character)
  return character
  
def bodypart_list_to_dict(bodypart_list):
  """
  Function that takes in a list of bodyparts and returns a dictionary where the keys are names of bodyparts and the values are dictionaries representing that bodypart. Effectively doing a conversion of the bodypart list to a bodypart dictonary. Thus allowing for easier access to bodyparts in calculations.  
  """
  bodypart_dict = {}
  for bodypart in bodypart_list:
    bodypart_dict[bodypart['name']] = bodypart # Setting the key in the dictonary to be the name of the bodypart and the value to be the dictionary of the bodypart
  return bodypart_dict  

def calculate_health(character):
  """
  Function that goes through all bodyparts of a character and returns the characters overall health as a single value.
  """
  health = sum(bodypart['health'] for bodypart in character['body']) # Goes through all bodyparts and sums their health
  return health

def bodypart_protection(character, bodypart): 
  total_protection = 0 # Intialiazes the protections value
  # Summarization of all protections that apply for that bodypart
  for armor in character['armor']: # Goes through all the armor items the character has
    for name, protection in armor['protections']: # Retrieves the name and protections for all the armor pieces
      if name == bodypart: # If the name of a protection is the same as the bodypart it is being compared to, then add that protections to the total
        total_protection += protection
  # Cap protection at 99%
  if total_protection > 99:
    total_protection = min(total_protection, 99) # Ensures that totalt_protection cannot be higher than 99.
  return total_protection

# Todo
# 1. Give different health values to body parts
# 2. Take armor into account when calculating damage
# 3. Add `damage_taken` to body parts

# Attack a character and print is the character dead or not?

# Example 1: 100 damage to the head wo. armor
# Example 2: 100 damage to the head w. armor

# 1.Attack 2.Summary 3.New turn