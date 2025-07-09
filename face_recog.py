import os
import face_recognition
import numpy as np

known_face_encodings = []
known_face_names = []

def load_known_faces():
    global known_face_encodings, known_face_names
    known_face_encodings = []
    known_face_names = []

    known_faces_dir = "known_faces"
    for filename in os.listdir(known_faces_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            path = os.path.join(known_faces_dir, filename)
            image = face_recognition.load_image_file(path)
            encodings = face_recognition.face_encodings(image)
            if encodings:
                known_face_encodings.append(encodings[0])
                known_face_names.append(os.path.splitext(filename)[0])
            else:
                print(f"[WARNING] No face found in {filename}")

    return known_face_encodings, known_face_names

def set_known_faces(encodings, names):
    global known_face_encodings, known_face_names
    known_face_encodings = encodings
    known_face_names = names

def recognize_encoding(unknown_encoding):
    if not known_face_encodings:
        return "Unknown"
    matches = face_recognition.compare_faces(known_face_encodings, unknown_encoding)
    distances = face_recognition.face_distance(known_face_encodings, unknown_encoding)
    if True in matches:
        best_index = np.argmin(distances)
        return known_face_names[best_index]
    return "Unknown"
