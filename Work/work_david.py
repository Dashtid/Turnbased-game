# Armor System Modeling
# V3.1
# 2023-08-08

# Todo
# 1. Give different health values to body parts
# 2. Take armor into account when calculating damage
# 3. Add `damage_taken` to body parts

# Attack a character and print is the character dead or not?

# Example 1: 100 damage to the head wo. armor
# Example 2: 100 damage to the head w. armor

# 1.Attack 2.Summary 3.New turn

# A little bit unsure as of how to go about this
import unittest # https://docs.python.org/3/library/unittest.html
import game.character as character_model

class TestCharacter(unittest.TestCase):

  def test_character(self):
    test_character = character_model.Character('Test')
    self.assertEqual(test_character, {'name': 'David', 'body': [{'name': 'Head', 'health': 10}, {'name':  'Neck', 'health': 20}, {'name':  'Torso', 'health': 60}, {'name':  'Arms', 'health': 40}, {'name':  'Legs', 'health': 40}, {'name':  'Groin', 'health': 60}], 'health': 200, 'armor' : []})

  if __name__ == '__main__':
    unittest.main()

  ## Task 2
  ## Either find a chest and get a piece of armor OR become attacked
  ## Some % chance for a chest or attack
  ## If it's a chest what does it have?
  ## If it's an attack which attack
