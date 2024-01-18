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


class StudentManagement:
    def __init__(self):
        self.__students = []

    def get_students(self):
        return self.__students

    def input_number_of_students(self):
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


class Course:
    def __init__(self, course_id, course_name):
        self.__course_id = course_id
        self.__course_name = course_name

    def get_course_id(self):
        return self.__course_id

    def get_course_name(self):
        return self.__course_name






