# Python Program to Calculate Grade Based on Marks in 3 Subjects

# Input subject names and marks
subjects = []
marks = []

for i in range(3):
    subject = input(f"Enter name of subject {i+1}: ")
    mark = float(input(f"Enter marks for {subject}: "))
    subjects.append(subject)
    marks.append(mark)

# Calculate total and average
total = sum(marks)
average = total / 3

# Determine grade based on average
if average >= 90:
    grade = 'A'
elif average >= 75:
    grade = 'B'
elif average >= 60:
    grade = 'C'
elif average >= 40:
    grade = 'D'
else:
    grade = 'F'

    print("\n--- Student Report ---")
for i in range(len(subjects)):
    print(f"{subjects[i]}: {marks[i]} marks")
    print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")  