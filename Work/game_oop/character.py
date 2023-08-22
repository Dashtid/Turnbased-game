from body import Body

class Character():
  def __init__(self, name):
    self.name = name
    self.body = Body()
    self.armor = None
    self._level = 1

  def health(self):
    """
    Character's health:

    - Based on body's health
    - Scales with character's level
    """
    health = self.body.health()
    health += self._level * health // 10
    return health