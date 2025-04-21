# Range function should be used with another function like for loop.

# Range from 1 to 10 with default step 1. Here 1 is inclusive and 10 is not inclusive.
for i in range(1, 10):
    print(f"With default step 1: {i}")

# Range from 1 to 50 with step size 3.
for i in range(1, 50, 3):
    print(f"With step size 3: {i}")

total = 0
for i in range(1, 101):
    total += i

print(f"Sum of numbers from 1 to 100: {total}")