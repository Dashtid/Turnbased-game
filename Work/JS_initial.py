# Armor System Modeling
# V1.4
# 2023-07-20

# Armor System for Tactics Game
# 
# Example Modeling Exercise

def Character(name=None, body_parts=None):
  body_parts = body_parts or []
  character = {
    'name': name,
    'body': body_parts,
  }
  return character

def BodyPart(name, strength, armor=None):
  body_part = {
    'name': name,
    'strength': strength,
    'armor': armor or [],
  }
  assert body_part.strength > 0
  return body_part

def Armor(name, protections=None):
  armor = {
    'name': name,
    'protections': protections or [],
  }
  return armor

# Taking armor into account
def attacked(character, attack):
  # “Attacked left arm for 5 damage”
  body_part, damage = attack
  # Damage gets absorbed by armor
  damage -= blocked(body_part, damage)
  # Remaining damage impacts the body part
  body_part = hurt(body_part, damage)

# Armor absorbs damage
def blocked(body_part, damage):
  # Armor possibly takes damage here
  #Not implemented#
  pass
  # “Blocked 2 damage”
  blocked = damage * armor_for(body_part)
  return blocked

# After armor
def hurt(body_part, damage):
  """
  “Hurt for 3 damage”
  
  hurt(body_part, 3)
  """
  # Decrement strength of body part

  body_part.strength -= damage
  return body_part

def armor_for(body_part):
  """
  Protects head for 50%:

  [('Helmet', 30), ('Glasses', 20)]
  """
  total_protection = sum( protection for armor, protection in body_part.armor )
  
  # Normalize
  # total_protection = _clamp(sum( protection for armor, protection in body_part.armor ))
  
  # Imperative
  if total_protection > 99:
    total_protection = 99
  
  # Functional
  total_protection = min(total_protection, 99)

def _clamp(val, top = (10 ** 2) - 1, bottom = 0):
  # clamped = min(val, top)
  # if bottom is not None:
  #   clamped = max(clamped, bottom)
  # Idiomatic
  clamped = min(max(val, bottom or val), top)
  return clamped