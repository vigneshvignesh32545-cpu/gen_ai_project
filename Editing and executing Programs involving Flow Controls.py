# Program: Student Marks Analysis using Flow Control

# Step 1: Read number of students
n = int(input("Enter number of students: "))

# Step 2: Loop through each student
for i in range(1, n + 1):
    print("\nStudent", i)

    # Step 3: Read marks
    marks = int(input("Enter marks (0-100): "))

    # Step 4: Flow control using if-elif-else
    if marks >= 90:
        grade = "A"
        result = "Pass"
    elif marks >= 75:
        grade = "B"
        result = "Pass"
    elif marks >= 50:
        grade = "C"
        result = "Pass"
    elif marks >= 0:
        grade = "F"
        result = "Fail"
    else:
        print("Invalid marks entered")
        continue   # skip to next student

    # Step 5: Display result
    print("Grade:", grade)
    print("Result:", result)
