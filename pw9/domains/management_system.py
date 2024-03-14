import tkinter as tk
from tkinter import simpledialog, messagebox
from domains.student import Student
from domains.course import Course
import pickle
import os

class ManagementSystem:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__selected_courses = set()
        self.marks = {}

    def save_course_data(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.courses, file)

    def save_student_data(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.students, file)

    def save_mark_data(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.marks, file)

    def load_course_data(self, filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                self.courses = pickle.load(file)

    def load_student_data(self, filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                self.students = pickle.load(file)

    def load_mark_data(self, filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                self.marks = pickle.load(file)

    def get_students(self):
        return self.__students

    def get_courses(self):
        return self.__courses

    def get_selected_courses(self):
        return self.__selected_courses

    def input_number_of_students(self):
        root = tk.Tk()
        root.withdraw()
        num_students = simpledialog.askinteger("Input", "Enter the number of students:")
        root.destroy()
        return num_students

    def input_student_info(self, number_of_students):
        student_information_list = []
        for _ in range(number_of_students):
            student_information = {}
            student_id = simpledialog.askstring("Input", "Enter the ID of the student:")
            student_name = simpledialog.askstring("Input", "Enter the name of the student:")
            student_dob = simpledialog.askstring("Input", "Enter the date of birth for the student (YYYY-MM-DD):")
            student_information["student_id"] = student_id
            student_information["student_name"] = student_name
            student_information["student_DoB"] = student_dob
            a_student = Student(student_id, student_name, student_dob)
            self.__students.append(a_student)
            student_information_list.append(student_information)
        self.save_students_info(student_information_list)

    def input_number_of_courses(self, num_courses):
        return num_courses

    def input_course_info(self, number_of_courses):
        course_information_list = []
        for _ in range(number_of_courses):
            course_info = {}
            course_id = simpledialog.askstring("Input", "Enter the ID of the course:")
            course_name = simpledialog.askstring("Input", "Enter the name of the course:")
            credits = simpledialog.askinteger("Input", "Enter the credits for the course:")
            course_info["course_id"] = course_id
            course_info["course_name"] = course_name
            course_info["credits"] = credits
            a_course = Course(course_id, course_name, credits)
            self.__courses.append(a_course)
            course_information_list.append(course_info)
        self.save_courses_info(course_information_list)

    def select_courses(self):
        selected_courses = simpledialog.askstring("Input", "Enter the courses separated by comma:")
        courses = selected_courses.split(',')
        for course_name in courses:
            course = next((c for c in self.__courses if c.get_name() == course_name.strip()), None)
            if course:
                self.__selected_courses.add(course)
            else:
                messagebox.showerror("Error", f"Course '{course_name.strip()}' not found.")

    def list_courses(self):
        course_names = [course.get_name() for course in self.__courses]
        messagebox.showinfo("Courses", "\n".join(course_names))

    def list_students(self):
        student_info = ""
        for student in self.__students:
            student_info += f"ID: {student.get_student_id()}, Name: {student.get_name()}, DoB: {student.get_dob()}\n"
        messagebox.showinfo("Students", student_info)


    def set_mark(self, student_id, course_name, mark):
        if student_id not in self.marks:
            self.marks[student_id] = {}
        self.marks[student_id][course_name] = mark

    def get_marks(self, course_name):
        marks_for_course = {}
        for student_id, marks in self.marks.items():
            if course_name in marks:
                marks_for_course[student_id] = marks[course_name]
        return marks_for_course

    def sort_gpa(self):
        self.__students.sort(key=lambda x: x.calculate_gpa(), reverse=True)
        self.list_students()

    def save_students_info(self, student_information_list):
        try:
            existing_students = []
            try:
                with open('students.pickle', 'rb') as file:
                    existing_students = pickle.load(file)
            except FileNotFoundError:
                pass
            existing_students.extend(student_information_list)
            with open('students.pickle', 'wb') as file:
                pickle.dump(existing_students, file)
        except IOError:
            messagebox.showerror("Error", "Error saving students information")

    def save_courses_info(self, course_information_list):
        try:
            existing_courses = []
            try:
                with open('courses.pickle', 'rb') as file:
                    existing_courses = pickle.load(file)
            except FileNotFoundError:
                pass
            existing_courses.extend(course_information_list)
            with open('courses.pickle', 'wb') as file:
                pickle.dump(existing_courses, file)
        except IOError:
            messagebox.showerror("Error", "Error saving courses information")
