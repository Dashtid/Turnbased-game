# Body Model
# V3.1
# 2023-08-13

class Body():
  """
  """
  def __init__(self, mass=1):
    self._mass = mass
    self._parts = [
      Bodypart('Head', self),
      Bodypart('Neck', self),          
      Bodypart('Torso', self),
      Bodypart('Arms', self),
      Bodypart('Legs', self),
      Bodypart('Groin', self),
    ]

  def parts(self):
    return self._parts

  def health(self):
    """
    Hit points
    
    Not tested!
    """
    # Sum up body part ratios
    health = sum( Bodypart.ratios().values() )
    # Scale by body's mass
    health *= self.mass
    return health

class Bodypart():
  """
  """
  def init(self, name, body=None):
    self.name = name
    # Attach to body
    self.body = body
  
  @staticmethod
  def ratios():
    """
    Allows us to write `Bodypart.ratios()['Head']`, etc.
    """
    return {
      'Head': 3,
      'Neck': 1,
      'Torso': 18,
      'Arms': 6 * 2,
      'Legs': 9 * 2,
      'Groin': 2,
    }

    # Perhaps better like this
    ratios = {}
    ratios['Head']   = 3
    ratios['Neck']   = ratios['Head'] // 3
    ratios['Torso']  = 6 * ratios['Head']
    ratios['Arms']   = 2 * 3 * ratios['Head']
    ratios['Legs']   = 2 * 2 * ratios['Head']
    return ratios
  
  @staticmethod
  def names():
    return Bodypart.ratios().keys()