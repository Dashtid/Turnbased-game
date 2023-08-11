# Utilities
# V3.1
# 2023-08-09

def list_to_dict(list):
  """
  Utility function that takes in a list containing dictionaries and returns a dictionary where the keys are the names of the dictionaries and the values the dictionaries themselves.   
  """
  new_dict = {}
  for dict in list:
    new_dict[dict['name']] = dict # Setting the key in the new dictonary to be the name of the selected dictionary and the value to be the dictionary itself
  return new_dict

# Alternative implementation
def named(dicts):
  named = {}
  for dict in dicts:
    named[dict['name']] = dict
  return named

# Another way
# named = lambda dicts : { dict['name']: dict for dict in dicts }