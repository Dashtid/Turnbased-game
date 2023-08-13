# Body
import body
# Checking that a bodypart is created correctly
assert(body.Bodypart('Head') == {'name': 'Head', 'health': 10})
# Checking that the body is created correctly
assert(body.Body() == [{'name': 'Head', 'health': 10}, {'name': 'Neck', 'health': 20}, {'name': 'Torso', 'health': 60}, {'name': 'Arms', 'health': 40}, {'name': 'Legs', 'health': 40}, {'name': 'Groin', 'health': 60}])

# Character
import character
# Checking that a test character can be created
test_character = character.Character('Test')
assert(test_character == {'name': 'Test', 'body': [{'name': 'Head', 'health': 10}, {'name': 'Neck', 'health': 20}, {'name': 'Torso', 'health': 60}, {'name': 'Arms', 'health': 40}, {'name': 'Legs', 'health': 40}, {'name': 'Groin', 'health': 60}], 'health': 200, 'armor' : []})
# Checking that calculate_health works
assert(character.calculate_health(test_character) == 200)


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
