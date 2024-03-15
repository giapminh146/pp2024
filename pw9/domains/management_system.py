import tkinter as tk
from tkinter import simpledialog, messagebox
from domains.student import Student
from domains.course import Course
import pickle
import os
import datetime
from datetime import datetime

class ManagementSystem:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__selected_courses = set()
        self.marks = {}

    def load_course_data(self, filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                course_data = pickle.load(file)
                self.__courses = [Course(**course_info) for course_info in course_data]

    def load_student_data(self, filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                student_data = pickle.load(file)
                self.__students = [Student(**student_info) for student_info in student_data]

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

    def validate_date_format(self, date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False


    def input_student_info(self, number_of_students):
        if number_of_students < 0:
            messagebox.showerror("Error", "Number of students must be greater than or equal 0.")
            return

        student_information_list = []
        existing_ids = set(student.get_student_id() for student in self.__students)

        for _ in range(number_of_students):
            student_information = {}
            while True:
                student_id = simpledialog.askstring("Input", "Enter the ID of the student:")
                if student_id in existing_ids:
                    messagebox.showerror("Error", "Student ID already exists.")
                else:
                    existing_ids.add(student_id)
                    student_information["student_id"] = student_id
                    break

            student_name = simpledialog.askstring("Input", "Enter the name of the student:")
            student_information["student_name"] = student_name

            while True:
                student_dob = simpledialog.askstring("Input", "Enter the date of birth for the student (YYYY-MM-DD):")
                if not self.validate_date_format(student_dob):
                    messagebox.showerror("Error", "Invalid date format. Date must be in the form YYYY-MM-DD.")
                else:
                    student_information["student_DoB"] = student_dob
                    break

            a_student = Student(**student_information)
            self.__students.append(a_student)
            student_information_list.append(student_information)

        messagebox.showinfo("Success", "Student information added successfully.")
        self.save_students_info(student_information_list)


    def input_course_info(self, number_of_courses):
        if number_of_courses < 0:
            messagebox.showerror("Error", "Number of courses must be greater than 0.")
            return

        course_information_list = []
        existing_ids = set(course.get_course_id() for course in self.__courses)

        for _ in range(number_of_courses):
            course_info = {}
            while True:
                course_id = simpledialog.askstring("Input", "Enter the ID of the course:")
                if course_id in existing_ids:
                    messagebox.showerror("Error", "Course ID already exists.")
                else:
                    existing_ids.add(course_id)
                    course_info["course_id"] = course_id
                    break

            course_name = simpledialog.askstring("Input", "Enter the name of the course:")
            course_info["course_name"] = course_name
            while True:
                credits = simpledialog.askinteger("Input", "Enter the credits for the course:")
                if credits <= 0:
                    messagebox.showerror("Error", "Credits must be greater than 0.")
                else:
                    course_info["credits"] = credits
                    break

            a_course = Course(**course_info)
            self.__courses.append(a_course)
            course_information_list.append(course_info)
        messagebox.showinfo("Success", "Course information added successfully.")
        self.save_courses_info(course_information_list)


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

    def calculate_student_gpa(self, student):
        total_mark = 0
        total_credits = 0
        for course in self.__courses:
            course_name = course.get_course_name()
            if course_name in self.marks.get(student.get_student_id(), {}):
                mark = self.marks[student.get_student_id()][course_name]
                credits = course.get_credits()
                total_mark += mark * credits
                total_credits += credits
        if total_credits == 0:
            return 0
        return total_mark / total_credits


    def sort_gpa(self):
        sorted_students = sorted(self.__students, key=self.calculate_student_gpa, reverse=True)
        return sorted_students

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

    def save_marks_info(self):
        try:
            with open('marks.pickle', 'wb') as file:
                pickle.dump(self.marks, file)
            messagebox.showinfo("Success", "Marks information saved successfully.")
        except IOError:
            messagebox.showerror("Error", "Error saving marks information")


