def input_number_of_students():
    while True:
        try:
            number_of_students = int(input("Enter number of students in a class: "))
            if number_of_students >= 0:
                break
            else:
                print("Please enter a positive number of students: ")
        except ValueError:
            print("Please enter a valid number: ")
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
        if year < 0:
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
    while True:
        try:
            number_of_courses = int(input("Enter number of courses: "))
            if number_of_courses >= 0:
                break
            else:
                print("Please enter a positive number of courses: ")
        except ValueError:
            print("Please enter a valid number of courses: ")
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


def select_courses(course_information_list):
    print("Available courses:")
    for i, course in enumerate(course_information_list, 1):
        print(f"{i}. {course["course_name"]}")

    selected_courses = []
    while True:
        choice = int(input("Enter the index number of the course to select the course (0 to exit): "))
        try:
            if choice == 0:
                break
            elif 0 < choice <= len(course_information_list):
                selected_course = course_information_list[choice - 1]
                selected_courses.append(selected_course)
            else:
                print("Please enter a valid index or number 0 to exit: ")
        except ValueError:
            print("Please enter valid index or number 0 to exit: ")
    return selected_courses


def input_marks(student_information_list, selected_courses):
    for course in selected_courses:
        print(f"You are currently in course: {course["course_name"]}")
        for student in student_information_list:
            student_id = student["student_id"]
            student_name = student["student_name"]
            while True:
                mark = input(f"Enter the mark for student {student_name} (ID: {student_id}): ")
                if not mark.isdigit():
                    print("Please enter a valid integer: ")
                    continue
                mark = int(mark)

                if mark < 0:
                    print("Please enter a positive mark.")
                    continue

                student["mark"] = mark
                break


def list_courses(course_information_list):
    if len(course_information_list) == 0:
        print("No course available.")
    else:
        print("Available courses:")
        for i, course in enumerate(course_information_list, 1):
            print(f"{i}. {course["course_name"]} - {course["course_id"]}")


def list_students(student_information_list):
    if len(student_information_list) == 0:
        print("No student available.")
    else:
        print("Students list: ")
        for i, student in enumerate(student_information_list, 1):
            print(f"{i}. Name: {student["student_name"]}, ID: {student["student_id"]}, Date of birth: {student["student_DoB"]}")


def show_marks(student_information_list, course_information_list):
    list_courses(course_information_list)
    while True:
        try:
            choice = int(input("Enter the index number of the course to show marks (0 to exit): "))
            if choice == 0:
                return
            elif 0 < choice <= len(course_information_list):
                selected_course = course_information_list[choice - 1]
                break
            else:
                print("Please enter a valid index (or number 0 to exit): ")
        except ValueError:
            print("Please enter a valid index (or number 0 to exit): ")

    print(f"Marks for {selected_course["course_name"]}:\n")
    for i, student in enumerate(student_information_list, 1):
        mark = student.get("mark", None)
        student_name = student["student_name"]
        student_id = student["student_id"]
        print(f"{i}. {student_name} - {student_id}: {mark if mark is not None else 'N/A'}")


def main():
