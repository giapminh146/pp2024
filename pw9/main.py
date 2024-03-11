import tkinter as tk
from tkinter import messagebox
from domains.management_system import ManagementSystem
from domains.student import Student
from domains.course import Course

class StudentManagementGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Management System")
        self.system = ManagementSystem()

        self.create_menu()

    def create_menu(self):
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        file_menu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.master.quit)

        student_menu = tk.Menu(menu)
        menu.add_cascade(label="Students", menu=student_menu)
        student_menu.add_command(label="Input Number of Students", command=self.input_number_of_students)
        student_menu.add_command(label="Input Student Information", command=self.input_student_info)

        course_menu = tk.Menu(menu)
        menu.add_cascade(label="Courses", menu=course_menu)
        course_menu.add_command(label="Input Number of Courses", command=self.input_number_of_courses)
        course_menu.add_command(label="Input Course Information", command=self.input_course_info)

        action_menu = tk.Menu(menu)
        menu.add_cascade(label="Actions", menu=action_menu)
        action_menu.add_command(label="Select Courses", command=self.select_courses)
        action_menu.add_command(label="Input Marks", command=self.input_marks)
        action_menu.add_command(label="List Courses", command=self.list_courses)
        action_menu.add_command(label="List Students", command=self.list_students)
        action_menu.add_command(label="Show Marks", command=self.show_marks)
        action_menu.add_command(label="Sort Students by GPA", command=self.sort_students_by_gpa)

    def input_number_of_students(self):
        top = tk.Toplevel(self.master)
        top.title("Input Number of Students")

        label = tk.Label(top, text="Enter number of students:")
        label.pack()

        entry = tk.Entry(top)
        entry.pack()

        def save_number_of_students():
            try:
                num_students = int(entry.get())
                if num_students < 0:
                    messagebox.showerror("Error", "Number of students must be a non-negative integer")
                else:
                    self.system.set_number_of_students(num_students)
                    messagebox.showinfo("Success", f"Number of students set to {num_students}")
                    top.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number")

        save_button = tk.Button(top, text="Save", command=save_number_of_students)
        save_button.pack()

    def input_number_of_courses(self):
        top = tk.Toplevel(self.master)
        top.title("Input Number of Courses")

        label = tk.Label(top, text="Enter number of courses:")
        label.pack()

        entry = tk.Entry(top)
        entry.pack()

        def save_number_of_courses():
            try:
                num_courses = int(entry.get())
                if num_courses < 0:
                    messagebox.showerror("Error", "Number of courses must be a non-negative integer")
                else:
                    self.system.set_number_of_courses(num_courses)
                    messagebox.showinfo("Success", f"Number of courses set to {num_courses}")
                    top.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number")

        save_button = tk.Button(top, text="Save", command=save_number_of_courses)
        save_button.pack()

    def input_student_info(self):
        top = tk.Toplevel(self.master)
        top.title("Input Student Information")

        label_id = tk.Label(top, text="Student ID:")
        label_id.pack()

        entry_id = tk.Entry(top)
        entry_id.pack()

        label_name = tk.Label(top, text="Student Name:")
        label_name.pack()

        entry_name = tk.Entry(top)
        entry_name.pack()

        label_dob = tk.Label(top, text="Date of Birth (YYYY-MM-DD):")
        label_dob.pack()

        entry_dob = tk.Entry(top)
        entry_dob.pack()

        def save_student_info():
            student_id = entry_id.get()
            student_name = entry_name.get()
            student_dob = entry_dob.get()

            if not (student_id and student_name and student_dob):
                messagebox.showerror("Error", "Please fill in all fields")
                return

            if not self.system.check_for_valid_date(student_dob):
                messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD")
                return

            student = Student(student_id, student_name, student_dob)
            self.system.add_student(student)
            messagebox.showinfo("Success", "Student information saved successfully")
            top.destroy()

        save_button = tk.Button(top, text="Save", command=save_student_info)
        save_button.pack()

    def input_course_info(self):
        top = tk.Toplevel(self.master)
        top.title("Input Course Information")

        label_id = tk.Label(top, text="Course ID:")
        label_id.pack()

        entry_id = tk.Entry(top)
        entry_id.pack()

        label_name = tk.Label(top, text="Course Name:")
        label_name.pack()

        entry_name = tk.Entry(top)
        entry_name.pack()

        label_credits = tk.Label(top, text="Credits:")
        label_credits.pack()

        entry_credits = tk.Entry(top)
        entry_credits.pack()

        def save_course_info():
            course_id = entry_id.get()
            course_name = entry_name.get()
            credits = entry_credits.get()

            try:
                credits = int(credits)
                if credits <= 0:
                    messagebox.showerror("Error", "Credits must be a positive integer")
                    return
            except ValueError:
                messagebox.showerror("Error", "Credits must be a positive integer")
                return

            if not (course_id and course_name and credits):
                messagebox.showerror("Error", "Please fill in all fields")
                return

            course = Course(course_id, course_name, credits)
            self.system.add_course(course)
            messagebox.showinfo("Success", "Course information saved successfully")
            top.destroy()

        save_button = tk.Button(top, text="Save", command=save_course_info)
        save_button.pack()

    def select_courses(self):
        top = tk.Toplevel(self.master)
        top.title("Select Courses")

        label_student_id = tk.Label(top, text="Enter Student ID:")
        label_student_id.pack()

        entry_student_id = tk.Entry(top)
        entry_student_id.pack()

        label_course_ids = tk.Label(top, text="Enter Course IDs (comma separated):")
        label_course_ids.pack()

        entry_course_ids = tk.Entry(top)
        entry_course_ids.pack()

        def save_selected_courses():
            student_id = entry_student_id.get()
            course_ids = entry_course_ids.get().split(',')

            if not (student_id and course_ids):
                messagebox.showerror("Error", "Please fill in all fields")
                return

            for course_id in course_ids:
                if not self.system.check_course_exist(course_id.strip()):
                    messagebox.showerror("Error", f"Course with ID {course_id.strip()} does not exist")
                    return

            self.system.select_courses(student_id, course_ids)
            messagebox.showinfo("Success", f"Courses selected successfully for student {student_id}")
            top.destroy()

        save_button = tk.Button(top, text="Save", command=save_selected_courses)
        save_button.pack()

    def input_marks(self):
        top = tk.Toplevel(self.master)
        top.title("Input Marks")

        label_student_id = tk.Label(top, text="Enter Student ID:")
        label_student_id.pack()

        entry_student_id = tk.Entry(top)
        entry_student_id.pack()

        label_course_id = tk.Label(top, text="Enter Course ID:")
        label_course_id.pack()

        entry_course_id = tk.Entry(top)
        entry_course_id.pack()

        label_marks = tk.Label(top, text="Enter Marks:")
        label_marks.pack()

        entry_marks = tk.Entry(top)
        entry_marks.pack()

        def save_student_marks():
            student_id = entry_student_id.get()
            course_id = entry_course_id.get()
            marks = entry_marks.get()

            try:
                marks = float(marks)
            except ValueError:
                messagebox.showerror("Error", "Marks must be a number")
                return

            if not (student_id and course_id and marks):
                messagebox.showerror("Error", "Please fill in all fields")
                return

            if not self.system.check_student_course_exist(student_id, course_id):
                messagebox.showerror("Error", "Student or Course does not exist")
                return

            self.system.input_marks(student_id, course_id, marks)
            messagebox.showinfo("Success", "Marks saved successfully")
            top.destroy()

        save_button = tk.Button(top, text="Save", command=save_student_marks)
        save_button.pack()

    def list_courses(self):
        top = tk.Toplevel(self.master)
        top.title("List Courses")

        courses = self.system.list_courses()

        if not courses:
            label = tk.Label(top, text="No courses available")
            label.pack()
        else:
            for course in courses:
                label = tk.Label(top, text=course)
                label.pack()

    def list_students(self):
        top = tk.Toplevel(self.master)
        top.title("List Students")

        students = self.system.list_students()

        if not students:
            label = tk.Label(top, text="No students available")
            label.pack()
        else:
            for student in students:
                label = tk.Label(top, text=student)
                label.pack()

    def show_marks(self):
        top = tk.Toplevel(self.master)
        top.title("Show Marks")

        label_student_id = tk.Label(top, text="Enter Student ID:")
        label_student_id.pack()

        entry_student_id = tk.Entry(top)
        entry_student_id.pack()

        def display_student_marks():
            student_id = entry_student_id.get()

            if not student_id:
                messagebox.showerror("Error", "Please enter Student ID")
                return

            marks = self.system.show_marks(student_id)

            if not marks:
                label = tk.Label(top, text=f"No marks found for student {student_id}")
                label.pack()
            else:
                for course_id, mark in marks.items():
                    label = tk.Label(top, text=f"Course ID: {course_id}, Mark: {mark}")
                    label.pack()

        display_button = tk.Button(top, text="Display", command=display_student_marks)
        display_button.pack()

    def sort_students_by_gpa(self):
        top = tk.Toplevel(self.master)
        top.title("Sort Students by GPA")

        sorted_students = self.system.sort_students_by_gpa()

        if not sorted_students:
            label = tk.Label(top, text="No students available")
            label.pack()
        else:
            for student in sorted_students:
                label = tk.Label(top, text=student)
                label.pack()


def main():
    root = tk.Tk()
    app = StudentManagementGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
