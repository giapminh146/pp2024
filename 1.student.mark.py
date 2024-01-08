def input_number_of_students():
    number_of_students = int(input("Enter number of students in a class: "))
    while number_of_students < 0:
        number_of_students = int(input("Please enter a valid number of students: "))
    return number_of_students


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

        return True
    except ValueError:
        return False


def input_student_info(number_of_students):
    student_information_list = []
    if number_of_students == 0:
        print("There is no student in a class")
    else:
        for _ in range(number_of_students):
            student_information = {}
            student_id = input("Enter the ID of the student: ")
            student_name = input("Enter the name of the student: ")

            while True:
                student_dob = input("Enter the date of birth of the student (YYYY-MM-DD): ")
                if check_for_valid_date(student_dob):
                    break
                else:
                    print("Please enter a valid format of date (YYYY-MM-DD): ")

            student_information["student_id"] = student_id
            student_information["student_name"] = student_name
            student_information["student_DoB"] = student_dob
            student_information_list.append(student_information)
    return student_information_list


def input_number_of_courses():
    number_of_courses = int(input("Enter number of courses: "))
    while number_of_courses < 0:
        number_of_courses = int(input("Please enter a valid number of courses (>= 0): "))
    return number_of_courses


def input_course_info(number_of_courses):
    course_information_list = []
    if number_of_courses == 0:
        print("There is no course.")
    else:
        for _ in range(number_of_courses):
            course_info = {}
            course_id = input("Enter the ID of the course: ")
            course_name = input("Enter the name of the course: ")
            course_info["course_id"] = course_id
            course_info["course_name"] = course_name
            course_information_list.append(course_info)
    return course_information_list

def select_courses():

