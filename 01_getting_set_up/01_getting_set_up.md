# Introduction to Python--Lesson 1

## Introduction

1. Goal of course: learn to think like a programmer
2. Goal of lesson: write and run two Python programs
   1. Hello world
   2. Hello user

## Enable file extensions in Windows Explorer

1. ...

## Install GitHub Desktop

1. Download the [GitHub Desktop for Windows installer](https://central.github.com/deployments/desktop/desktop/latest/win32).
2. Install...

## Install and Configure Visual Studio Code

1. Download the [Visual Studio Code for Windows installer](https://aka.ms/win32-x64-user-stable).
2. Install...
3. Run `install_vs_code_ext.cmd`. This installs a few extensions to make life easier in VS Code.

## Install Anaconda

1. Download the [Anaconda for Windows installer](https://repo.anaconda.com/archive/Anaconda3-2020.02-Windows-x86_64.exe).
2. Install...

## Approaching Programming

1. What is programming?
   1. Started as a way to do math on computing machines (Ada Lovelace).
   2. In fact, Computer Science is still pretty much a branch of Mathematics.
   3. But nowadays, programming is so much more!
   4. The experience of programming is like being an architect, a poet, and a detective all at once.
2. Code is like a coworker: TOM (Milton Waddams pic?)
3. Exercise: Make a PB&J sandwich
4. Bugs and debugging
   1. ADM Grace Hopper and the first bug
   2. When things go wrong, TOM doesn't communicate very clearly
   3. Google and StackOverflow (error messages are your friend)

## Approaching Python

1. What is Python?
2. What is Python used for?

## The Python REPL

1. REPL--the **R**ead-**E**valuate-**P**rint **L**oop
2. Launching the Python REPL

## Strings

1. When we have a bunch of letters/numbers/symbols all lumped together, they're called "strings"
2. Two types: single-line and multi-line strings
3. Single-line string syntax
   1. Wrap in single or double quotes, but can't mix.
   2. Exercises
      1. Wrap in single quotes
      2. Wrap in double quotes
      3. Leading quote but not trailing quote
      4. Mixed usage--when it's a bug (diff leading and trailing quotes)
      5. Mixed usage--when it's a feature (using quotes inside of a string)
      6. Mixed usage--escaping quotes inside a string
   3. Idiomatic style is single quotes.
4. Multi-line string syntax
   1. Wrapped in three sets of single quotes or three sets of double quotes, but can't mix.
   2. Exercises
      1. Wrap in single quotes
      2. Wrap in double quotes
      3. Leading quote but not trailing quote
      4. Mixed usage--when it's a bug (diff leading and trailing quotes)
      5. Mixed usage--when it's a feature (using quotes inside of a string)
      6. Mixed usage--escaping quotes inside a string
   3. Idiomatic style is double quotes.

## Variables

1. Variables are like putting nametags on things inside Python.
2. Anatomy of an assignment expression
   1. variable name
   2. assignment operator
   3. variable value
3. Rules for names
   1. Can only contain letters, numbers, and underscores.
   2. Cannot start with a number, but can start with an underscore.
   3. Cannot be a keyword.
   4. By convention, variable names should be all-lowercase, with words separated by underscores, a/k/a `snake_case`.

## Functions

1. In Python, a function is a bunch of code all grouped together under a single nametag.
2. Their names look like variables but with parentheses at the end, like `my_function()`.
3. The parentheses make it look like math, like $y = f(x)$. The mathiness is on purpose. It's to remind you that a Python function, just like a mathematical function, takes what you put between the parentheses and performs some action on it.

## `print()`

1. Doesn't have anything to do with printers (anymore, at least).
2. Name is a relic of the past, like using a picture of a floppy disk for the "save" icon.
3. What it does: takes whatever is put between the parentheses and shows it on the screen. So `print('foo')` makes the string "foo" show up on the screen.
4. Why don't we need to use it in the REPL? Because it's a Read-Evaluate-**Print** Loop--the `print()` happens automagically.
5. Exercise: `print('Hello, world!')` in the REPL

## Writing Hello World

1. Open VS Code.
2. File -> New File, File -> Save, name it `hello_world.py`.
3. ".py" is the file extension for Python files.
4. Write `print('Hello, world!')` inside `hello_world.py`. File -> Save.
5. VS Code: View -> Terminal
6. In terminal, type `python hello_world.py` and hit Enter.
7. The text "Hello, world!" should appear inside the terminal.
8. What would happen if we just wrote `'Hello, world!'` inside the program and tried running it?
