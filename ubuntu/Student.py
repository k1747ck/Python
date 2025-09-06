# Program to store and display student data

# Step 1: Take input from the user
name = input("Enter student name: ")
age = int(input("Enter student age: "))
roll_no = input("Enter roll number: ")
course = input("Enter course name: ")

# Step 2: Store data in a dictionary
student = {
    "Name": name,
    "Age": age,
    "Roll No": roll_no,
    "Course": course
}

# Step 3: Print stored data
print("\n----- Student Details -----")
for key, value in student.items():
    print(f"{key}: {value}")
