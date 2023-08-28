# Tests
# V3.1
# 2023-08-13

"""
Testing functions that test all functions in the game.
Works of a structure where a variable is set to True initially.
The variable is then evaluated together with a function.
If any part of the testing function fails, the entire module test fails.
Functions being tested are imported at the start of each module test.
All module tests return True for passed test and False for failed test.
"""

def body_ok():
  """
  Testing the funtions of the body module.
  Firstly, checks that a bodypart is created correctly
  Then, checks that the body is created correctly
  """
  from body import Bodypart, Body
  result = True
  result = result and Bodypart('Head') == {'name': 'Head', 'health': 10}
  result = result and Body() == [{'name': 'Head', 'health': 10}, {'name': 'Neck', 'health': 20}, {'name': 'Torso', 'health': 60}, {'name': 'Arms', 'health': 40}, {'name': 'Legs', 'health': 40}, {'name': 'Groin', 'health': 30}]
  return True
  
def character_ok():  
  """
  Testing the functions of the character module.
  Firstly, checks that a test character can be created.
  Then, checks that calculation of character health is correct.
  """
  from character import Character, calculate_health
  result = True
  test_character = Character('Test')
  result = result and test_character == {'name': 'Test', 'body': [{'name': 'Head', 'health': 10}, {'name': 'Neck', 'health': 20}, {'name': 'Torso', 'health': 60}, {'name': 'Arms', 'health': 40}, {'name': 'Legs', 'health': 40}, {'name': 'Groin', 'health': 30}], 'health': 200, 'armor' : []}
  result = result and calculate_health(test_character) == 200
  return True 

def armor_ok():
  """
  Testing the functions of the armor module. 
  Firstly, checks that protections are created correctly
  Then, creates a piece of armor with said protections and evaluates. 
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
  Testing the functions of the combat module.
  Firstly, checks that attack_type is selected correctly.
  Then, checks that attack is works correctly with that attack_type.
  """
  from character import Character
  from combat import attack, attack_type
  result = True
  test_character = Character('Test')
  normal_attack = attack_type('Normal')
  result = result and normal_attack == 20 # TODO: Could make a mocking seq.
  test_victim, test_damage  = attack(test_character, 'Torso', normal_attack)
  result = result and test_victim == ({'name': 'Test', 'body': [{'name': 'Head', 'health': 10}, {'name': 'Neck', 'health': 20}, {'name': 'Torso', 'health': 40}, {'name': 'Arms', 'health': 40}, {'name': 'Legs', 'health': 40}, {'name': 'Groin', 'health': 60}], 'health': 200, 'armor' : []})
  result = result and test_damage == 20
  return True 

def run_tests():
  """
  Runs all the module tests.
  If any module tests fail, the failed test is printed.
  Returns True for all tests passed and False if any test fails. 
  """
  tests = body_ok, character_ok, armor_ok, combat_ok
  for test_ok in tests:
    if not test_ok(): # TODO: Naming?
      print(f'Tests failed at the following test: {test_ok}')
      return False # Could skip this and maybe to a continue?
  print('All tests passed!')
  return True

run_tests()