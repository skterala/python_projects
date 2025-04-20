'''
A list is a built-in data type in Python that is ordered, mutable, and can contain duplicate values and mixed data types.

Key Properties:
---------------
1) Ordered: Items maintain their insertion order.
2) Mutable: You can change add or remove items.
3) Indexed: You can retrieve the items from the list via zero-based index.
4) Can contain mixed data types and duplicates.

Example: my_list = [10, "hello", 3.14, True]

Common List of Functions and Methods.
-------------------------------------
1) Access and Modify:

   my_list[0] # Access the first element.
   my_list[-1] # Access the last element.
   my_list[1:3] # Slicing.
   my_list[1] = 42 # Modify the 2nd element value.

2) Add Items:

   my_list.append("hi") # add the element at the end of the list.
   my_list.insert(2, "new") # insert at position
   my_list.extend([5,6]) # add multiple items.

3) Remove Items:

   my_list.remove("hello") # Remove first occurrence.
   my_list.pop() # Remove last item.
   my_list.pop(2) # Remove at Index.
   del my_list[1] # Remove by index.
   my_list.clear() # Remove all items.

4) Check, Count & Sort:

   len(my_list) : Length of list.
   "hello" in my_list # Check existence.
   my_list.count(10)  # count occurrences.
   my_list.index(10)  # Find index of item.
   my_list.sort()     # Sort list
   sorted(my_list)    # Return sorted copy.
   my_list.reverse()  # Reverse in place.

5) Copy and Combine:

   copy_list = my_list.copy()  # Shallow Copy.
   combine = my_list + [1, 2, 3] #Combine List.
'''

my_list = [10, "hello", 3.14, True]

my_list[1] = 'Hi'

my_list.append("1234")
my_list.extend(['a', 'b', 'c'])
my_list.insert(1,'how are you?')

print(my_list[1])
print(my_list)

my_list.pop(4)
print(my_list)