
'''
                                    Tasrif Nur Himel

Python problem - 2D List Assignment


1. take student id, name and gpa as input for 5 students.

2. store them in a 2D list.

3. print information of each student using a loop.

4. print information of the stduent who has highest gpa.

5. print the information of the student with the first/lowest id.

6. calculate the highest, lowest and avg gpa from the student gpas.

'''

student = []

for i in range(5):
    std_id = input(f"Enter {i+1} no Student ID: ")
    std_name = input(f"Enter {i+1} no Student Name: ")
    std_gpa = input(f"Enter {i+1} no Student GPA: ")
    print("\n")

    std_list = [std_id, std_name, std_gpa]

    student.append(std_list)

print("\nStudent data entered successfully!")

print("Information of each student:\n")

for i in student:
    print(f"Student ID: {i[0]}")
    print(f"Student Name: {i[1]}")
    print(f"Student GPA: {i[2]}")
    print("-" * 20)

def find_highest_gpa_student(student):
    highest_gpa = max(float(i[2]) for i in student)
    for i in student:
        if float(i[2]) == highest_gpa:
            return i
    return None 

highest_gpa_student = find_highest_gpa_student(student)

if highest_gpa_student:
    print("\nStudent with the highest GPA:")
    print(f"Student ID: {highest_gpa_student[0]}")
    print(f"Student Name: {highest_gpa_student[1]}")
    print(f"Student GPA: {highest_gpa_student[2]}")
else:
    print("\nNo student has the highest GPA (all GPAs are the same).")

print("-" * 20)

sorted_students_id = sorted(student, key = lambda x: x[0])
lowest_id_student = sorted_students_id[0]
print("Student with the lowest ID:")
print("Student ID:", lowest_id_student[0])
print("Student Name:", lowest_id_student[1])
print("Student GPA:", lowest_id_student[2])

print("\n")
print('Calculate the highest, lowest, and average GPA from the student GPAs:')

gpas = [float(i[2]) for i in student]
highest_gpa = max(gpas)
lowest_gpa = min(gpas)
average_gpa = sum(gpas) / len(gpas)

print("Highest GPA:", highest_gpa)
print("Lowest GPA:", lowest_gpa)
print("Average GPA:", average_gpa)