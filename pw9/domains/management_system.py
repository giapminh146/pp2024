from input import *
from output import *
import pickle
from domains.student import Student


class ManagementSystem:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__selected_courses = set()

    def set_number_of_students(self, num_students):
        self.students = [None] * num_students

    def set_number_of_courses(self, num_courses):
        self.courses = [None] * num_courses

    def add_student(self, student):
        self.get_students().append(student)

    def add_course(self, course):
        self.get_courses().append(course)

    def read_data_from_files(self):
        try:
            with open('students.pickle', 'rb') as file:
                students_data = pickle.load(file)
                for student_info in students_data:
                    student_id = student_info["student_id"]
                    student_name = student_info["student_name"]
                    student_dob = student_info["student_DoB"]
                    student = Student(student_id, student_name, student_dob)
                    self.__students.append(student)

            with open('courses.pickle', 'rb') as file:
                courses_data = pickle.load(file)
                for course_info in courses_data:
                    course_id = course_info["course_id"]
                    course_name = course_info["course_name"]
                    credits = course_info["credits"]
                    course = Course(course_id, course_name, credits)
                    self.__courses.append(course)

            with open('marks.pickle', 'rb') as file:
                marks_data = pickle.load(file)
                for mark_info in marks_data:
                    course_name = mark_info[0]
                    student_name = mark_info[1]
                    student_id = mark_info[2]
                    mark = mark_info[3]
                    student = next((s for s in self.__students if s.get_student_id() == student_id), None)
                    if student:
                        student.get_marks()[course_name] = mark

        except FileNotFoundError:
            print(f"Error finding the files: {FileNotFoundError}")
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




