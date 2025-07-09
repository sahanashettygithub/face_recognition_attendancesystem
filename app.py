from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import face_recognition
import base64
import csv
import os
from datetime import datetime
from face_recog import load_known_faces, recognize_encoding, set_known_faces

app = Flask(__name__)

STUDENT_CSV = 'students.csv'
ATTENDANCE_CSV = 'attendance.csv'

known_face_encodings, known_face_names = load_known_faces()
set_known_faces(known_face_encodings, known_face_names)

if not os.path.exists(ATTENDANCE_CSV):
    with open(ATTENDANCE_CSV, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Date', 'Time', 'Name', 'Status'])

@app.route('/')
def home():
    return render_template('dashboard.html', total=len(known_face_names), present=0, absent=len(known_face_names), rate=0)

@app.route('/dashboard')
def dashboard():
    total_students = len(known_face_names)
    today = datetime.now().strftime('%Y-%m-%d')
    present_names = set()

    with open(ATTENDANCE_CSV, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Date'] == today and row['Status'] == 'Present':
                present_names.add(row['Name'])

    present = len(present_names)
    absent = total_students - present
    rate = round((present / total_students) * 100, 2) if total_students > 0 else 0

    return render_template('dashboard.html', total=total_students, present=present, absent=absent, rate=rate)
@app.route('/students')
def students():
    students = []
    if os.path.exists(STUDENT_CSV):
        with open(STUDENT_CSV, 'r') as f:
            reader = csv.DictReader(f)
            students = list(reader)
    return render_template('students.html', students=students)


@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    data = request.get_json(force=True)
    if 'image' not in data:
        return jsonify({'success': False, 'message': 'No image data received.'})

    try:
        _, encoded = data["image"].split(",", 1)
        img_bytes = base64.b64decode(encoded)
        nparr = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        cv2.imwrite("uploads/captured.jpg", img)
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    except Exception as e:
        return jsonify({'success': False, 'message': f'Image decode error: {str(e)}'})

    face_encodings = face_recognition.face_encodings(rgb_img)
    if not face_encodings:
        return jsonify({'success': False, 'message': 'No face detected in the image.'})

    encoding = face_encodings[0]
    name = recognize_encoding(encoding)

    if name == "Unknown":
        return jsonify({'success': False, 'message': 'Face not recognized.'})

    today = datetime.now().strftime('%Y-%m-%d')
    already_marked = False
    present_names = set()

    with open(ATTENDANCE_CSV, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Date'] == today:
                if row['Name'] == name and row['Status'] == 'Present':
                    already_marked = True
                if row['Status'] == 'Present':
                    present_names.add(row['Name'])

    if not already_marked:
        with open(ATTENDANCE_CSV, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([today, datetime.now().strftime('%H:%M:%S'), name, 'Present'])
        present_names.add(name)

    present = len(present_names)
    absent = len(known_face_names) - present
    rate = round((present / len(known_face_names)) * 100, 2)

    return jsonify({
        'success': True,
        'name': name,
        'present': present,
        'absent': absent,
        'rate': rate
    })
@app.route("/attendance")
def show_attendance():
    attendance_records = []

    with open("attendance.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            attendance_records.append(row)

    return render_template("attendance.html", attendance_records=attendance_records) 
if __name__ == '__main__':
    app.run(debug=True)
