"""
Dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

left side =key
right  side = value

jaise example 
{key1:value1, key2:value2, key3:value3}

add , update,delete,view,exit

.item display kardega student aur grade ko
"""
student_grades = { }
#add student
def add_student(name,grade):
    student_grades[name] = grade
    print(f"Student {name} added with grade {grade}.")

#to update the student
def update_student(name,grade):
   if name in student_grades:
         student_grades[name] = grade
         print(f"{name} with marks are updated {grade}.")
   else:
        print(f" {name} not found.")   
# to delete the student 
def delete_student(name):
     if name in student_grades:
            del student_grades[name]
            print(f"{name} deleted successfully.")
     else:
            print(f"{name} not found.")
# to view the student
def display_all_students():            
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    else:
        print("No students found/added.")


def main():
    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Exit")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            name = input("Enter student name: ")
            grade = int(input("Enter student grade: "))
            add_student(name, grade)
        elif choice == 2:
            name = input("Enter student name to update: ")
            grade = int(input("Enter new grade: "))
            update_student(name, grade)
        elif choice == 3:
            name = input("Enter student name to delete: ")
            delete_student(name)
        elif choice == 4:
            display_all_students()
        elif choice == 5:
            print("Exiting the program.")
            
            break
        else:
            print("Invalid choice! Please select a valid option.")     

if __name__ == "__main__":
    main() 