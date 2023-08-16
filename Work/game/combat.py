# Combat Model
# V3.1
# 2023-08-09
import character
from utils import bodypart_list_to_dict

# Should probably be a part of character!

def attack(victim, bodypart, attack_type):
  """
  Performs an attack, of a certain strenght on a victims bodyparts, in three stages.
  1. Prepares the attack by gathering parameters from the victim.
  2. Executes the attack and takes into account protections that may apply.
     Calculates damage and updates bodypart health.
  3. Updates the player of outcome of the attack.

  Example:
  attack('victim', 'Neck', 'Weak') -> (
  'name': 'victim_name',
    'body': [
      {'name': 'Head',  'health': 10}, 
      {'name':  'Neck', 'health': 10}, 
      {'name':  ...,    'health': ...},
    ],
    'health': 190,
    'armor' : [],
  }, 10)
  """
  
  # -- Preparing the attack -- #
  victim_body = bodypart_list_to_dict(victim['body'])
  bodypart_name = victim_body[bodypart]['name']
  bodypart_health = victim_body[bodypart]['health']
  protection = calculate_protection(victim, bodypart)
  
  # -- Performing the attack -- #
  new_bodypart_health = bodypart_health - attack_type * (protection / 100) 
  victim_body[bodypart]['health'] = new_bodypart_health 

  # -- Updating user on the status of the character -- #
  victim_damage = bodypart_health - new_bodypart_health
  new_health = character.calculate_health(victim) 
  
  # Unsure as of how to do this :P
  attack_message(victim, victim_damage, bodypart_name, new_bodypart_health, new_health)
  return victim, victim_damage

def attack_type(type_chosen):
  attack_types = {
    'Weak': 10,
    'Normal': 20,
    'Strong': 30,
    'Critical': 50,
  }
  selected_attack = attack_types[type_chosen]
  return selected_attack

def calculate_protection(character, bodypart): 
  """
  Calculates the total protection that applies to a bodypart for a character.
  Goes through all armor piecies equipped.
  Summarizes the protections that applies for that bodypart.
  Caps protections at 99 %.

  Example:
    calculate_protection('character_name', 'Head') -> 80
  """
  total_protection = 0 
  for armor in character['armor']: 
    for name, protection in armor['protections']: 
      if name == bodypart: 
        total_protection += protection
  # Capping totalt_protection at 99%
  total_protection = min(total_protection, 99) 
  return total_protection

# Dunno...
def attack_message(victim, victim_damage, bodypart_name, new_bodypart_health, new_health):
  status = f'''Damage taken is: {victim_damage}!
  New health of {bodypart_name} is: {new_bodypart_health} hp
  New health of {victim['name']} is: {new_health} hp'''
  return print(status)