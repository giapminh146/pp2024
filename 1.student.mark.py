def input_number_of_students():
    number = int(input("Enter number of students in a class: "))
    while number <= 0:
        number = int(input("Please enter a valid number of students: "))
    return number


def check_for_valid_day(date):
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


def input_student_info():
    student_information = {}
    student_id = input("Enter the ID of the student: ")
    student_name = input("Enter the name of the student: ")

    while True:
        student_dob = input("Enter the date of birth of the student (YYYY-MM-DD): ")
        if check_for_valid_day(student_dob):
            break
        else:
            print("Please enter a valid format of date (YYYY-MM-DD): ")

    student_information["id"] = student_id
    student_information["name"] = student_name
    student_information["DoB"] = student_dob
    return student_information


