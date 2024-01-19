class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.__student_id = student_id
        self.__student_name = student_name
        self.__student_dob = student_dob

    def get_id(self):
        return self.__student_id

    def get_name(self):
        return self.__student_name

    def get_dob(self):
        return self.__student_dob


class StudentsInfo:
    @staticmethod
    def input_number_of_students():
        while True:
            try:
                number_of_students = int(input("Enter number of students to add: "))
                if number_of_students >= 0:
                    break
                else:
                    print("Please enter a positive number of students. ")
            except ValueError:
                print("Please enter a valid number. ")
        return number_of_students

    @staticmethod
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

    @staticmethod
    def input_student_info(number_of_students, existing_students_list):
        student_information_list = []
        if number_of_students == 0:
            print("There is no student in a class")
        else:
            for _ in range(number_of_students):
                student_information = {}
                while True:
                    student_id = input("Enter the ID of the student: ")
                    for student in existing_students_list:
                        if student_id not in student.student_id:
                            break
                        else:
                            print("Please enter a unique ID for the student.")

                    student_name = input("Enter the name of the student: ")
                    while True:
                        student_dob = input("Enter the date of birth for the student (YYYY-MM-DD): ")
                        if StudentsInfo.check_for_valid_date(student_dob):
                            break
                        else:
                            print("Please enter a valid format of date (YYYY-MM-DD).")
                    print("\n")

                    student_information["student_id"] = student_id
                    student_information["student_name"] = student_name
                    student_information["student_DoB"] = student_dob
                    a_student = Student(student_id, student_name, student_dob)
                    existing_students_list.append(a_student)
                    student_information_list.append(student_information)
        return student_information_list


class Course:
    def __init__(self, course_id, course_name):
        self.__course_id = course_id
        self.__course_name = course_name

    def get_course_id(self):
        return self.__course_id

    def get_course_name(self):
        return self.__course_name


class CoursesInfo:
    @staticmethod
    def input_number_of_courses():
        while True:
            try:
                number_of_courses = int(input("Enter number of courses to add: "))
                if number_of_courses >= 0:
                    break
                else:
                    print("Please enter a positive number of courses. ")
            except ValueError:
                print("Please enter a valid number of courses. ")
        return number_of_courses

    @staticmethod
    def input_course_info(number_of_courses, existing_courses_list):
        course_information_list = []
        if number_of_courses == 0:
            print("There is no course.")
        else:
            for _ in range(number_of_courses):
                course_info = {}
                for course in existing_courses_list:
                    while True:
                        course_id = input("Enter the ID of the course: ")
                        if course_id not in course.course_id:
                            break
                        else:
                            print("Please enter a unique ID for the course.")

                    while True:
                        course_name = input("Enter the name for the course: ")
                        if course_name not in course.course_name:
                            break
                        else:
                            print("Please enter a unique course name.")

                    print("\n")
                    course_info["course_id"] = course_id
                    course_info["course_name"] = course_name
                    a_course = Course(course_id, course_name)
                    existing_courses_list.append(a_course)
                    course_information_list.append(course_info)
        return course_information_list



