
class Armor():
  """
  """
  def __init__(self, name, protections):
    self.name = name
    self.protections = protections

  def Protection(self, body_part, percentage): # TODO: Naming?
    self.body_part = body_part
    self.percentage = percentage
    
    