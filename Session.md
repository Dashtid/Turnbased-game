# Session 2023-03-15

## Working with code

### REPL shortcuts

* `Ctrl+A` / `Ctrl+E` jump to beginning and end of line
* `Shift` to select / Combine with other modifiers

### Editor shortcuts

* `Ctrl+D` to select multiple occurences in editor

## Python coding concepts

### Tuples

* Collection of multiple items
* Items are ordered, immutable

```python
# Generic tuple
tup = ('value_one', 2)

# Dont' need the (parens)
# The comma       ↓ is what counts
tup == 'value_one', 2
```

```python
# Specific instance according to model
person = ('Jim', 42)
```

----

```python
# Later: constructor functions
def Person(name = 'Jim', age = 42):
  return (name, age)
```

* Unpacking vs. indexing

```python
# Tuple indexing
assert person[0] == 'Jim'
assert person[1] == 42
```

```python
# Tupel unpacking
name, age = person
```

### Functions

* Units of reusable code:

```python
# Functions return values
def my_func():
  pass
  return ...

# Functions may take arguments
def my_func(args):
  pass

----
  
# Later: variable argument structures
# `*list` and `**dict`
def my_func(*args, **kwargs):
  pass
```

### Assert statements

* As development tests:

```python
# Will halt program
assert False == True, "Nope!"

# Will pass
assert True, "We'll never see this"
```

```python
# Test function
assert my_func("?") == 42, "Not the answer"
```

* As sanity checks:

```python
# Constituent parts combine to a whole
assert tup == (tup[0], tup[1])

# Size of parts add up to size of whole
assert len(tup) == len(tup[0]) + len(tup[1])

# Object returned by constructor is equal to an identical one
assert (person := Person()) == Person()
```