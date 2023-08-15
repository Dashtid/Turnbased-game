# Utilities
# V3.1
# 2023-08-09

def list_to_dict(list):
  """
  Utility function that takes in a list containing dictionaries.
  Returns a dictionary where the keys are the names of the dictionaries.
  The values the dictionaries themselves.   
  """
  new_dict = {}
  for dict in list:
    new_dict[dict['name']] = dict 
  return new_dict

# Alternative implementation
def named(dicts):
  named = {}
  for dict in dicts:
    named[dict['name']] = dict
  return named

# Another way
# named = lambda dicts : { dict['name']: dict for dict in dicts }