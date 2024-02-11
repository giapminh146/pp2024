import numpy as np


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