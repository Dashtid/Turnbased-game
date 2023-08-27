# Tests
# V3.1
# 2023-08-13
 
def body_ok():
  """
  # Checking that a bodypart is created correctly
  # Checking that the body is created correctly
  """
  from body import Bodypart, Body
  result = True
  result = result and Bodypart('Head') == {'name': 'Head', 'health': 10}
  result = result and Body() == [{'name': 'Head', 'health': 10}, {'name': 'Neck', 'health': 20}, {'name': 'Torso', 'health': 60}, {'name': 'Arms', 'health': 40}, {'name': 'Legs', 'health': 40}, {'name': 'Groin', 'health': 30}]
  return True
  
def character_ok():  
  """
  # Checking that a test character can be created
  # Checking that calculate_health works
  """
  from character import Character, calculate_health
  result = True
  test_character = Character('Test')
  result = result and test_character == {'name': 'Test', 'body': [{'name': 'Head', 'health': 10}, {'name': 'Neck', 'health': 20}, {'name': 'Torso', 'health': 60}, {'name': 'Arms', 'health': 40}, {'name': 'Legs', 'health': 40}, {'name': 'Groin', 'health': 30}], 'health': 200, 'armor' : []}
  result = result and calculate_health(test_character) == 200
  return True 

def armor_ok():
  """
  # Checking that protections are created correctly
  # Checking that armor is created correctly
  """
  from armor import Protection, Armor
  result = True
  head_protection = Protection('Head', 30)
  result = result and head_protection == ('Head', 30)
  torso_protection = Protection('Torso', 50)
  result = result and torso_protection == ('Torso', 50)
  test_protections = [head_protection, torso_protection]
  test_armor = Armor('test_armor', test_protections)
  result = result and test_armor == {'name': 'test_armor', 'protections': [('Head', 30), ('Torso', 50)]}
  return True
  
def combat_ok():
  """
  # Checking that attack_type is selected correctly
  # Checking that attack is works correctly
  """
  from character import Character
  from combat import attack, attack_type
  result = True
  test_character = Character('Test')
  normal_attack = attack_type('Normal')
  result = result and normal_attack == 20
  test_victim, test_damage  = attack(test_character, 'Torso', normal_attack)
  result = result and test_victim == ({'name': 'Test', 'body': [{'name': 'Head', 'health': 10}, {'name': 'Neck', 'health': 20}, {'name': 'Torso', 'health': 40}, {'name': 'Arms', 'health': 40}, {'name': 'Legs', 'health': 40}, {'name': 'Groin', 'health': 60}], 'health': 200, 'armor' : []})
  result = result and test_damage == 20
  return True 

def run_tests():
  """
  """
  tests = body_ok, character_ok, armor_ok, combat_ok
  for test in tests:
    if test() == False: 
      print(f'Tests failed at the following test: {test}')
      return False
  print('All tests passed!')
  return True

run_tests()