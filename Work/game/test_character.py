# A little bit unsure as of how to go about this
import unittest # https://docs.python.org/3/library/unittest.html
import game.character as character_model

class TestCharacter(unittest.TestCase):

  def test_character(self):
    test_character = character_model.Character('Test')
    self.assertEqual(test_character, {'name': 'David', 'body': [{'name': 'Head', 'health': 10}, {'name':  'Neck', 'health': 20}, {'name':  'Torso', 'health': 60}, {'name':  'Arms', 'health': 40}, {'name':  'Legs', 'health': 40}, {'name':  'Groin', 'health': 60}], 'health': 200, 'armor' : []})

  if __name__ == '__main__':
    unittest.main()


#test_character = character('Test')

# Check it out
#
# Import as factory function
from character import Character
# `Character('David')`
#
# Alternatively, import as function with verb name
from character import character_creation as choose_player
# `choose_player('David')`
#
# BUT
# 
# The function `character_creation` shouldn't be within `character`.
# Probably, `game.py` is the more appropriate module.
