"""ITF 08 Final Project Attendance System
# TODO 1
Name : Tasneem Mosabeh
Delivery Date : 31/8/2023
"""
import uuid



# TODO 2
class Course:
    def __init__(self,course_name, course_mark):
         self.course_id = str(uuid.uuid4())
         self.course_name = course_name
         self.course_mark = course_mark

# TODO 3
class Student:
    total_students = 0

    # TODO 4
    def __init__(self, student_name, student_age, student_number):
        self.student_id = uuid.uuid4()
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []
        Student.total_students += 1

        # TODO 5

    def enroll_new_course(self, new_course_name, new_course_mark):
        new_course = Course(new_course_name, new_course_mark)
        self.courses_list.append(new_course)

        # TODO 6

    def get_student_courses(self):
        for course in self.courses_list:
            print(f"Course: {course.course_name}, Mark: {course.course_mark}")

            # TODO 7

    def get_student_average(self):
        marks = [course.course_mark for course in self.courses_list]
        if not marks:
            return 0

        total_sum = sum(marks)
        average = total_sum / len(marks)
        return average


    # TODO 8

students = []

while True:
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Add Course to student with mark.\n"
                              "5.Get Student Average\n"
                              "6.Exit\n"
                              "Enter Your Choice : "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

    if selection == 1:
        student_number = input("Enter Student Number: ")

        # TODO 10
        if any(student.student_number == student_number for student in students):
            print("The student number already exists.")
            continue

        student_name = input("Enter Student Name: ")
        while True:
            try:
                student_age = int(input("Enter Student Age: "))
                break
            except ValueError:
                print("Invalid Value. Please enter a valid age.")

        new_student = Student(student_name, student_age,student_number)
        students.append(new_student)

        print("Student Added Successfully.")

    elif selection == 2:
        student_number = input("Enter Student Number: ")
        # TODO 12
        index_to_remove = None
        for index, student in enumerate(students):
            if student.student_number == student_number:
                index_to_remove = index
                break

        if index_to_remove is not None:
            removed_student = students.pop(index_to_remove)
            print(f"Student {removed_student.student_name} with student number {student_number} has been deleted.")
        else:
            print("Student not found with the given student number.")

    elif selection == 3:
        student_number = input("Enter Student Number: ")
        # TODO 13
        target_student = None
        for student in students:
            if student.student_number == student_number:
                target_student = student
                break

        if target_student is not None:
            print("Student Information:")
            print("Student Number:", target_student.student_number)
            print("Student Name:", target_student.student_name)
            print("Student Age:", target_student.student_age)
        else:
            print("Student not found with the given student number.")

    elif selection == 4:
        student_number = input("Enter Student Number: ")

        # TODO 14
        target_student = None
        for student in students:
            if student.student_number == student_number:
                target_student = student
                break

        if target_student is not None:
            while True:
                course_name = input("Enter Course Name (or 'exit' to finish): ")
                if course_name.lower() == "exit":
                    break

                try:
                    course_mark = float(input("Enter Course Mark: "))
                    target_student.enroll_new_course(course_name, course_mark)
                    print(
                        f"Course {course_name} with mark {course_mark} added to student {target_student.student_name}'s courses.")
                except ValueError:
                    print("Invalid input. Please enter a valid course mark.")
        else:
            print("Student not found with the given student number.")


    elif selection == 5:
        student_number = input("Enter Student Number: ")
        # TODO 15
        target_student = None
        for student in students:
            if student.student_number == student_number:
                target_student = student
                break

        if target_student is not None:
            average = target_student.get_student_average()
            print(f"Student {target_student.student_name}'s average: {average}")
        else:
            print("Student not found with the given student number.")

   #TODO 16
    elif selection == 6:
        # TODO 16
        print("Exiting the program.")
        break
    else:
        print("Invalid selection. Please choose a valid option.")