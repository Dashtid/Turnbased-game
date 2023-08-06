# # Contents in this file are executed when we hit “Run”
import work as work

def end_condition(character):
  # Checking if the character is still alive
  if work.calculate_health(character) <= 0:
    return True
  return False


# Just some hardcorded booleans for now.
ongoing_game = True
character = None


while ongoing_game:
  if character is None:
    work.character_creation() # Creating a character if none exists
    
  ## Task 2
  ## Either find a chest and get a piece of armor OR become attacked
  ## Some % chance for a chest or attack
  ## If it's a chest what does it have?
  ## If it's an attack which attack
  
  if end_condition:
    print("You have died")
  
ongoing_game = False