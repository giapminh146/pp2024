import curses
import math
from domains.student import Student
from domains.course import Course


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
    self.get_selected_courses().clear()
