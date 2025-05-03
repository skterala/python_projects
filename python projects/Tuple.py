'''
Tuple:
======
A tuple is an immutable (unchangeable) and ordered collection of elements in Python. Tuples are similar to lists but
cannot be modified after creation.

Properties:
===========
    1) Ordered: Items have a defined order and can be accessed by index.
    2) Immutable: Cannot change elements after creation.
    3) Can contain mixed data types: (1, "hello", 3.14)
    4) Can be nested: (1, (2, 3), [4, 5])

Syntax:
=======
my_tuple = (1, 2, 3)

-> You can also create a tuple without parentheses using commas:

my_tuple = 1, 2, 3 #

-> To create a single-element tuple, a comma is required.

single = (1,)  # This is a tuple
not_a_tuple = (1)  # This is just an integer

Tuple Operations:
=================
t = (10, 20, 30, 20)
len(t)         # Length of the tuple
t[1]           # Access element by index
t[-1]          # Access last element
t[1:3]         # Slicing
20 in t        # Membership test
t + (40, 50)   # Concatenation
t * 2          # Repetition

Tuple Methods:
==============
.count(x)	Returns the number of times x appears in tuple
.index(x)	Returns the index of the first occurrence of x

Example:
--------
t = (1, 2, 3, 2, 4)
t.count(2)      # Output: 2
t.index(3)      # Output: 2

'''