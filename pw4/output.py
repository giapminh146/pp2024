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
                stdscr.addstr(
                    f"Please enter a valid index (between 1 and {len(self.get_courses())}) or number 0 to exit.\n")
                stdscr.refresh()
        except ValueError:
            stdscr.addstr(f"Please enter valid index or number 0 to exit.\n")
            stdscr.refresh()

    stdscr.refresh()
    return selected_courses


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
