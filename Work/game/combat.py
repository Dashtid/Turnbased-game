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
  # Converts the bodypart list into a dictionary
  victim_body = bodypart_list_to_dict(victim['body'])
  bodypart_name = victim_body[bodypart]['name']
  bodypart_health = victim_body[bodypart]['health']
  # Calculates protections that apply to that bodypart
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
  total_protection = 0 # Initialiazes the protections value
  # -- Summarization of all protections that apply for that bodypart -- #
  # Goes through all the armor items the character has
  for armor in character['armor']: 
    # Retrieves the name and protections for all the armor pieces
    for name, protection in armor['protections']: 
      # If the name of a protection is the same as the bodypart it is being compared to, then add that protections to the total
      if name == bodypart: 
        total_protection += protection
  # Ensures that totalt_protection cannot be higher than 99%
  total_protection = min(total_protection, 99) 
  return total_protection

# Dunno...
def attack_message(victim, victim_damage, bodypart_name, new_bodypart_health, new_health):
  status = f'''Damage taken is: {victim_damage}!
  New health of {bodypart_name} is: {new_bodypart_health} hp
  New health of {victim['name']} is: {new_health} hp'''
  return status