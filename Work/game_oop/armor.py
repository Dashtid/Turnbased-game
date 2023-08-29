class Armor:
  """
  """
  def __init__(self, name):
    self.name = name
    self.protections = []

  def add_protection(self, body_part, percentage, protections):
    self.body_part = body_part
    self.percentage = percentage
    protection = self.bodypart, self.percentage
    protections.append(protection)