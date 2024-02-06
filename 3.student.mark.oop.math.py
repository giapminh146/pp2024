import math


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

    def __str__(self):
        return f"Name: {self.__student_name}, ID: {self.__student_id}, Date of birth: {self.__student_dob}"


class Course:
    def __init__(self, course_id, course_name):
        self.__course_id = course_id
        self.__course_name = course_name

    def get_course_id(self):
        return self.__course_id

    def get_course_name(self):
        return self.__course_name

    def __str__(self):
        return f"{self.__course_name} - {self.__course_id}"


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

    def input_number_of_students(self):
        while True:
            try:
                number_of_students = int(input("Enter number of students to add: "))
                if number_of_students >= 0:
                    return number_of_students
                else:
                    print("Please enter a positive number of students. ")
            except ValueError:
                print("Please enter a valid number. ")

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

    def input_student_info(self, number_of_students):
        student_information_list = []
        if number_of_students == 0:
            print("There is no student in a class")
        else:
            for _ in range(number_of_students):
                student_information = {}
                while True:
                    student_id = input("Enter the ID of the student: ")
                    if student_id not in [student.get_student_id() for student in self.get_students()]:
                        break
                    else:
                        print("Please enter a unique ID for the student.")

                student_name = input("Enter the name of the student: ")
                while True:
                    student_dob = input("Enter the date of birth for the student (YYYY-MM-DD): ")
                    if self.check_for_valid_date(student_dob):
                        break
                    else:
                        print("Please enter a valid format of date (YYYY-MM-DD).")
                print("\n")

                student_information["student_id"] = student_id
                student_information["student_name"] = student_name
                student_information["student_DoB"] = student_dob
                a_student = Student(student_id, student_name, student_dob)
                self.get_students().append(a_student)
                student_information_list.append(student_information)
        return student_information_list

    def input_number_of_courses(self):
        while True:
            try:
                number_of_courses = int(input("Enter number of courses to add: "))
                if number_of_courses >= 0:
                    return number_of_courses
                else:
                    print("Please enter a positive number of courses. ")
            except ValueError:
                print("Please enter a valid number of courses. ")

    def input_course_info(self, number_of_courses):
        course_information_list = []
        if number_of_courses == 0:
            print("There is no course.")
        else:
            for _ in range(number_of_courses):
                course_info = {}
                while True:
                    course_id = input("Enter the ID of the course: ")
                    if course_id not in [course.get_course_id() for course in self.get_courses()]:
                        break
                    else:
                        print("Please enter a unique ID for the course.")

                while True:
                    course_name = input("Enter the name for the course: ")
                    if course_name not in [course.get_course_name() for course in self.get_courses()]:
                        break
                    else:
                        print("Please enter a unique course name.")

                print("\n")
                course_info["course_id"] = course_id
                course_info["course_name"] = course_name
                a_course = Course(course_id, course_name)
                self.get_courses().append(a_course)
                course_information_list.append(course_info)

        return course_information_list

    def select_courses(self):
        print("Available courses:")
        for i, course in enumerate(self.get_courses(), 1):
            print(f"{i}. {course}")

        selected_courses = []
        while True:
            choice = int(input("Enter the index number of the course to select the course (0 to exit): "))
            try:
                if choice == 0:
                    break
                elif 1 <= choice <= len(self.get_courses()):
                    selected_course = self.get_courses()[choice - 1]
                    self.get_selected_courses().add(selected_course)
                    print(f"Selected course: {selected_course}")
                    break
                else:
                    print(f"Please enter a valid index (between 1 and {len(self.get_courses())}) or number 0 to exit.")
            except ValueError:
                print(f"Please enter valid index or number 0 to exit.")

        return selected_courses

    def input_marks(self):
        selected_course = next(iter(self.get_selected_courses()), None)
        if selected_course is None:
            print("Please select a course first.")
            return

        print(f"You are currently in course: {selected_course}")
        for student in self.get_students():
            student_id = student.get_student_id()
            student_name = student.get_student_name()

            if selected_course.get_course_name() in student.get_marks():
                print(f"Mark already entered for {student_name} (ID: {student_id}) in course: {selected_course}")
                continue

            while True:
                mark = input(f"Enter the mark for student {student_name} (ID: {student_id}): ")
                try:
                    mark = float(mark)
                    if mark < 0.0:
                        print("Please enter a positive mark.")
                        continue
                    mark = math.floor(mark * 10) / 10
                    student.get_marks()[selected_course.get_course_name()] = mark
                    break
                except ValueError:
                    print("Please enter a valid mark.")

    def list_courses(self):
        if len(self.get_courses()) == 0:
            print("No course available.")
        else:
            print("Available courses:")
            for i, course in enumerate(self.get_courses(), 1):
                print(f"{i}. {course}")

    def list_students(self):
        if len(self.get_students()) == 0:
            print("No student available.")
        else:
            print("Students list: ")
            for i, student in enumerate(self.get_students(), 1):
                print(f"{i}. {student}")

    def show_marks(self):
        self.list_courses()
        while True:
            try:
                choice = int(input("Enter the index number of the course to show marks (0 to exit): "))
                if choice == 0:
                    return
                elif 0 < choice <= len(self.get_courses()):
                    selected_course = self.get_courses()[choice - 1]
                    break
                else:
                    print("Please enter a valid index (or number 0 to exit). ")
            except ValueError:
                print("Please enter a valid index (or number 0 to exit). ")

        print(f"Marks for {selected_course}:\n")
        for i, student in enumerate(self.get_students(), 1):
            marks_dict = student.get_marks()
            mark = marks_dict.get(selected_course.get_course_name(), None)
            student_name = student.get_student_name()
            student_id = student.get_student_id()
            print(f"{i}. {student_name} - {student_id}: {mark if mark is not None else 'N/A'}")


def main():
    system = ManagementSystem()
    number_of_students = 0
    number_of_courses = 0

    print("Welcome to the student management system")
    while True:
        print("\nPlease select an option below: ")
        print("1. Input number of students")
        print("2. Input students information")
        print("3. Input number of courses")
        print("4. Input course information")
        print("5. Select courses")
        print("6. Input marks")
        print("7. List courses")
        print("8. List students")
        print("9. Show marks")
        print("0. Exit")

        choice = input("Your choice: ")
        print("\n")
        try:
            choice = int(choice)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            number_of_students = system.input_number_of_students()
            print("Input successfully")
        elif choice == 2:
            if number_of_students == 0:
                print("There is currently no student. Please input the number of student first.")
            else:
                system.input_student_info(number_of_students)
                print("Input successfully")
        elif choice == 3:
            number_of_courses = system.input_number_of_courses()
            print("Input successfully")
        elif choice == 4:
            if number_of_courses == 0:
                print("There is currently no course. Please input the number of course first.")
            else:
                system.input_course_info(number_of_courses)
                print("Input successfully")
        elif choice == 5:
            if not system.get_courses():
                print("Please input course information first. ")
            else:
                system.select_courses()
        elif choice == 6:
            if not system.get_students() or not system.get_selected_courses():
                print("Please input the student information and select the course first.")
            else:
                system.input_marks()
        elif choice == 7:
            system.list_courses()
        elif choice == 8:
            system.list_students()
        elif choice == 9:
            if not system.get_students() or not system.get_courses():
                print("Please input student and course information first.")
            else:
                system.show_marks()
        elif choice == 0:
            print("Exited.")
            break
        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()
