from input import *
from output import *
from domains.student import Student


class ManagementSystem:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__selected_courses = set()

    def read_data_from_files(self):
        try:
            with open('students.txt', 'r') as f:
                for line in f:
                    student_id, student_name, student_dob = line.strip().split(' - ')
                    student = Student(student_id, student_name, student_dob)
                    self.__students.append(student)

            with open('courses.txt', 'r') as f:
                for line in f:
                    course_id, course_name, credits = line.strip().split(' - ')
                    course = Course(course_id, course_name, int(credits))
                    self.__courses.append(course)

            with open('marks.txt', 'r') as f:
                for line in f:
                    course_name, student_info, mark = line.strip().split(' - ')
                    student_name, student_id = student_info.strip('()').split('(')
                    student = next((s for s in self.__students if s.get_student_id() == student_id), None)
                    if student:
                        student.get_marks()[course_name] = float(mark)

        except IOError as e:
            print(f"Error reading from files: {e}")

    def get_students(self):
        return self.__students

    def get_courses(self):
        return self.__courses

    def get_selected_courses(self):
        return self.__selected_courses

    def input_number_of_students(self, stdscr):
        return input_number_of_students(self, stdscr)

    def check_for_valid_date(self, date):
        return check_for_valid_date(self, date)

    def input_student_info(self, number_of_students, stdscr):
        return input_student_info(self, number_of_students, stdscr)

    def input_number_of_courses(self, stdscr):
        return input_number_of_courses(self, stdscr)

    def input_course_info(self, number_of_courses, stdscr):
        return input_course_info(self, number_of_courses, stdscr)

    def input_marks(self, stdscr):
        return input_marks(self, stdscr)

    def select_courses(self, stdscr):
        return select_courses(self, stdscr)

    def list_courses(self, stdscr):
        return list_courses(self, stdscr)

    def list_students(self, stdscr):
        return list_students(self, stdscr)

    def show_marks(self, stdscr):
        return show_marks(self, stdscr)

    def calc_gpa(self, courses):
        return calc_gpa(self, courses)

    def sort_gpa(self, stdscr):
        return sort_gpa(self, stdscr)




