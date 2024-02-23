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
