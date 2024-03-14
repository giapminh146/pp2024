import tkinter as tk
from tkinter import messagebox
import math
import os
import pickle
import zipfile
import threading
from domains.student import Student
from domains.course import Course

class SaveDataThread(threading.Thread):
    def __init__(self, data, filename):
        super().__init__()
        self.data = data
        self.filename = filename

    def run(self):
        try:
            with open(self.filename, 'wb') as file:
                pickle.dump(self.data, file)
        except IOError:
            print(f"Error saving data: {IOError}")


def save_students_info(student_information_list):
    try:
        existing_students = []
        try:
            with open('students.pickle', 'rb') as file:
                existing_students = pickle.load(file)
        except FileNotFoundError:
            pass
        existing_students.extend(student_information_list)
        SaveDataThread(existing_students, 'students.pickle').start()
    except IOError:
        print(f"Error saving students information: {IOError}")


def save_courses_info(course_information_list):
    try:
        existing_courses = []
        try:
            with open('courses.pickle', 'rb') as file:
                existing_courses = pickle.load(file)
        except FileNotFoundError:
            pass
        existing_courses.extend(course_information_list)
        SaveDataThread(existing_courses, 'courses.pickle').start()
    except IOError:
        print(f"Error saving courses information: {IOError}")


def save_marks(self, stdscr):
    selected_course = next(iter(self.get_selected_courses()), None)
    if selected_course is None:
        stdscr.addstr("Please select a course first.")
        stdscr.refresh()
        return

    try:
        marks_data = []
        try:
            with open('marks.pickle', 'rb') as file:
                marks_data = pickle.load(file)
        except FileNotFoundError:
            pass

        for student in self.get_students():
            student_id = student.get_student_id()
            student_name = student.get_student_name()
            if selected_course.get_course_name() in student.get_marks():
                marks_data.append((selected_course.get_course_name(), student_name, student_id, student.get_marks()[selected_course.get_course_name()]))
        SaveDataThread(marks_data, 'marks.pickle').start()
    except IOError:
        print(f"Error saving marks: {IOError}")


def compress_files():
    try:
        with zipfile.ZipFile('students.dat', 'w') as zip:
            zip.write('students.pickle')
            zip.write('courses.pickle')
            zip.write('marks.pickle')
    except IOError:
        print(f"Error compressing files: {IOError}")


def decompress_files():
    if os.path.exists('students.dat'):
        try:
            with zipfile.ZipFile('students.dat', 'r') as zip:
                zip.extractall('.')
        except IOError:
            print(f"Error decompressing files: {IOError}")



def check_for_valid_date(date):
    if len(date) != 10:
        return False

    if date[4] != "-" or date[7] != "-":
        return False

    year, month, day = date.split("-")

    try:
        year = int(year)
        month = int(month)
        day = int(day)

        if month < 1 or month > 12:
            return False

        if day < 1 or day > 31:
            return False

        if year < 0:
            return False

        return True
    except ValueError:
        return False

def input_student_info(number_of_students):
    student_information_list = []

    for _ in range(number_of_students):
        student_information = {}

        student_id = student_id_entry.get()
        student_name = student_name_entry.get()
        student_dob = student_dob_entry.get()

        if student_id not in [student.get_student_id() for student in get_students()]:
            messagebox.showerror("Error", "Please enter a unique ID for the student.")
            return

        if not check_for_valid_date(student_dob):
            messagebox.showerror("Error", "Please enter a valid format of date (YYYY-MM-DD).")
            return

        student_information["student_id"] = student_id
        student_information["student_name"] = student_name
        student_information["student_DoB"] = student_dob

        a_student = Student(student_id, student_name, student_dob)
        student_information_list.append(student_information)

    save_students_info(student_information_list)

def input_number_of_students():
    top_window = tk.Toplevel()
    top_window.title("Enter number of students")
    top_window.geometry("400x200")

    no_label = tk.Label(top_window, text="Enter number of students to add:")
    no_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    number_of_students_entry = tk.Entry(top_window)
    number_of_students_entry.grid(row=0, column=1, padx=5, pady=5, sticky="e")

    def close_window():
        top_window.destroy()

    def save_number_of_student():
        error_label.config(text="")  # Reset error labels
        error2_label.config(text="")

        try:
            number_of_students = int(number_of_students_entry.get())
            if number_of_students >= 0:
                input_student_info(number_of_students)
                success_label.config(text="Save Successful!", fg="green")
            else:
                error_label.config(text="Please enter a valid positive number")
        except ValueError:
            error2_label.config(text="Please enter a valid number")

    submit_button = tk.Button(top_window, text="Submit", command=save_number_of_student)
    submit_button.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    back_button = tk.Button(top_window, text="Back", command=close_window)
    back_button.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    error_label = tk.Label(top_window, text="", fg="red")
    error_label.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

    error2_label = tk.Label(top_window, text="", fg="red")
    error2_label.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

    success_label = tk.Label(top_window, text="", fg="green")
    success_label.grid(row=4, column=0, padx=5, pady=5, columnspan=2)

    window =tk.Tk()
    window.title("Enter student information")

    student_id_label = tk.Label(window, text="Student ID:")
    student_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    student_id_entry = tk.Entry(window)
    student_id_entry.grid(row=0, column=1, padx=5, pady=5)

    student_name_label = tk.Label(window, text="Student Name:")
    student_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    student_name_entry = tk.Entry(window)
    student_name_entry.grid(row=1, column=1, padx=5, pady=5)

    student_dob_label = tk.Label(window, text="Date of Birth (YYYY-MM-DD):")
    student_dob_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    student_dob_entry = tk.Entry(window)
    student_dob_entry.grid(row=2, column=1, padx=5, pady=5)

    # Button to open the input window
    open_button = tk.Button(window, text="Open Input Window", command=input_number_of_students)
    open_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


'''def input_number_of_courses(self, stdscr):
    curses.echo()
    stdscr.clear()
    stdscr.addstr("Enter number of courses to add: ")
    stdscr.refresh()
    number_of_courses = stdscr.getstr().decode()
    stdscr.clear()
    stdscr.refresh()
    while True:
        try:
            number_of_courses = int(number_of_courses)
            if number_of_courses >= 0:
                return number_of_courses
            else:
                stdscr.clear()
                stdscr.addstr("Please enter a positive number of courses.\n")
                stdscr.addstr("Enter number of courses to add: ")
                stdscr.refresh()
                number_of_courses = stdscr.getstr().decode()
        except ValueError:
            stdscr.clear()
            stdscr.addstr("Please enter a valid number of courses.\n")
            stdscr.addstr("Enter number of courses to add: ")
            stdscr.refresh()
            number_of_courses = stdscr.getstr().decode()


def input_course_info(self, number_of_courses, stdscr):
    course_information_list = []
    if number_of_courses == 0:
        stdscr.addstr("There is no course.")
        stdscr.refresh()
    else:
        for _ in range(number_of_courses):
            course_info = {}
            while True:
                stdscr.addstr("Enter the ID of the course: ")
                stdscr.refresh()
                course_id = stdscr.getstr().decode()
                if course_id not in [course.get_course_id() for course in self.get_courses()]:
                    break
                else:
                    stdscr.clear()
                    stdscr.addstr("Please enter a unique ID for the course.\n")
                    stdscr.refresh()

            while True:
                stdscr.clear()
                stdscr.addstr("Enter the name for the course: ")
                stdscr.refresh()
                course_name = stdscr.getstr().decode()
                if course_name not in [course.get_course_name() for course in self.get_courses()]:
                    break
                else:
                    stdscr.addstr("Please enter a unique course name.\n")
                    stdscr.refresh()

            while True:
                stdscr.addstr("Enter the credits for the course: ")
                stdscr.refresh()
                credits = stdscr.getstr().decode()
                try:
                    credits = int(credits)
                    if credits <= 0:
                        stdscr.clear()
                        stdscr.addstr("Please enter a valid credits for the course.\n")
                        stdscr.refresh()
                    else:
                        break
                except ValueError:
                    stdscr.clear()
                    stdscr.addstr("Please enter a valid credits for the course.\n")
                    stdscr.refresh()

            stdscr.clear()
            stdscr.addstr("\n")
            course_info["course_id"] = course_id
            course_info["course_name"] = course_name
            course_info["credits"] = credits
            a_course = Course(course_id, course_name, credits)
            self.get_courses().append(a_course)
            course_information_list.append(course_info)
    save_courses_info(course_information_list)
    return course_information_list


def input_marks(self, stdscr):
    selected_course = next(iter(self.get_selected_courses()), None)
    if selected_course is None:
        stdscr.addstr("Please select a course first.\n")
        stdscr.refresh()
        return

    stdscr.addstr(f"You are currently in course: {selected_course}\n")
    for student in self.get_students():
        student_id = student.get_student_id()
        student_name = student.get_student_name()

        if selected_course.get_course_name() in student.get_marks():
            stdscr.addstr(f"Mark already entered for {student_name} (ID: {student_id}) in course: {selected_course}\n")
            continue

        while True:
            stdscr.addstr(f"Enter the mark for student {student_name} (ID: {student_id}): ")
            stdscr.refresh()
            mark = stdscr.getstr().decode()
            try:
                mark = float(mark)
                if mark < 0.0:
                    stdscr.clear()
                    stdscr.addstr("Please enter a positive mark.\n")
                    stdscr.refresh()
                    continue
                mark = math.floor(mark * 10) / 10
                student.get_marks()[selected_course.get_course_name()] = mark
                break
            except ValueError:
                stdscr.addstr("Please enter a valid mark.\n")
                stdscr.refresh()
    save_marks(self, stdscr)
    self.get_selected_courses().clear()'''
