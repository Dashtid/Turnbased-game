# Modeling

Modeling within programming is the art of projecting systems from the real world onto corresponding code structures.
This normally involves coming up with a specification as an intermediary step:

```text
Real world → Specification → Code
```

We'll look at some sample scenarios.

## Armor System for Tactics Game

We're developing a round-based tactics game.
Our soldiers, as well as the enemies, can wear pieces of armor.
Each piece of armor offers a certain degree of protection to one or more body parts.

### Specification

Our system needs the following components to work.
We explain how they interrelate and give rough examples.
Edge-cases are up to the programmer to test and document.

#### Armor effect

Armor reduces incoming damage.
For each attack against an in-game character, the armor percentage for the targeted body part is multiplied by the raw damage to give the applied damage:

* Attack against the torso:

  * Damage: 60
  * Armor protection: 25%
  * Damage applied: 45

Multiple pieces of armor may be worn at the same time.
In this case, protection stacks up to 99%.

#### Example armor pieces

1. *Steel helmet* protects:

   * Head: 30%

2. *Kevlar helmet* protects:

   * Head: 50%
   * Neck: 30%

3. *Flak vest* protects:

   * Torso: 50%

4. *Interceptor body armor* protects:

   * Torso: 70%
   * Groin: 30%
   * Neck: 10%

### Modeling task

1. Outline the neceassary functions to calculate damage applied to an in-game character:

   1. What functions are needed?
   2. What are their names and parameters?

2. Model the armor system using the built-in Python data structures:

   1. What concepts will you need to model?
   2. What data structures should be used, and how?

3. Test your model and verify it works:

   1. Develop tests for your model.
   2. Run tests to verify your model works.

### Tips

* There are no clear-cut right and wrong answers here.
* It's up to you to come up with a good solution.
* It's probably a good idea to draft a few solutions and compare the pro's and con's.

## Updates

`2023-08-08`

### Restructure

1. Create dedicated `game/` project directory.

2. Create individual files to hold the code:

    * `game/`
        * `character.py`
        * `armor.py`
        * `game.py`
        * etc.

3. Move functions into individual files.

4. Reconnect the pieces via imports in

### Refactor

* `BodyPart()` function that takes `name` and `mass`.

  * Calculate bodypart `health` based on its `mass`.

* `Body()` function that takes a `bodypart` and constructs proportional body from that.

    ```
    Body(('Head', 10))
    ```
