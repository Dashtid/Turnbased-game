from body import Body

def STATS(which):
  '''
  from character import STATS as character_stats
  character_stats('base')
  '''
  stats = {}
  stats['base'] = {
    'experience': 100,
    'level': 1,
  }
  return stats[which]

# Last alternative: “`lambda`-hardened” `dict`
# STATS()['base']['level']
# STATS()['base']['level'] = None
# assert STATS()['base']['level'] = None
# assert 
STATS = lambda : {
  'base': {
    'experience': 100,
    'level': 1,
  },
}

class Character():
  @staticmethod
  def stats(which):
    '''
    from character import Character
    Character.stats('base')
    '''
    stats = {}
    stats['base'] = {
      'experience': 100,
      'level': 1,
    }
    return stats['which']
  
  def __init__(self, name):
    self.name = name
    self.body = Body()
    self.armor = []
    # self._level = 1
    self._stats = {
      'level': Character.stats('base')['level'],
      # 'level': STATS['base']['level'],
      'experience': Character.stats('base')['experience'],
    }

  def add_armor(self, armor_piece):
    self.armor.append(armor_piece)
    

  def stats(self):
    stats = self._stats
    # Sanity Check
    assert stats is not None
    # Ideally, something like:
    # - Make sure we haven't lost any entries
    #   assert depth(stats) >= depth(Character.stats())
    # - Perhaps: make sure we haven't added any entries
    #   assert depth(stats) == depth(Character.stats())
    return stats

  def level(self):
    level = self.stats()['level']
    # Sanity check
    assert level >= 1
    return level

  def _level_up(self):
    self._stats['level'] += 1
    return self._stats['level']

  def health(self):
    """
    Character's health:

    - Based on body's health
    - Scales with character's level
    """
    health = self.body.health()
    # Scale by character level
    health += health * self.level() // 10
    return health

  def protection(self): # TODO: This should be done in the armor class
    total_protection = sum(self.armor.protections[0]) 
    return total_protection
    
  def attack(self, target, attack):
    """
    Launch an attack against another character
    """
    target_health = target.health()
    pass   

    
    pass
  
  def attacked(self, attacker, attack):
    """
    Receive an attack

    `attack` includes:

    - attacker
    - body part
    - damage
    """
    pass

# Tests

def _tests():
  pass

if __name__ == '__main__':
  _tests()