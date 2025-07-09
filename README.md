# 👁️‍🗨️ Face Recognition Attendance System

A smart attendance management system that uses face recognition to automate the attendance marking process. Built using Python, OpenCV, and the `face_recognition` library, this system ensures accuracy, eliminates proxy attendance, and reduces manual effort.

---

## 📌 Problem Statement

Manual attendance systems are often time-consuming, error-prone, and vulnerable to proxy attendance. There is a need for an efficient, secure, and automated solution to manage attendance in educational institutions and workplaces.

---

## 💡 Proposed Solution

This project implements a Face Recognition-based Attendance System that:
- Uses a webcam to detect and recognize faces in real-time.
- Automatically marks attendance when a known face is detected.
- Stores attendance data in a structured format (CSV or database).
- Updates the dashboard with real-time recognition status.

---

## 🛠️ System Development Approach

**Technologies Used:**
- **Frontend:** HTML, CSS
- **Backend:** Python (Flask)
- **Face Recognition:** `face_recognition` library
- **Image/Video Processing:** OpenCV
- **Database:** CSV file

---

## ⚙️ Algorithm & Deployment

### 🔄 Workflow:
1. Load and encode known face images from the `known_faces` folder.
2. Capture real-time video from the webcam using OpenCV.
3. Detect faces in each frame and compare with known encodings.
4. If a match is found:
   - Display name on screen.
   - Mark attendance with timestamp.
5. If no match is found:
   - Display **"Face Not Found"** alert on dashboard.
   - Notify admin (for future upgrade).

### 🚀 Deployment:
- Run the app locally using `app.py`.
- Can be hosted on a local server (Flask).
- For scalability, cloud deployment can be considered.

---

## 🖼️ Result (Output Images)

- Real-time recognition dashboard with bounding boxes.
- Attendance data stored in a `.csv` file.
- Sample message: `"Sahana Shetty marked present at 09:05 AM"`
![WhatsApp Image 2025-07-09 at 20 34 22_b694cf1d](https://github.com/user-attachments/assets/b9bbd0e8-c117-43c8-987d-1c6691fddc36)
---
![WhatsApp Image 2025-07-09 at 21 10 08_6d210c21](https://github.com/user-attachments/assets/6472da33-4c04-4d14-8fb8-c12607689e8b)
---
![WhatsApp Image 2025-07-09 at 21 11 35_5b9d8188](https://github.com/user-attachments/assets/475b2ae8-661c-4acc-88b7-2a0326b7b929)
---
![WhatsApp Image 2025-07-09 at 21 17 24_2971c3b1](https://github.com/user-attachments/assets/df0f03de-738e-457d-a388-41f651be8b01)
---
![WhatsApp Image 2025-07-09 at 21 19 00_45c25f7b](https://github.com/user-attachments/assets/37e4c882-6e76-49fb-9013-00c117577a15)
---
![WhatsApp Image 2025-07-09 at 21 19 21_66e4ec54](https://github.com/user-attachments/assets/263ba5e8-f7e1-46ad-8c81-4f5081d5a251)



## ✅ Conclusion

The Face Recognition Attendance System automates the attendance process, ensuring faster, more secure, and contactless tracking. It minimizes human error and enhances transparency.

---

## 🔮 Future Scope

- Cloud-based attendance dashboard with centralized access.
- Mask detection and thermal screening integration.
- Mobile app version for remote attendance.
- Biometric fusion (face + voice recognition).

---

## 📚 References

- [OpenCV](https://opencv.org/)
- [Flask Framework](https://flask.palletsprojects.com/)
- Research papers on biometric authentication

---

## 👩‍💻 Developed by
**Sahana Shetty**  
B.Tech IT, CMR University  
