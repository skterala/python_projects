student_scores = [180, 124, 165, 173, 189, 169, 146]

# Option 1:
print(max(student_scores))

# Option 2:

max_num = 0

for score in student_scores:
    if score > max_num:
        max_num = score
        
print(f"Max score is {max_num}")