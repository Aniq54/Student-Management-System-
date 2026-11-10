
import json
import os

FILE_NAME = "students.json"


def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


students = load_students()


def add_student():
    roll = input("Enter Roll Number: ")

    for student in students:
        if student["roll"] == roll:
            print("Roll number already exists!")
            return

    name = input("Enter Student Name: ")
    marks = float(input("Enter Marks (out of 100): "))

    if marks < 0 or marks > 100:
        print("Invalid marks!")
        return

    student = {
        "roll": roll,
        "name": name,
        "marks": marks
    }

    students.append(student)
    save_students()

    print("Student added successfully!")


def display_students():
    if not students:
        print("No student records found.")
        return

    print("\n--- STUDENT RECORDS ---")

    for student in students:
        print("Roll Number:", student["roll"])
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("----------------------")


def search_student():
    roll = input("Enter Roll Number to search: ")

    for student in students:
        if student["roll"] == roll:
            print("Student Found!")
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            print("Percentage:", student["marks"], "%")
            return

    print("Student not found!")


def update_student():
    roll = input("Enter Roll Number to update: ")

    for student in students:
        if student["roll"] == roll:
            student["name"] = input("Enter new name: ")

            marks = float(input("Enter new marks: "))

            if marks < 0 or marks > 100:
                print("Invalid marks!")
                return

            student["marks"] = marks
            save_students()

            print("Record updated successfully!")
            return

    print("Student not found!")


def delete_student():
    roll = input("Enter Roll Number to delete: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            save_students()
            print("Student deleted successfully!")
            return

    print("Student not found!")


def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice! Try again.")


main()
