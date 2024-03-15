import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
from domains.management_system import ManagementSystem


class MainApplication:
    def __init__(self, master):
        self.selected_course = None
        self.master = master
        self.master.title("Student Management System")
        self.system = ManagementSystem()
        self.number_of_students = 0
        self.number_of_courses = 0

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.master, text="Welcome to the Student Management System", font=("Helvetica", 16))
        title_label.pack(pady=20)

        buttons_frame = tk.Frame(self.master)
        buttons_frame.pack(pady=10)

        button_texts = ["Input students information", "Input course information", "Select courses", "Input marks",
                        "List courses", "List students", "Show marks", "Sort students by GPA", "Load Course Data",
                        "Load Student Data", "Load Mark Data", "Exit"]
        button_commands = [self.input_student_info, self.input_course_info, self.select_course, self.call_input_marks,
                           self.list_courses, self.list_students, self.show_marks, self.sort_gpa, self.load_course_data,
                           self.load_student_data, self.load_mark_data, self.master.quit]

        for text, command in zip(button_texts, button_commands):
            self.create_button(buttons_frame, text, command)

    def create_button(self, frame, text, command):
        button = tk.Button(frame, text=text, command=command, bg="#4CAF50", fg="white", font=("Helvetica", 12),
                           width=30)
        button.pack(pady=5)

    def load_data(self, data_type):
        filename = filedialog.askopenfilename(filetypes=[("Pickle files", "*.pickle")])
        if filename:
            getattr(self.system, f"load_{data_type}_data")(filename)
            messagebox.showinfo("Success", f"{data_type.capitalize()} data loaded successfully.")

    def input_student_info(self):
        num_students = simpledialog.askstring("Input", "Enter the number of students", parent=self.master)
        try:
            num_students = int(num_students)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for number of students.")
            return
        self.system.input_student_info(num_students)

    def input_course_info(self):
        num_courses = simpledialog.askstring("Input", "Enter the number of courses", parent=self.master)
        try:
            num_courses = int(num_courses)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for number of courses.")
            return
        self.system.input_course_info(num_courses)

    def select_course(self):
        if not self.system.get_courses():
            messagebox.showerror("Error", "No courses available. Please input course information first.")
            return

        def on_course_selected(course):
            self.selected_course = course
            messagebox.showinfo("Success", f"Course '{course.get_course_name()}' selected successfully.")
            select_window.destroy()

        select_window = tk.Toplevel(self.master)
        select_window.title("Select a Course")

        for course in self.system.get_courses():
            course_button = tk.Button(select_window, text=course.get_course_name(),
                                      command=lambda c=course: on_course_selected(c), width=30)
            course_button.pack(pady=5)

    def input_marks(self, selected_course):
        if not self.system.get_students():
            messagebox.showerror("Error", "Please input student information first.")
            return

        if not self.system.get_courses():
            messagebox.showerror("Error", "Please input course information first.")
            return

        if not selected_course:
            messagebox.showerror("Error", "Please select a course first.")
            return

        input_marks_window = tk.Toplevel(self.master)
        input_marks_window.title(f"Input Marks for Students in {selected_course.get_course_name()}")

        students = self.system.get_students()
        for student in students:
            frame = tk.Frame(input_marks_window)
            frame.pack(padx=10, pady=5, fill=tk.X)

            label = tk.Label(frame, text=f"{student.get_student_name()} (ID: {student.get_student_id()}):", anchor="w")
            label.pack(side=tk.LEFT)

            entry_var = tk.StringVar()
            entry = tk.Entry(frame, textvariable=entry_var)
            entry.pack(side=tk.LEFT, padx=10)

            def set_mark(student=student, entry_var=entry_var):
                try:
                    mark = float(entry_var.get())
                    self.system.set_mark(student.get_student_id(), selected_course.get_course_name(), mark)
                    self.system.save_marks_info()
                    messagebox.showinfo("Success",
                                        f"Mark set for {student.get_student_name()} in {selected_course.get_course_name()}: {mark}")
                except ValueError:
                    messagebox.showerror("Error", "Invalid mark. Please enter a numeric value.")

            submit_button = tk.Button(frame, text="Set Mark", command=set_mark, bg="#4CAF50", fg="white", width=10)
            submit_button.pack(side=tk.RIGHT)

    def call_input_marks(self):
        if hasattr(self, 'selected_course'):
            self.input_marks(self.selected_course)
        else:
            messagebox.showerror("Error", "Please select a course first.")

    def list_courses(self):
        if not self.system.get_courses():
            messagebox.showerror("Error", "No courses available.")
            return

        messagebox.showinfo("Courses", "\n".join([str(course) for course in self.system.get_courses()]))

    def list_students(self):
        messagebox.showinfo("Students", "\n".join([str(student) for student in self.system.get_students()]))

    def show_marks(self):
        if not hasattr(self, 'selected_course'):
            messagebox.showerror("Error", "Please select a course first.")
            return

        selected_course_name = self.selected_course.get_course_name()
        marks = self.system.get_marks(selected_course_name)

        if marks:
            marks_str = "\n".join([f"{student.get_student_name()}: {marks[student.get_student_id()]}" for student in
                                   self.system.get_students()])
            messagebox.showinfo(f"Marks for {selected_course_name}", marks_str)
        else:
            messagebox.showinfo("No Marks", f"No marks found for {selected_course_name}")

    def sort_gpa(self):
        sorted_students = self.system.sort_gpa()
        messagebox.showinfo("Sorted Students by GPA", "\n".join(
            [f"{student.get_student_name()} - GPA: {self.system.calculate_student_gpa(student):.2f}" for student in
             sorted_students]))

    def load_course_data(self):
        self.load_data("course")

    def load_student_data(self):
        self.load_data("student")

    def load_mark_data(self):
        self.load_data("mark")


def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()


if __name__ == "__main__":
    main()
