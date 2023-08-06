def _random(thing):
  from random import choice

  # Harden dict against accidental changes
  # Insert `lambda : ` before opening `{`
  # categories = {
  categories = lambda: {
    # Sets guard against duplicates
    'name': {'Jim', 'John', 'Jack'},
    'age': {42, 69, 51, 13, 72},
    'size': {'large', 'medium', 'small'},
    'animal': {'Dog', 'Cat', 'Horse'},
  }
  variations = categories().get(thing)
  # Observations is `None` if key unkown
  # Ensure `choice()` works
  # `None` -> `[None]`

  # Harden list conversion against None
  instance = choice(list(variations or [None]))
  return instance

  # return choice([*variations]) if variations else None

  if variations is None:
    return None
  else:
    return choice(variations)

  if variations is not None:
    return choice(variations)
  else:
    return None


# Tests
assert _random('name') in ['Jim', 'John', 'Jack']
assert _random('age') > 0
# Adjust range until satisfied ;)
assert all(_random('age') > 0 for _ in range(100))
assert _random('totally_undefined') is None