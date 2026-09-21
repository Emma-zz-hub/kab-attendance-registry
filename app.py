from attendance import (
    register_student,
    check_in_student,
    today_attendance
)

from reporting import (
    mark_absent_students,
    all_attendance_rates,
    chronic_absentees
)


def register():
    name = input("Enter student name: ").strip()
    student_id = input("Enter student ID: ").strip()

    if not name or not student_id:
        print("Name and Student ID are required.")
        return

    success, message = register_student(name, student_id)
    print(message)


def check_in():
    student_id = input("Enter student ID: ").strip()

    print("1. Present")
    print("2. Late")

    choice = input("Choose status: ").strip()

    if choice == "1":
        status = "Present"
    elif choice == "2":
        status = "Late"
    else:
        print("Invalid status.")
        return

    success, message = check_in_student(student_id, status)
    print(message)


def display_today():
    records = today_attendance()

    print("\nToday's Check-ins")
    print("-----------------")

    if not records:
        print("No students checked in today.")
        return

    for record in records:
        print(
            f"{record['student_id']} - "
            f"{record['name']} - "
            f"{record['status']} - "
            f"{record['timestamp']}"
        )


def mark_absences():
    marked = mark_absent_students()

    if marked:
        print("\nStudents marked absent:")
        for name in marked:
            print(f"- {name}")
    else:
        print("No additional students needed to be marked absent.")


def attendance_report():
    results = all_attendance_rates()

    print("\nAttendance Report")
    print("-----------------")

    if not results:
        print("No attendance data available.")
        return

    for student in results:
        print(
            f"{student['student_id']} - "
            f"{student['name']} - "
            f"{student['rate']:.2f}%"
        )


def chronic_report():
    students = chronic_absentees()

    print("\nChronically Absent Students")
    print("---------------------------")

    if not students:
        print("No students are below 85%.")
        return

    for student in students:
        print(
            f"{student['student_id']} - "
            f"{student['name']} - "
            f"{student['rate']:.2f}%"
        )


def main():
    while True:
        print("\n================================")
        print(" KAB STUDENT ATTENDANCE REGISTER")
        print("================================")
        print("1. Register student")
        print("2. Check in student")
        print("3. View today's attendance")
        print("4. Mark absent students")
        print("5. Attendance report")
        print("6. Chronic absence report")
        print("7. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            register()

        elif choice == "2":
            check_in()

        elif choice == "3":
            display_today()

        elif choice == "4":
            mark_absences()

        elif choice == "5":
            attendance_report()

        elif choice == "6":
            chronic_report()

        elif choice == "7":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()