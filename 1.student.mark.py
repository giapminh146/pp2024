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


def input_student_info(number_of_students, existing_student_ids):
    student_information_list = []
    if number_of_students == 0:
        print("There is no student in a class")
    else:
        for _ in range(number_of_students):
            student_information = {}
            while True:
                student_id = input("Enter the ID of the student: ")
                if student_id not in existing_student_ids:
                    existing_student_ids.add(student_id)
                    break
                else:
                    print("Please enter a unique ID for the student")

            student_name = input("Enter the name of the student: ")

            while True:
                student_dob = input("Enter the date of birth of the student (YYYY-MM-DD): ")
                if check_for_valid_date(student_dob):
                    break
                else:
                    print("Please enter a valid format of date (YYYY-MM-DD). ")
            print("\n")

            student_information["student_id"] = student_id
            student_information["student_name"] = student_name
            student_information["student_DoB"] = student_dob
            student_information_list.append(student_information)
    return student_information_list


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


def input_course_info(number_of_courses, existing_course_ids, existing_course_names):
    course_information_list = []
    if number_of_courses == 0:
        print("There is no course.")
    else:
        for _ in range(number_of_courses):
            course_info = {}
            while True:
                course_id = input("Enter the ID of the course: ")
                if course_id not in existing_course_ids:
                    existing_course_ids.add(course_id)
                    break
                else:
                    print("Please enter a unique ID for the course.")

            while True:
                course_name = input("Enter the name of the course: ")
                if course_name not in existing_course_names:
                    existing_course_names.add(course_name)
                    break
                else:
                    print("Please enter a unique course name.")
            print("\n")
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
            elif 1 <= choice <= len(course_information_list):
                selected_course = course_information_list[choice - 1]
                selected_courses.append(selected_course)
                print(f"Selected course: {selected_course['course_name']}")
                break
            else:
                print(f"Please enter a valid index (between 1 and {len(course_information_list)}) or number 0 to exit. ")
        except ValueError:
            print("Please enter valid index or number 0 to exit. ")
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
                    print("Please enter a valid integer. ")
                    continue
                mark = int(mark)

                if mark < 0:
                    print("Please enter a positive mark.")
                    continue

                if "marks" not in student:
                    student["marks"] = {}
                student["marks"][course["course_name"]] = mark
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
                print("Please enter a valid index (or number 0 to exit). ")
        except ValueError:
            print("Please enter a valid index (or number 0 to exit). ")

    print(f"Marks for {selected_course["course_name"]}:\n")
    for i, student in enumerate(student_information_list, 1):
        marks_dict = student.get("marks", {})
        mark = marks_dict.get(selected_course["course_name"], None)
        student_name = student["student_name"]
        student_id = student["student_id"]
        print(f"{i}. {student_name} - {student_id}: {mark if mark is not None else 'N/A'}")


def main():
    number_of_students = 0
    student_information_list = []
    number_of_courses = 0
    course_information_list = []
    selected_courses = []
    existing_course_ids = set()
    existing_course_names = set()
    existing_student_ids = set()

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

        try:
            choice = int(choice)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            number_of_students = input_number_of_students()
        elif choice == 2:
            if number_of_students == 0:
                print("There is currently no student. Please input the number of student first.")
            else:
                student_information_list.extend(input_student_info(number_of_students, existing_student_ids))
        elif choice == 3:
            number_of_courses = input_number_of_courses()
        elif choice == 4:
            if number_of_courses == 0:
                print("There is currently no course. Please input the number of course first.")
            else:
                course_information_list.extend(input_course_info(number_of_courses, existing_course_ids, existing_course_names))
        elif choice == 5:
            if not course_information_list:
                print("Please input course information first.")
            else:
                selected_courses = select_courses(course_information_list)
        elif choice == 6:
            if not student_information_list or not selected_courses:
                print("Please input the student information and select the courses first.")
            else:
                input_marks(student_information_list, selected_courses)
        elif choice == 7:
            list_courses(course_information_list)
        elif choice == 8:
            list_students(student_information_list)
        elif choice == 9:
            if not student_information_list or not course_information_list:
                print("Please input student and course information first.")
            else:
                show_marks(student_information_list, course_information_list)
        elif choice == 0:
            print("Exited.")
            break
        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()
