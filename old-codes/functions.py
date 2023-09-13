#!/usr/bin/env python3

students = []


# make the name of the student to title case
def get_students_titlecase():
    students_titlecase = {}
    for student in students:
        students_titlecase[student["name"].title()] = student["student_id"]
    return students_titlecase


# print the name of the student
def print_student_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


# append student name and id to the dictionary
def add_student(name, student_id = 332):
    student = {"name":name, "student_id":student_id}
    students.append(student)


def save_file(name_list):
    print("hello world")
    try:
        f = open("students.txt", "a")
        for name in name_list:
            f.write(name + ": " + name_list["name"] + "\n")
        f.close()
    except Exception:
        print("could not read the file")


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            print(student)
            add_student(student)
        f.close()
    except Exception:
        print("could not read file")


if __name__ == "__main__":

    read_file()

    while(True):
        student_name = input("enter student name: ")

        if student_name == "exit":
            break

        student_id = input("enter student id: ")

        add_student(student_name, student_id)

    student_list = get_students_titlecase()
    print_student_titlecase()
    save_file(student_list)
