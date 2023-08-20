# Tests
# V3.1
# 2023-08-13

import body, character, armor, combat

def body_tests():
  # Checking that a bodypart is created correctly
  assert body.Bodypart('Head') == {'name': 'Head', 'health': 10}
  # Checking that the body is created correctly
  assert body.Body() == [{'name': 'Head', 'health': 10}, {'name': 'Neck', 'health': 20}, {'name': 'Torso', 'health': 60}, {'name': 'Arms', 'health': 40}, {'name': 'Legs', 'health': 40}, {'name': 'Groin', 'health': 30}]
  result_body = 'Body tests passed'
  return result_body
  
def character_tests():  
  # Checking that a test character can be created
  test_character = character.Character('Test')
  assert test_character == {'name': 'Test', 'body': [{'name': 'Head', 'health': 10}, {'name': 'Neck', 'health': 20}, {'name': 'Torso', 'health': 60}, {'name': 'Arms', 'health': 40}, {'name': 'Legs', 'health': 40}, {'name': 'Groin', 'health': 30}], 'health': 200, 'armor' : []}
  # Checking that calculate_health works
  assert character.calculate_health(test_character) == 200
  result_character = 'Character tests passed'
  return result_character

def armor_tests():  
  # Checking that protections are created correctly
  head_protection = armor.Protection('Head', 30)
  assert head_protection == ('Head', 30)
  torso_protection = armor.Protection('Torso', 50)
  assert torso_protection == ('Torso', 50)
  # Checking that armor is created correctly
  test_protections = [head_protection, torso_protection]
  test_armor = armor.Armor('test_armor', test_protections)
  assert test_armor == {'name': 'test_armor', 'protections': [('Head', 30), ('Torso', 50)]}
  result_armor = 'Armor tests passed'
  return result_armor
  
def combat_tests():
  # Checking that attack_type is selected correctly
  test_character = character.Character('Test') # DRY?
  normal_attack = combat.attack_type('Normal')
  assert normal_attack == 20
  # Checking that attack is works correctly
  test_victim, test_damage  = combat.attack(test_character, 'Torso', normal_attack)
  assert test_victim, test_damage == ({'name': 'Test', 'body': [{'name': 'Head', 'health': 10}, {'name': 'Neck', 'health': 20}, {'name': 'Torso', 'health': 40}, {'name': 'Arms', 'health': 40}, {'name': 'Legs', 'health': 40}, {'name': 'Groin', 'health': 60}], 'health': 200, 'armor' : []}, 20)
  result_combat = 'Combat tests passed'
  return result_combat 

def run_tests():
  print(body_tests())
  print(character_tests())
  print(armor_tests())
  print(combat_tests())
  result_tests = 'All tests passed'
  return result_tests

run_tests()