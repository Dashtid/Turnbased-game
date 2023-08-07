# # Contents in this file are executed when we hit “Run”
from enum import Enum
import random as rand
import work as work

class AttackType(Enum):
  NORMAL = 25
  HEAVY = 50

def end_condition(character):
  # Checking if the character is still alive
  if work.calculate_health(character) <= 0:
    return True
  return False


  ## Task 2
  ## Either find a chest and get a piece of armor OR become attacked
  ## Some % chance for a chest or attack
  ## If it's a chest what does it have?
  ## If it's an attack which attack

def event(character):
  random_number = rand.random()
  if random_number >= 0.5:
    work.attack(character, 'Torso', AttackType.NORMAL)
    return None
  else:
    return None # Find a chest with an item?
    
    
# Just some hardcorded booleans for now.
ongoing_game = True
character = None


while ongoing_game:
  if character is None:
    work.character_creation() # Creating a character if none exists
  event(character) # Think this is not quite right
  if end_condition(character): # Checks if the character is dead
    print("You have died") 
    ongoing_game = False # Ends the game

# Todo
# 1. Give different health values to body parts
# 2. Take armor into account when calculating damage
# 3. Add `damage_taken` to body parts

# Attack a character and print is the character dead or not?

# Example 1: 100 damage to the head wo. armor
# Example 2: 100 damage to the head w. armor

# 1.Attack 2.Summary 3.New turn


import curses

def main(stdscr):
    ongoing_game = True
    character = None

    while ongoing_game:
        if character is None:
            character = work.character_creation()

        stdscr.clear()  # Clear the screen
        stdscr.addstr(0, 0, "Your Game Title Here", curses.A_BOLD)

        # Update and display game state here
        # You can use stdscr.addstr() to print text at specific positions

        stdscr.refresh()  # Refresh the screen

        # Handle user input and game logic
        key = stdscr.getch()
        if key == ord('q'):
            ongoing_game = False
        # Other key handling logic

        if end_condition(character):
            stdscr.addstr(10, 0, "You have died", curses.A_BOLD)
            stdscr.refresh()
            curses.napms(2000)  # Pause for 2 seconds
            ongoing_game = False

curses.wrapper(main)  # Start the game loop with curses
