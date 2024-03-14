import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
from domains.management_system import ManagementSystem
import pickle

class MainApplication:
    def __init__(self, master):
        self.selected_course = None
        self.master = master
        self.master.title("Student Management System")

        self.system = ManagementSystem()
        self.number_of_students = 0
        self.number_of_courses = 0

        self.create_widgets()

    def simple_selection_dialog(self, title, options):
        def on_select(event):
            selection_index = listbox.curselection()
            if selection_index:
                selected_option.set(options[selection_index[0]])
                dialog.destroy()

        dialog = tk.Tk()
        dialog.title(title)
        dialog.geometry('300x200')

        selected_option = tk.StringVar(value=None)

        listbox = tk.Listbox(dialog)
        listbox.pack(fill=tk.BOTH, expand=True)
        for option in options:
            listbox.insert(tk.END, option)

        listbox.bind('<<ListboxSelect>>', on_select)

        dialog.mainloop()
        return selected_option.get()

    def create_widgets(self):
        tk.Label(self.master, text="Welcome to the Student Management System").pack()

        tk.Button(self.master, text="Input number of students", command=self.input_number_of_students).pack()
        tk.Button(self.master, text="Input students information", command=self.input_student_info).pack()
        tk.Button(self.master, text="Input number of courses", command=self.input_number_of_courses).pack()
        tk.Button(self.master, text="Input course information", command=self.input_course_info).pack()
        tk.Button(self.master, text="Select courses", command=self.select_course).pack()
        tk.Button(self.master, text="Input marks", command=self.call_input_marks).pack()
        tk.Button(self.master, text="List courses", command=self.list_courses).pack()
        tk.Button(self.master, text="List students", command=self.list_students).pack()
        tk.Button(self.master, text="Show marks", command=self.show_marks).pack()
        tk.Button(self.master, text="Sort students by GPA descending", command=self.sort_gpa).pack()
        tk.Button(self.master, text="Save Course Data", command=self.save_course_data).pack()
        tk.Button(self.master, text="Save Student Data", command=self.save_student_data).pack()
        tk.Button(self.master, text="Save Mark Data", command=self.save_mark_data).pack()
        tk.Button(self.master, text="Load Course Data", command=self.load_course_data).pack()
        tk.Button(self.master, text="Load Student Data", command=self.load_student_data).pack()
        tk.Button(self.master, text="Load Mark Data", command=self.load_mark_data).pack()
        tk.Button(self.master, text="Exit", command=self.master.quit).pack()

    def save_course_data(self):
        filename = tk.filedialog.asksaveasfilename(defaultextension=".pickle", filetypes=[("Pickle files", "*.pickle")])
        if filename:
            self.system.save_course_data(filename)
            messagebox.showinfo("Success", "Course data saved successfully.")

    def save_student_data(self):
        filename = tk.filedialog.asksaveasfilename(defaultextension=".pickle", filetypes=[("Pickle files", "*.pickle")])
        if filename:
            self.system.save_student_data(filename)
            messagebox.showinfo("Success", "Student data saved successfully.")

    def save_mark_data(self):
        filename = filedialog.asksaveasfilename(defaultextension=".pickle", filetypes=[("Pickle files", "*.pickle")])
        if filename:
            selected_course = self.simple_selection_dialog("Select a Course", [course.get_course_name() for course in self.system.get_courses()])
            if selected_course:
                marks = {}
                for student in self.system.get_students():
                    marks[student.get_student_name()] = student.get_marks().get(selected_course, None)
                with open(filename, 'wb') as file:
                    pickle.dump(marks, file)
                messagebox.showinfo("Success", "Mark data saved successfully.")


    def load_course_data(self):
        filename = tk.filedialog.askopenfilename(filetypes=[("Pickle files", "*.pickle")])
        if filename:
            self.system.load_course_data(filename)
            messagebox.showinfo("Success", "Course data loaded successfully.")

    def load_student_data(self):
        filename = tk.filedialog.askopenfilename(filetypes=[("Pickle files", "*.pickle")])
        if filename:
            self.system.load_student_data(filename)
            messagebox.showinfo("Success", "Student data loaded successfully.")

    def load_mark_data(self):
        filename = tk.filedialog.askopenfilename(filetypes=[("Pickle files", "*.pickle")])
        if filename:
            self.system.load_mark_data(filename)
            messagebox.showinfo("Success", "Mark data loaded successfully.")

    def input_number_of_students(self):
        self.number_of_students = simple_input_dialog("Input number of students")
        messagebox.showinfo("Success", "Number of students set successfully.")

    def input_student_info(self):
        if self.number_of_students == 0:
            messagebox.showerror("Error", "Please input the number of students first.")
            return
        num_students = simple_input_dialog("Enter the number of students")
        try:
            num_students = int(num_students)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for number of students.")
            return
        student_info_list = self.system.input_student_info(num_students)
        messagebox.showinfo("Success", "Student information added successfully.")

    def input_number_of_courses(self):
        self.number_of_courses = simple_input_dialog("Input number of courses")
        messagebox.showinfo("Success", "Number of courses set successfully.")

    def input_course_info(self):
        if self.number_of_courses == 0:
            messagebox.showerror("Error", "Please input the number of courses first.")
            return
        num_courses = simple_input_dialog("Enter the number of courses")
        try:
            num_courses = int(num_courses)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for number of courses.")
            return
        course_info_list = self.system.input_course_info(num_courses)
        messagebox.showinfo("Success", "Course information added successfully.")

    def select_course(self):
        def on_course_selected(course):
            self.selected_course = course
            messagebox.showinfo("Success", f"Course '{course.get_course_name()}' selected successfully.")
            select_window.destroy()

        select_window = tk.Toplevel(self.master)
        select_window.title("Select a Course")
        select_window.geometry("300x200")

        for course in self.system.get_courses():
            course_button = tk.Button(select_window, text=course.get_course_name(),
                                      command=lambda c=course: on_course_selected(c))
            course_button.pack(pady=5)

    def input_marks(self, selected_course):
        input_marks_window = tk.Toplevel(self.master)
        input_marks_window.title(f"Input Marks for Students in {selected_course.get_course_name()}")
        input_marks_window.geometry("400x300")

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
                    messagebox.showinfo("Success",
                                        f"Mark set for {student.get_student_name()} in {selected_course.get_course_name()}: {mark}")
                except ValueError:
                    messagebox.showerror("Error", "Invalid mark. Please enter a numeric value.")

            submit_button = tk.Button(frame, text="Set Mark", command=set_mark)
            submit_button.pack(side=tk.RIGHT)

    def call_input_marks(self):
        if hasattr(self, 'selected_course'):
            self.input_marks(self.selected_course)
        else:
            messagebox.showerror("Error", "Please select a course first.")

    def list_courses(self):
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
        messagebox.showinfo("Sorted Students by GPA", "\n".join([f"{student} - GPA: {student.calc_gpa(self.system.get_courses()):.2f}" for student in sorted_students]))

def simple_input_dialog(prompt):
    return simple_dialog(prompt, tk.simpledialog.askstring)

def simple_dialog(prompt, func):
    return func("Input", prompt)

def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()
