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

def dict_to_list(dict):
  new_list = []
  for key in dict:
    new_list.append(dict[key])
  return new_list

# Another way
# named = lambda dicts : { dict['name']: dict for dict in dicts }


body = [
      {'name': 'Head', 'health': 10}, 
      {'name':  'Neck', 'health': 20}, 
    ]

