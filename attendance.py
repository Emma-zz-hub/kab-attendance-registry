from datetime import datetime
import json
import os

ATTENDANCE_LOG_FILE = 'attendance_log.json'

def load_attendance_log():
    if not os.path.exists(ATTENDANCE_LOG_FILE):
        return []

    with open(ATTENDANCE_LOG_FILE, 'r') as file:
        return json.load(file)

def save_attendance_log(records):
    with open(ATTENDANCE_LOG_FILE, 'w') as file:
        json.dump(records, file, indent=4)

def register_student(name, student_id):
    records = load_attendance_log()
    
    # Check if student already exists
    for record in records:
        if record['student_id'] == student_id:
            return False, "Student ID already exists."

    # Create new student record
    new_record = {
        'name': name,
        'student_id': student_id,
        'attendance': []
    }
    records.append(new_record)
    save_attendance_log(records)
    return True, "Student registered successfully."

def check_in_student(student_id, status):
    records = load_attendance_log()
    timestamp = datetime.now().isoformat()

    for record in records:
        if record['student_id'] == student_id:
            record['attendance'].append({
                'status': status,
                'timestamp': timestamp
            })
            save_attendance_log(records)
            return True, "Check-in recorded successfully."

    return False, "Student ID not found."

def today_attendance():
    records = load_attendance_log()
    today_records = []

    for record in records:
        for attendance in record['attendance']:
            if attendance['timestamp'].startswith(datetime.now().date().isoformat()):
                today_records.append({
                    'student_id': record['student_id'],
                    'name': record['name'],
                    'status': attendance['status'],
                    'timestamp': attendance['timestamp']
                })

    return today_records