#! ~/anaconda3/bin/python

"""
todo_list.py

Assignment: Complete the following functions:

1) show_todo()
2) add_todo_item()
3) remove_todo_item()

Optional/stretch goals:

4) mark_item_complete()
5) show_completed()

Instructions and hints about logic are available in each function's
docstring.
"""

import io
import json

from typing import Dict, List, Optional


USAGE = """todo_list.py

Options:

1 -> Show to-do list
2 -> Add item to to-do list
3 -> Remove item from to-do list
4 -> Mark item as complete
5 -> Show completed items
6 -> Save
7 -> Save and exit
0 -> Show this menu
"""


TodoAndCompleted = Dict[str, List[str]]


def load_existing_list(filename: str) -> TodoAndCompleted:
    """
    Attempt to load a to-do list from disk. If it doesn't exist, create a new one.

    Parameters
    ----------
    filename : str
        Path to to-do list file.

    Returns
    -------
    TodoAndCompleted
        A dict containing a to-do list and a list of completed tasks.
    """
    with open(filename, 'a') as _file:
        try:
            _todo = json.load(_file)
        except io.UnsupportedOperation:
            _todo = dict(todo=[], complete=[])
    return _todo


def safe_number_input(prompt: str) -> Optional[int]:
    """
    Handle numeric values passed to `input()`.

    Parameters
    ----------
    prompt : str
        Text to use as user prompt.

    Returns
    -------
    Optional[int]
        The user input cast to `int`. If user input cannot be cast as
        an integer, returns None.
    """
    _choice: Optional[int] = None
    try:
        _choice = int(input(prompt).strip())
    except ValueError:
        print('ERROR: Must choose an integer.')

    return _choice


def show_todo(todo: TodoAndCompleted) -> None:
    """
    Enumerate and print todo['todo'].

    Parameters
    ----------
    todo : TodoAndCompleted
        A dict containing a to-do list and a list of completed tasks.

    Returns
    -------
    None
    """
    _todo = todo.copy()

    # Your code here...
    
    return None


def add_todo_item(todo: TodoAndCompleted, task: str) -> TodoAndCompleted:
    """
    Append an item to todo['todo'].

    Parameters
    ----------
    todo : TodoAndCompleted
        A dict containing a to-do list and a list of completed tasks.
    task : str
        Task to append to todo['todo'].

    Returns
    -------
    TodoAndCompleted
        Copy of `todo` with `task` appended to `todo['todo']`.
    """
    _todo = todo.copy()

    # Your code here...
    
    return _todo


def remove_todo_item(todo: TodoAndCompleted, idx: int) -> TodoAndCompleted:
    """
    Delete todo['todo'][idx].

    Parameters
    ----------
    todo : TodoAndCompleted
        A dict containing a to-do list and a list of completed tasks.
    idx : int
        Index of an item to delete from todo['todo'].

    Returns
    -------
    TodoAndCompleted
        Copy of `todo` with todo['todo'][idx] removed.
    """
    _todo = todo.copy()

    # Your code here...
    
    return _todo


def mark_item_complete(todo: TodoAndCompleted, idx: int) -> TodoAndCompleted:
    """
    Pop todo['todo'][idx] and append it to todo['complete'].

    Parameters
    ----------
    todo : TodoAndCompleted
        A dict containing a to-do list and a list of completed tasks.
    idx : int
        Index of an item to move from todo['todo'] to todo['complete'].

    Returns
    -------
    TodoAndCompleted
        Copy of `todo` with `todo['todo'][idx]` moved to `todo['complete'].
    """
    _todo = todo.copy()

    # Your code here...
    
    return _todo


def show_completed(todo: TodoAndCompleted) -> None:
    """
    Enumerate and print todo['complete'].

    Parameters
    ----------
    todo : TodoAndCompleted
        A dict containing a to-do list and a list of completed tasks.

    Returns
    -------
    None
    """
    _todo = todo.copy()

    # Your code here...
    
    return None


def write_list(todo: TodoAndCompleted, filename: str) -> None:
    """
    Write `todo` to disk as a JSON file.

    Parameters
    ----------
    todo : TodoAndCompleted
        A dict containing a to-do list and a list of completed tasks.
    filename : str
        Path for to-do list output

    Returns
    -------
    None
    """
    with open(filename, 'w') as _file:
        json.dump(todo, _file)
    return None


def main() -> None:
    _filename = 'todo_list.json'
    _todo = load_existing_list(_filename)

    print(USAGE)

    while True:
        _choice = safe_number_input('Choose a menu option: ')

        # 1 -> Show to-do list
        if _choice == 1:
            show_todo(_todo)
        
        # 2 -> Add item to to-do list
        elif _choice == 2:
            _to_add = input('Enter a new to-do item: ').strip()
            _todo = add_todo_item(_todo, _to_add)
        
        # 3 -> Remove item from to-do list
        elif _choice == 3:
            _remove_idx = safe_number_input('Enter an item number to remove: ')
            if _remove_idx is not None:
                _todo = remove_todo_item(_todo, _remove_idx)
        
        # 4 -> Mark item as complete
        elif _choice == 4:
            _complete_idx = safe_number_input('Enter an item number to mark complete: ')
            if _complete_idx is not None:
                _todo = mark_item_complete(_todo, _complete_idx)
        
        # 5 -> Show completed items
        elif _choice == 5:
            show_completed(_todo)
        
        # 6 -> Save
        elif _choice == 6:
            write_list(_todo, _filename)
        
        # 7 -> Save and exit
        elif _choice == 7:
            write_list(_todo, _filename)
            break
        
        # 0 -> Show menu
        elif _choice == 0:
            print(USAGE)
        
        else:
            continue


if __name__ == '__main__':
    main()
