name = input("Student name: ")
marks = [int(input(f"Subject {i}: ")) for i in range(1, 4)]

total = sum(marks)
average = total / len(marks)

print("Name:", name)
print("Total:", total)
print("Average:", average)
print("Result:", "Pass" if all(m >= 35 for m in marks) else "Fail")