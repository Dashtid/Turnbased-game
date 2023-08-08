# Combat Model
# V3.1
# 2023-08-09
import character

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
  new_health = character.calculate_health(victim)
  print(f'Damage taken is: {victim_damage}!')
  print(f'New health is: {new_health}')
  return None

def attack_type(type_chosen):
  attack_types = {
    'Weak': 10,
    'Normal': 20,
    'Strong': 30,
    'Critical': 50,
  }
  selected_attack = attack_types[type_chosen]
  return selected_attack

def damage_taken(new_bodypart_health, bodypart_health): # TODO: Check all the bodyparts and calculate the damage taken to each. Make it more sofisticated. 
  damage = new_bodypart_health - bodypart_health
  return damage
  
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