import math
import numpy as np
import curses


class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.__student_id = student_id
        self.__student_name = student_name
        self.__student_dob = student_dob
        self.__marks = {}

    def get_student_id(self):
        return self.__student_id

    def get_student_name(self):
        return self.__student_name

    def get_student_dob(self):
        return self.__student_dob

    def get_marks(self):
        return self.__marks

    def calc_gpa(self, courses):
        marks_list = []
        credits_list = []

        for course in courses:
            course_name = course.get_course_name()
            if course_name in self.__marks:
                mark = self.__marks[course_name]
                credits = course.get_credits()
                marks_list.append(mark * credits)
                credits_list.append(credits)

        marks_array = np.array(marks_list)
        credits_array = np.array(credits_list)

        total_credits = np.sum(credits_array)
        if total_credits != 0:
            sum = np.sum(marks_array)
            return sum / total_credits
        else:
            return 0

    def __str__(self):
        return f"Name: {self.__student_name}, ID: {self.__student_id}, Date of birth: {self.__student_dob}"


class Course:
    def __init__(self, course_id, course_name, credits):
        self.__course_id = course_id
        self.__course_name = course_name
        self.__credits = credits

    def get_course_id(self):
        return self.__course_id

    def get_course_name(self):
        return self.__course_name

    def get_credits(self):
        return self.__credits

    def __str__(self):
        return f"{self.__course_name} - {self.__course_id} - ({self.__credits} credits)"


class ManagementSystem:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__selected_courses = set()

    def get_students(self):
        return self.__students

    def get_courses(self):
        return self.__courses

    def get_selected_courses(self):
        return self.__selected_courses

    def input_number_of_students(self, stdscr):
        curses.echo()
        stdscr.clear()
        stdscr.addstr("Enter number of students to add: ")
        stdscr.refresh()
        number_of_students = stdscr.getstr().decode()
        stdscr.clear()
        stdscr.refresh()
        while True:
            try:
                number_of_students = int(number_of_students)
                if number_of_students >= 0:
                    return number_of_students
                else:
                    stdscr.clear()
                    stdscr.addstr("Please enter a positive number of students.\n")
                    stdscr.addstr("Enter number of students to add: ")
                    stdscr.refresh()
                    number_of_students = stdscr.getstr().decode()
            except ValueError:
                stdscr.clear()
                stdscr.addstr("Please enter a valid number.\n")
                stdscr.addstr("Enter number of students to add: ")
                stdscr.refresh()
                number_of_students = stdscr.getstr().decode()

    def check_for_valid_date(self, date):
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

    def input_student_info(self, number_of_students, stdscr):
        student_information_list = []
        if number_of_students == 0:
            stdscr.addstr("There is no student in a class")
            stdscr.refresh()
        else:
            for _ in range(number_of_students):
                student_information = {}
                while True:
                    stdscr.addstr("Enter the ID of the student: ")
                    stdscr.refresh()
                    student_id = stdscr.getstr().decode()
                    if student_id not in [student.get_student_id() for student in self.get_students()]:
                        break
                    else:
                        stdscr.clear()
                        stdscr.addstr("Please enter a unique ID for the student.\n")
                        stdscr.refresh()

                stdscr.clear()
                stdscr.addstr("Enter the name of the student: ")
                stdscr.refresh()
                student_name = stdscr.getstr().decode()
                while True:
                    stdscr.addstr("Enter the date of birth for the student (YYYY-MM-DD): ")
                    stdscr.refresh()
                    student_dob = stdscr.getstr().decode()
                    if self.check_for_valid_date(student_dob):
                        break
                    else:
                        stdscr.clear()
                        stdscr.addstr("Please enter a valid format of date (YYYY-MM-DD).\n")
                        stdscr.refresh()
                stdscr.addstr("\n")

                student_information["student_id"] = student_id
                student_information["student_name"] = student_name
                student_information["student_DoB"] = student_dob
                a_student = Student(student_id, student_name, student_dob)
                self.get_students().append(a_student)
                student_information_list.append(student_information)
        return student_information_list

    def input_number_of_courses(self, stdscr):
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

        return course_information_list

    def select_courses(self, stdscr):
        stdscr.clear()
        stdscr.addstr("Available courses:\n")
        for i, course in enumerate(self.get_courses(), 1):
            stdscr.addstr(f"{i}. {course}\n")

        selected_courses = []
        while True:
            stdscr.addstr("Enter the index number of the course to select the course (0 to exit): ")
            stdscr.refresh()
            choice = stdscr.getstr().decode()
            try:
                choice = int(choice)
                if choice == 0:
                    break
                elif 1 <= choice <= len(self.get_courses()):
                    selected_course = self.get_courses()[choice - 1]
                    self.get_selected_courses().add(selected_course)
                    stdscr.addstr(f"Selected course: {selected_course}\n")
                    break
                else:
                    stdscr.addstr(f"Please enter a valid index (between 1 and {len(self.get_courses())}) or number 0 to exit.\n")
                    stdscr.refresh()
            except ValueError:
                stdscr.addstr(f"Please enter valid index or number 0 to exit.\n")
                stdscr.refresh()

        stdscr.refresh()
        return selected_courses

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
        self.__selected_courses.clear()

    def list_courses(self, stdscr):
        stdscr.clear()
        if len(self.get_courses()) == 0:
            stdscr.addstr("No course available.\n")
        else:
            stdscr.addstr("Available courses:\n")
            for i, course in enumerate(self.get_courses(), 1):
                stdscr.addstr(f"{i}. {course}\n")
        stdscr.refresh()

    def list_students(self, stdscr):
        stdscr.clear()
        if len(self.get_students()) == 0:
            stdscr.addstr("No student available.\n")
        else:
            stdscr.addstr("Students list:\n")
            for i, student in enumerate(self.get_students(), 1):
                stdscr.addstr(f"{i}. {student}\n")
        stdscr.refresh()

    def show_marks(self, stdscr):
        self.list_courses(stdscr)
        while True:
            stdscr.addstr("Enter the index number of the course to show marks (0 to exit): ")
            stdscr.refresh()
            choice = stdscr.getstr().decode()
            try:
                choice = int(choice)
                if choice == 0:
                    return
                elif 0 < choice <= len(self.get_courses()):
                    selected_course = self.get_courses()[choice - 1]
                    break
                else:
                    stdscr.addstr("Please enter a valid index (or number 0 to exit).\n")
                    stdscr.refresh()
            except ValueError:
                stdscr.addstr("Please enter a valid index (or number 0 to exit).\n")
                stdscr.refresh()

        stdscr.addstr(f"Marks for {selected_course}:\n")
        for i, student in enumerate(self.get_students(), 1):
            marks_dict = student.get_marks()
            mark = marks_dict.get(selected_course.get_course_name(), None)
            student_name = student.get_student_name()
            student_id = student.get_student_id()
            stdscr.addstr(f"{i}. {student_name} - {student_id}: {mark if mark is not None else 'N/A'}\n")
        stdscr.refresh()

    def sort_gpa(self, stdscr):
        courses = self.get_courses()
        students_gpa = []

        for student in self.get_students():
            student_gpa = student.calc_gpa(courses)
            students_gpa.append((student, student_gpa))
        sorted_students = sorted(students_gpa, key=lambda x: x[1], reverse=True)
        sorted_students = [student[0] for student in sorted_students]

        return sorted_students


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_WHITE)

    system = ManagementSystem()
    number_of_students = 0
    number_of_courses = 0

    stdscr.addstr("Welcome to the student management system\n", curses.color_pair(4))
    stdscr.refresh()
    while True:
        stdscr.addstr("\nPlease select an option below: \n", curses.color_pair(2) | curses.A_BOLD)
        stdscr.addstr("1. Input number of students\n", curses.color_pair(6))
        stdscr.addstr("2. Input students information\n", curses.color_pair(6))
        stdscr.addstr("3. Input number of courses\n", curses.color_pair(6))
        stdscr.addstr("4. Input course information\n", curses.color_pair(6))
        stdscr.addstr("5. Select courses\n", curses.color_pair(6))
        stdscr.addstr("6. Input marks\n", curses.color_pair(6))
        stdscr.addstr("7. List courses\n", curses.color_pair(6))
        stdscr.addstr("8. List students\n", curses.color_pair(6))
        stdscr.addstr("9. Show marks\n", curses.color_pair(6))
        stdscr.addstr("10. Sort students by GPA descending\n", curses.color_pair(6))
        stdscr.addstr("0. Exit\n", curses.color_pair(3 | curses.A_BOLD))

        stdscr.addstr("Your choice: ", curses.color_pair(1))
        stdscr.refresh()
        curses.echo()
        choice = stdscr.getstr().decode()
        stdscr.clear()
        stdscr.refresh()
        try:
            choice = int(choice)
        except ValueError:
            stdscr.addstr("Please enter a valid number.\n", curses.color_pair(3))
            stdscr.refresh()
            continue

        if choice == 1:
            number_of_students = system.input_number_of_students(stdscr)
            stdscr.addstr("Input successfully\n", curses.color_pair(4))
            stdscr.refresh()
        elif choice == 2:
            if number_of_students == 0:
                stdscr.addstr("There is currently no student. Please input the number of student first.\n", curses.color_pair(3))
                stdscr.refresh()
            else:
                system.input_student_info(number_of_students, stdscr)
                stdscr.addstr("Input successfully\n", curses.color_pair(4))
                stdscr.refresh()
        elif choice == 3:
            number_of_courses = system.input_number_of_courses(stdscr)
            stdscr.addstr("Input successfully\n", curses.color_pair(4))
            stdscr.refresh()
        elif choice == 4:
            if number_of_courses == 0:
                stdscr.addstr("There is currently no course. Please input the number of course first.\n", curses.color_pair(3))
                stdscr.refresh()
            else:
                system.input_course_info(number_of_courses, stdscr)
                stdscr.addstr("Input successfully\n", curses.color_pair(4))
                stdscr.refresh()
        elif choice == 5:
            if not system.get_courses():
                stdscr.addstr("Please input course information first.\n", curses.color_pair(3))
                stdscr.refresh()
            else:
                system.select_courses(stdscr)
        elif choice == 6:
            if not system.get_students() or not system.get_selected_courses():
                stdscr.addstr("Please input the student information and select the course first.\n", curses.color_pair(3))
                stdscr.refresh()
            else:
                system.input_marks(stdscr)
                stdscr.addstr("Input successfully\n", curses.color_pair(3))
                stdscr.refresh()
        elif choice == 7:
            system.list_courses(stdscr)
            stdscr.refresh()
        elif choice == 8:
            system.list_students(stdscr)
            stdscr.refresh()
        elif choice == 9:
            if not system.get_students() or not system.get_courses():
                stdscr.addstr("Please input student and course information first.\n", curses.color_pair(3))
                stdscr.refresh()
            else:
                system.show_marks(stdscr)
        elif choice == 10:
            if not system.get_students() or not system.get_courses():
                stdscr.addstr("Please input student and course information first.\n", curses.color_pair(3))
                stdscr.refresh()
            else:
                sorted_students = system.sort_gpa(stdscr)
                stdscr.addstr("Sorted students by GPA descending: \n", curses.color_pair(2))
                for i, student in enumerate(sorted_students, 1):
                    stdscr.addstr(f"{i}. {student} - GPA: {student.calc_gpa(system.get_courses()):.2f}\n", curses.color_pair(6))
                stdscr.refresh()
        elif choice == 0:
            stdscr.addstr("Exited.\n", curses.color_pair(3) | curses.A_BOLD)
            stdscr.refresh()
            break
        else:
            stdscr.addstr("Invalid option. Please choose a valid option.\n", curses.color_pair(3))
            stdscr.refresh()


if __name__ == "__main__":
    curses.wrapper(main)
