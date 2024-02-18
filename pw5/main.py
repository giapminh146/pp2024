import curses
from domains.management_system import ManagementSystem
import os
from input import *


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_WHITE)

    decompress_files()
    file_exist = os.path.exists('students.txt') and os.path.exists('courses.txt') and os.path.exists('marks.txt')

    system = ManagementSystem()
    number_of_students = 0
    number_of_courses = 0
    if file_exist:
        system.read_data_from_files()
    else:
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

    if os.path.exists('students.txt') and os.path.exists('courses.txt') and os.path.exists('marks.txt'):
        compress_files()
        os.remove('students.txt')
        os.remove('courses.txt')
        os.remove('marks.txt')


if __name__ == "__main__":
    curses.wrapper(main)
