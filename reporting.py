from attendance_log import load_attendance_data, save_attendance_data

def mark_absent_students():
    attendance_data = load_attendance_data()
    absent_students = []

    for student in attendance_data:
        if student['status'] == 'Absent':
            absent_students.append(student['name'])

    save_attendance_data(attendance_data)
    return absent_students


def all_attendance_rates():
    attendance_data = load_attendance_data()
    attendance_rates = []

    total_days = len(attendance_data)
    for student in attendance_data:
        present_days = sum(1 for record in attendance_data if record['student_id'] == student['student_id'] and record['status'] == 'Present')
        rate = (present_days / total_days) * 100 if total_days > 0 else 0
        attendance_rates.append({
            'student_id': student['student_id'],
            'name': student['name'],
            'rate': rate
        })

    return attendance_rates


def chronic_absentees(threshold=85):
    attendance_rates = all_attendance_rates()
    chronic_students = [student for student in attendance_rates if student['rate'] < threshold]
    return chronic_students