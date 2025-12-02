# 📡 Network Status Dashboard API

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

מערכת Backend קלילה ומהירה לניטור סטטוס רשת, הבודקת זמינות שרתים (Ping) וסטטוס פורטים (Port Checking). המערכת נבנתה באמצעות Python ו-FastAPI.

---

## 🖼️ תצוגה מקדימה (Preview)
*(כאן כדאי להוסיף צילום מסך של ה-Swagger UI או של ה-Dashboard העתידי)*

## 🚀 פיצ'רים מרכזיים
* **בדיקת קישוריות (Ping):** בדיקת זמינות שרתים וזמני תגובה (RTT) בזמן אמת.
* **סריקת פורטים:** בדיקה האם פורט TCP מסוים פתוח בשרת מרוחק.
* **ביצועים גבוהים:** מבוסס על FastAPI לעבודה אסינכרונית מהירה.
* **תיעוד אוטומטי:** גישה מלאה ל-Swagger UI ול-Redoc.

## 🛠️ טכנולוגיות
* [FastAPI](https://fastapi.tiangolo.com/) - תשתית ה-Web.
* [Uvicorn](https://www.uvicorn.org/) - שרת ASGI להרצת האפליקציה.
* `ping3` - ספרייה לביצוע בדיקות ICMP (פינג).
* `socket` - לביצוע בדיקות TCP/פורטים.

---

## 📦 התקנה והרצה

### 1. שכפול המאגר (Clone)
```bash
git clone https://github.com/stavmay5/Network_Status_Dashboard.git
cd Network_Status_Dashboard
```


### 2. יצירת סביבה וירטואלית (מומלץ)
Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. הגדרות סביבה (env.)
יש ליצור קובץ בשם .env בתיקייה הראשית ולהגדיר בו את המיקום (אופציונלי):

Plaintext
PROJECT_LOCATION=Jaffa, Tel Aviv
### 4. התקנת תלויות
```bash
pip install -r requirements.txt
```

### 5. הרצת השרת
```bash
uvicorn main:app --reload
```
השרת ירוץ בכתובת: http://127.0.0.1:8000


