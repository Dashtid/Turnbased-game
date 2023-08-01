# # Contents in this file are executed when we hit “Run”
import work as work

jones = work.Character('jones')
print(jones)

def end_condition():
## Is my character still alive?
  return False

ongoing_game = True
character = None


while ongoing_game:
  if character is None:
  ## Task 1
  ## print to screen charcater creation
  ## who are youname
    character = Character("Tom")
  ## Task 2
  ## Either find a chest and get a piece of armor OR become attacked
  ## Some % chance for a chest or attack
  ## If it's a chest what does it have?
  ## If it's an attack which attack
  
  if end_condition:
    print("you died")
  
ongoing_game = False