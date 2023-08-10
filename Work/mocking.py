def _random(thing):
  """
  _random('name') -> 'Jack'
  _random('age') -> 42
  _random('size') -> 'medium'
  """
  from random import choice
  
  # Harden dict against accidental changes
  # Insert `lambda : ` before opening `{`
  # categories = {
  categories = lambda: {
    # Sets guard against duplicates
    'guy': (guys := {'Jim', 'John', 'Jack'}),
    'gal': (gals := {'Alice', 'Mary', 'Molly'}),
    'name': (person := guys.union(gals)),
    'person': person,
    'age': range(1, 100),
    'number': {42, 69, 51, 13, 72},
    'size': {'large', 'medium', 'small'},
    'animal': {'Dog', 'Cat', 'Horse'},
    ...: {...},
  }
  
  variations = categories().get(thing)
  # Variations is `None` if key unkown
  # Ensure `choice()` works
  # `None` -> `[None]`
  
  # Harden list conversion against None
  instance = choice(list(variations or [None]))
  return instance

# Define tests
def _random_tests():
  assert _random('guy') in ['Jim', 'John', 'Jack']
  assert _random('age') > 0
  # Adjust range until satisfied ;)
  assert all(_random('age') > 0 for _ in range(100))
  assert _random('totally_undefined') is None

  # guys = lambda count=3 : [ {'name': some('guy'), 'age': some('age')} for _ in range(count) ]

# Run tests
_random_tests()

# Public interface
# `from mocking import some`
def some(thing):
  return _random(thing)

# 
# return choice([*variations]) if variations else None
# 
# if variations is None:
#   return None
# else:
#   return choice(variations)

# if variations is not None:
#   return choice(variations)
# else:
#   return None