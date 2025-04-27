import random
import debugger_maths

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = debugger_maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])

# Create a breakpoint on the line of code you want to debug.
# CLick "bug" icon, next to run button to go to debug run mode.
# In the Debug window, use "Step Over, step into (which goes to another function which are used in this code. EX: debugger_maths.add), step out buttons".
# Use Threads & Variables and Console windows to debug.