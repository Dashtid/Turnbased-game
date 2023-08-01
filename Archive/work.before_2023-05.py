def get_older_person(younger, older):
  younger_age, older_age = younger[1], older[1]
  if younger_age < older_age:
    return older
  if younger_age == older_age:
    print("They're the same age")
  return younger

def is_even(number):
  if number % 2 == 0:
    return True
  return False

def is_odd(number):
  if is_even(number):
    return False
  return True

def is_even_no_if(number):
  return number % 2 == 0

def is_odd_no_if(number):
  return False == is_even_no_if(number) # This is basically (number % 2 != 0)

def moving_faster_than(object_speed):
  print('This is a comparasion of your object speed ' + str(object_speed) + ' m/s and various objects.')
  if object_speed > 1000: 
    return print('After detailed scientific analysis we can conclude: The object is faster than a bullet, sound, a cheetah, a bat, and of course, a snail.')
  if object_speed > 330:
    return print('After detailed scientific analysis we can conclude: The object is faster than sound, a cheetah, a bat, and of course, a snail.')
  if object_speed > 30:
    return print('After detailed scientific analysis we can conclude: The object is faster than a cheetah, a bat, and of course, a snail.')
  if object_speed > 10:
    return print('After detailed scientific analysis we can conclude: The object is faster than a bat and the slow-moving but mighty snail.')
  if object_speed > 1:
    return print('The object is faster than a snail')
  

def describe_product(name, kind, price):
  return print("A " + name + " is a " + kind + " and costs " + str(price) + " cents")


def make_person(first_name,last_name, age, middle_name='', initials=False):
  # if middle_name == '':
  if not middle_name:
    return first_name, last_name, age
  if initials == True:
    return first_name, middle_name[0], last_name, age
  else: 
    return first_name, middle_name, last_name, age

def make_person_w_initials(first_name, last_name, age, middle_name='', initials=False):
  if initials==True:
    return first_name, middle_name[0], last_name, age
  else:
    return first_name, middle_name, last_name, age


def get_name(person):
  tuple_lenght = len(person)
  if tuple_lenght > 3:
    return person[0], person[2]
  else:
    return person[0], person[1]


def hello_from(person):
  first, last = get_name(person)
  print(f"Hello from {first}, {last}!")
  return True

def find_older(person1, person2):
  assert len(person1) == len(person2), "Tuples are not the same lenght!"
  if person1[1] == person2[1]:
    print(f"The persons are the same age! Which is: {person1[1]} years.")
    return person1
  elif person1[1] > person2[1]:
    return person1
  else:
    return person2

## Basic mathematical functions

#1. Implement the mathematical functions `min()`, `max()`, `sum()`, and `mean()` using `for` loops.

#   * Your functions should take a list of numbers and return a single number.

def min(nums):
  # for index in range(len(nums)):
  #   num = nums[index]
  for num in nums:
    stored_value = num


def largest(balls):
  larger = 0 
  for ball in balls:
    if ball > larger:
      larger = ball
  return larger

def max(nums):
  largest = 0
  for num in nums:
    if num > largest:
      larger = num
  return larger

def max(nums):
  largest = 0
  index = 0
  while index < len(nums):
    num = nums[index]
    if num > largest:
      larger = num
    index += 1
  return larger

def min(nums):
  smallest = nums[0]
  for num in nums:
    if num < smallest:
      smallest = num
  return smallest

def sum(nums):
  total = 0
  for num in nums:
    total += num
  return total

def mean(nums):
  total = 0
  counted = 0
  for num in nums:
    total += num
    counted += 1
  return total / counted

def summary(nums):
  return min(nums), mean(nums), max(nums)


assert largest([42, 69, 51]) == 69
assert largest([99, 92, 12, 123, 2]) == 123
assert min([13, 88, 45]) == 13
assert min([105, 88, 45]) == 45

#2. Write tests to show your functions work.

#   * Complete the tests before writing your functions.



#3. Implement the same functions again, this time using `while` loops.

#   * Do not use an index variable.
#   * Instead, use the `pop()` method on the list of numbers to get the next element.

### Extra tasks

#1. Implement a function `summary()` that returns a tuple of `min, mean, max` for a list of numbers.

#   * Do not call the previously defined functions from within `summary()`.
#   * Use a single `for` or `while` within your function body.


# Declare two persons
younger_person = ('Jim', 42)
older_person = ('Jack', 51)
# Declare speeds
speed_slower_than_snail = 0.5
speed_faster_than_snail = 2
speed_faster_than_bat = 11 
speed_faster_than_cheetah = 33
speed_faster_than_sound = 333
speed_faster_than_bullet = 1001
# Unpack the ages
younger_age, older_age = younger_person[1], older_person[1]
### Tests - get_older_person()
assert get_older_person(younger_person, older_person) == older_person # Should return True
### Tests - is_even()
assert is_even(younger_age)     # Should return True
assert not is_even(older_age)   # Should return False
### Tests - is_odd()
assert not is_odd(younger_age)  # Should return False
assert is_odd(older_age)        # Should return True
### Tests - is_even_no_if()
assert is_even_no_if(younger_age)     # Should return True
assert not is_even_no_if(older_age)   # Should return False
### Tests - is_odd_no_if()
assert not is_odd_no_if(younger_age)  # Should return False
assert is_odd_no_if(older_age)        # Should return True
### Tests - moving_faster_than()
moving_faster_than(speed_slower_than_snail) 
moving_faster_than(speed_faster_than_bat)
moving_faster_than(speed_faster_than_cheetah)
moving_faster_than(speed_faster_than_sound)
moving_faster_than(speed_faster_than_bullet)
### Tests - negative values of speed
test_speed = -1
# assert test_speed >= 0, 'Speed is not a positive value!' # This error should be thrown
### Tests - describe_product()
product_apple = "apple", "fruit", 20
describe_product(product_apple[0], product_apple[1], product_apple[2])
### Tests - make_person() 
assert make_person('Walter', 'White', 42, middle_name = '') == ('Walter', 'White', 42)
assert make_person('Walter', 'White', 42, middle_name = 'Frank') == ('Walter', 'Frank', 'White', 42)
### Tests - make_person_w_initials()
assert make_person_w_initials('Walter', 'White', 42, middle_name = 'Frank') == ('Walter', 'Frank', 'White', 42)
### Tests - get_name()
# 3-item tuple
person = ('Walter', 'White', 42)
assert get_name(person) == ('Walter', 'White')
# 4-item tuple
person = ('Walter', 'Frank', 'White', 42)
assert get_name(person) == ('Walter', 'White')
### Tests - hello_from()
person = ('Walter', 'White', 42)
assert hello_from(person)
person = ('Walter', 'Frank', 'White', 42)
assert hello_from(person)
### Tests - find_older()
younger = ('Jack', 42)
older = ('John', 69)
result = find_older(younger,older)
print(result)
assert find_older(younger, older) == older
assert find_older(('Jim', 13), younger) == younger
assert find_older(('Jim', 42), younger) == ('Jim', 42)
assert find_older(older, ('Jim', 42)) == older

