class Armor:
  """
  """
  def __init__(self, name):
    self.name = name
    self.protections = []

  def add_protection(self, body_part, percentage):
    """
    """
    protection = body_part, percentage
    self.protections.append(protection)

