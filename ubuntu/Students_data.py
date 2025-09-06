# Program to store and display multiple student data

# Step 1: Create a list to hold all students
students = []

# Step 2: Ask how many students
n = int(input("Enter number of students: "))

# Step 3: Loop to take input for each student
for i in range(n):
    print(f"\nEnter details for student {i+1}:")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    roll_no = input("Enter roll number: ")
    course = input("Enter course name: ")

    # Store in dictionary
    student = {
        "Name": name,
        "Age": age,
        "Roll No": roll_no,
        "Course": course
    }
    
    # Add to list
    students.append(student)

# Step 4: Print all student details
print("\n----- All Student Details -----")
for i, student in enumerate(students, start=1):
    print(f"\nStudent {i}:")
    for key, value in student.items():
        print(f"{key}: {value}")
