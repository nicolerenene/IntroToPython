---
author: Cory Taylor
title: Getting Acquainted with Python
date: April 17, 2020
---

# Introduction

---

## Goals

1. Goal of course: Learn to think like a programmer
2. Goal of this lesson: Write and run two Python programs
   1. Hello world
   2. Hello NAME

---

## Lesson Overview

1. Set up a Python development environment
2. Approaching programming
3. Approaching Python
4. Strings, variables, and functions
5. The `print()` function
6. Hello, world!
7. The `input()` function
8. Hello, NAME!

---

# Getting Set Up

---

## Enable File Extensions in Windows Explorer

---

## Install Visual Studio Code

---

## Install GitHub Desktop

---

## Install Anaconda

---

# Approaching Programming

---

## What was Programming?

Started as a way to do math on computing machines.

![Charles Babbage's Analytical Engine](assets/img/babbage_analytical_engine_576x553.png)

---

## Ada Lovelace, The First Programmer

![Ada Lovelace](assets/img/ada_lovelace_498x623.png)

---

## Computers in 1924

![1920's computers at the Department of the Treasury](assets/img/1924_dept_treasury_computing_division.jpg)

---

## What is Programming?

* There's still math, sure...
* But nowadays, it's so much more than math.
* It's like being an architect, a poet, and a detective all at once.

---

## Code is Like a Coworker

Meet Tom.

![Milton Waddams](assets/img/milton_waddams.jpg)

---

## Exercise

Make a PB&J sandwich

---

# Bugs and debugging

---

## The First Bug

![The first computer bug](assets/img/first_computer_bug.jpg)

---

## Error Messages

1. When things go wrong, Tom doesn't communicate very clearly.
2. Error messages are your friend.
3. Google, Google, Google.

---

# Approaching Python

---

## What is Python?

---

## What is Python used for?

---

## The Python REPL

* *REPL*: *R*ead-*E*valuate-*P*rint *L*oop
* Launching the Python REPL

---

# Strings

---

## About Strings

* *Strings*: groups of characters all lumped together
* *Characters*: letters, numbers, and symbols
* Two types of strings:
  1. Single-line
  2. Multi-line

---

## Single-Line Strings

* Wrap in single or double quotes
* Idiomatic style: single quotes

    ```python
    'This is a string.'  # Most common form.
    "This is a string."  # Also works.
    ```

* Mixing quotes will cause a SyntaxError

    ```python
    'This is not a string."
    "This is not a string.'
    ```

---

## Mixing Quotes

* Mixing quotes has its uses.

    ```python
    "Python's great!"
    'They said, "Python is great!"'
    ```

* Sometimes we have to *escape* a quote.

    ```python
    'They said, "Python\'s great!"'
    'Don\'t need to mix quotes this way.'
    ```

---

## Single-Line String Exercises

1. Wrap in single quotes <!-- .element: class="fragment" data-fragment-index="1" -->
2. Wrap in double quotes <!-- .element: class="fragment" data-fragment-index="2" -->
3. Mixed usage--when it's a bug (different leading and trailing quotes) <!-- .element: class="fragment" data-fragment-index="3" -->
4. Mixed usage--when it's a feature (using quotes inside of a string) <!-- .element: class="fragment" data-fragment-index="4" -->
5. Mixed usage--escaping quotes inside a string <!-- .element: class="fragment" data-fragment-index="5" -->

---

## Multi-Line Strings

* Wrap in three sets of single quotes or three sets of double quotes
* Idiomatic style: double quotes

```python
# Most common:
"""This is a
multi-line string"""

# Also works:
'''This is a
multi-line string'''
```

---

## Multi-Line String Exercises

1. Wrap in single quotes <!-- .element: class="fragment" data-fragment-index="1" -->
2. Wrap in double quotes <!-- .element: class="fragment" data-fragment-index="2" -->
3. Mixed usage--when it's a bug (diff leading and trailing quotes) <!-- .element: class="fragment" data-fragment-index="3" -->
4. Mixed usage--when it's a feature (using quotes inside of a string) <!-- .element: class="fragment" data-fragment-index="4" -->

---

## Variables

* *Variables*: basically, putting nametags on things
* Create a variable with an *assignment expression*:

    ```python
    my_variable = 'A string'
    ```

* *Reference* a variable by using its name:

    ```python
    my_variable
    # >>> 'A string'
    ```

---

## Anatomy of an Assignment Expression

```python
  my_variable  =  'A string'
# |---1---| |2| |---3---|
```

1. Name
2. Assignment operator
3. Value

---

## Rules for Variable Names

* Can only contain letters, numbers, and underscores

    ```python
    my_variable = 'foo'    # This works
    my_variable_2 = 'bar'  # This works, too
    my_variable! = 'baz'   # SyntaxError
    ```

* Can't start with a number

    ```python
    my_variable_1 = 'quux' # This works
    1st_variable = 'spqr'  # SyntaxError
    ```

* Idiomatic style: `snake_case`
* Can't be a keyword

---

## Keywords

```python
False     await       else       import      pass

None      break       except     in          raise

True      class       finally    is          return

and       continue    for        lambda      try

as        def         from       nonlocal    while

assert    del         global     not         with

async     elif        if         or          yield
```

---

## Functions

* *Function*: a bunch of code grouped under one nametag
* Look like variables but with parentheses at the end:

    ```python
    my_function()
    ```

* Many take *arguments*: values or variables *passed in* between the parentheses

    ```python
    my_function('argument')
    my_function(foo)
    ```

* They *return* values, which can be assigned to a variable

    ```python
    foo = my_function('bar')
    ```

---

## Look Familiar?

* Similar notation to mathematical functions:  
  
    $$y = f(x)$$

    ```python
    y = f(x)
    ```

* A Python function takes whatever you put between the parentheses, does something with it, and returns a value.

---

## `print()`

* Doesn't have anything to do with printers (anymore, at least)
* What it does: takes arguments and shows them on the screen
* Name is a relic of the past, like using a picture of a floppy disk for the "save" icon

---

Floppy disks

![Floppy disks](assets/img/floppy_disks_531x256.png)

Save icon

![Save icon](assets/img/save_icon_256x256.png)

---

## `print()` Exercise

Print 'Hello, world!' in the REPL

---

## Question

Why don't we need to use `print()` in the REPL?

---

## Your First Program

1. Open `hello_world.py` in VS Code.  
   (".py" is the file extension for Python files.)
2. In `hello_world.py`, replace

    ```python
    # Your code here...
    ```

    with

    ```python
    print('Hello, world!')
    ```

    and save the file.

---

## Run `hello_world.py`

1. Open the terminal in VS Code.
2. In the terminal, type

    ```bash
    python hello_world.py
    ```

    and hit Enter.

3. The text "Hello, world!" should appear inside the terminal.

---

## Hello World Experiment

What happens if we do this?

1. Change `hello_world.py` from

    ```python
    print('Hello, world!')
    ```

    to

    ```python
    'Hello, world!'
    ```

2. Save and run the program.
