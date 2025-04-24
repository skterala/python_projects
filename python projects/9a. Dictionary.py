'''
A dictionary in a pythong is an unordered, mutable, and indexed collection of key-value pairs.
Each Key must be unique, and it can be of any immutable data type (strings, numbers, tuples)
Value can be any data type.

Key Properties:
===============
1. Unordered: The items are not sorted in a particular order.
2. Mutable: You can change the values and structure of a dictionary after it is created.
3. Indexed: Each item is accessed via a unique key.
'''

# 1) Create a Dictionary:
# ====================

# Option 1: Using curly braces.

my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

print(f"my_dict is: {my_dict}")

# Option 2: Using dict() constructor.

my_dict1 = dict(key1 = "value1", key2 = "value2", key3 = "value3")

print(f"my_dict1 is: {my_dict1}")

# Dictionary Methods and Functions:
# =================================

# 1) clear() : Removes all the items from the dictionary.

my_dict.clear()
# OR
my_dict = {} # empty dict.

# 2) copy() : Returns a shallow copy of the dictionary.

my_copied_dict = my_dict1.copy()

print(f"my_copied_dict is: {my_copied_dict}")

# 3) fromkeys() : Creates a new dictionary with keys from the provided iterable. Values set to a specified value, default is None.

keys_list = ['a', 'b', 'c']

my_new_dict1 = dict.fromkeys(keys_list,0)

print(f"my_new_dict1 is: {my_new_dict1}")

# 4) get() :  Returns the value of a specified key. If the key doesn't exist, it returns "None" default (or returns a value if the value is provided.)

print(f"Value of Key1 is : {my_copied_dict.get('key1')}")
print(f"Value of Key10 is : {my_copied_dict.get('key10')}")

# 5) items() : Returns a view object, which is a list of dictionary's key-value tuple pairs.

print(f"Items of a my_dict1 are : {my_dict1.items()}")
# O/P: Items of a my_dict1 are : dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])

# 6) keys() : Returns a view object of all the keys in dictionary.

print(f"All the keys of my_dict1 dictionary: {my_dict1.keys()}")

# 7) pop() : Removes and returns the value associated with a specific key. If the key doesn't exist, it raises a KeyError

my_dict1.pop('key1', None)

# 8) popitem() : Removes and returns the last inserted key-value pair as a tuple. This is useful for popping items in LIFO order.

my_new_dict2 = {'a':'v1', 'b':'v2'}
my_new_dict2.popitem()

print(my_new_dict2)

# 9) setdefault() : Returns the value of a key if it exists. If the key doesn't exist, it inserts the key with the specified default value.

my_new_dict3 = {'a':'v1', 'b':'v2'}
my_new_dict3.setdefault("c", 'v3')
print(my_new_dict3)

# 10) update() : updates the dictionary with key-value pairs from another dictionary or iterable of key-value pairs.

my_new_dict4 = {"a": 1, "b": 2}
my_new_dict4.update({"b": 3, "c": 4})

print(my_new_dict4)

# 11) values() : Returns a view object that displays a list of all the values in the dictionary.

my_new_dict5 = {"a": 1, "b": 2, 'c': 3}
print(my_new_dict5.values())

# 12) Add new item to the dictionary

my_new_dict5['d'] = 10

print(my_new_dict5)

# 13) Edit an item

my_new_dict5["a"] = 100  # if it finds a Key. a it wll update the value, otherwise it will insert.

print(my_new_dict5)

# 14) Loop through a dictionary

for key in my_new_dict5:
    print(f"Key Name : {key}")
    print(f"Value : {my_new_dict5[key]}")

# Common Functions:
# =================

# 1) len() : Returns the number of items in dictionary.
# 2) del : Deletes a key-value pair by key.  Eg: del my_dict["a"]
# 3) in : Checks if a key exists in the dictionary. Eg: "a" in my_dict
# 4) sorted() : Sorts the dictionary keys. Eg: sorted(my_dict)