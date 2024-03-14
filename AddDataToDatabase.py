import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancesystem-77784-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {

    "111721105015":
        {
            "Name": "Pratishta S",
            "Department": "EIE",
            "Batch": "2021-2025",
            "Year": 3,
            "Dayscholar_or_Hosteller": "H",
            "Total_Attendance": 9,
            "Last_Attendance_Time": "2023-8-12 18:30:45"
        },
    "111721105019":
        {
            "Name": "Sowmya S R",
            "Department": "EIE",
            "Batch": "2021-2025",
            "Year": 3,
            "Dayscholar_or_Hosteller": "D",
            "Total_Attendance": 10,
            "Last_Attendance_Time": "2023-8-12 18:25:45"
        },
    "111721105021":
        {
            "Name": "Swetha S",
            "Department": "EIE",
            "Batch": "2021-2025",
            "Year": 3,
            "Dayscholar_or_Hosteller": "D",
            "Total_Attendance": 11,
            "Last_Attendance_Time": "2023-8-12 18:20:45"
        },
    "111721105024":
        {
            "Name": "Vaishnavi G",
            "Department": "EIE",
            "Batch": "2021-2025",
            "Year": 3,
            "Dayscholar_or_Hosteller": "D",
            "Total_Attendance": 12,
            "Last_Attendance_Time": "2023-8-12 18:15:45"
        },
    "111721105028":
        {
            "Name": "Sundar Pichai",
            "Department": "CSE",
            "Batch": "2020-2024",
            "Year": 4,
            "Dayscholar_or_Hosteller": "H",
            "Total_Attendance": 13,
            "Last_Attendance_Time": "2023-8-12 18:10:45"
        },
    "111721105029":
        {
            "Name": "Emily Blunt",
            "Department": "ADS",
            "Batch": "2022-2026",
            "Year": 2,
            "Dayscholar_or_Hosteller": "D",
            "Total_Attendance": 8,
            "Last_Attendance_Time": "2023-8-12 18:05:45"
        },
    "111721105030":
        {
            "Name": "Elon Musk",
            "Department": "ECE",
            "Batch": "2020-2024",
            "Year": 4,
            "Dayscholar_or_Hosteller": "H",
            "Total_Attendance": 7,
            "Last_Attendance_Time": "2023-8-12 18:03:45"
        }
}

for key, value in data.items():
    ref.child(key).set(value)

