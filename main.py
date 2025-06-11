from fastapi import FastAPI
import socket

from ping3 import ping, verbose_ping
from typing import Optional # נוסיף את זה כדי לציין שערך יכול להיות גם None

# יצירת מופע (אובייקט) של FastAPI
app = FastAPI()

def get_ping_details(hostname: str) -> dict:
    """
    Performs a ping to the given hostname and returns details.
    Returns None if the host is unreachable or an error occurs.
    """
    try:
        delay = ping(hostname, unit='ms')  # מבצע פינג ומקבל את העיכוב במילישניות
        if delay is None:
            return {"host": hostname, "status": "unreachable", "rtt_ms": None}
        elif delay is False: # יכול לקרות במקרים מסוימים של timeout או שגיאה
            return {"host": hostname, "status": "error_or_timeout", "rtt_ms": None}
        else:
            return {"host": hostname, "status": "reachable", "rtt_ms": round(delay, 2)}
    except Exception as e:
        # במקרה של שגיאה כלשהי (למשל, שם דומיין לא קיים)
        print(f"Error pinging {hostname}: {e}")
        return {"host": hostname, "status": "error", "error_message": str(e), "rtt_ms": None}

# אפשרות נוספת עם יותר פירוט (verbose_ping) - יכולה להיות שימושית לבדיקות
# verbose_ping(hostname, count=4, interval=1) # ידפיס את תוצאות הפינג לטרמינל

# הגדרת נתיב (route) ראשון עבור בקשות GET לכתובת הבסיסית "/"
@app.get("/")
async def read_root():
    return {"message": "Network Status Dashboard API is running!"}

# נתיב נוסף לבדיקה
@app.get("/test")
async def test_endpoint():
    return {"status": "Test successful", "project_location": "Rishon LeTsiyon"}

@app.get("/ping/{hostname}")
async def ping_specific_host(hostname: str):
    ping_result = get_ping_details(hostname)
    return ping_result

@app.get("/check_port/{hostname}/{port}")
async def check_specific_port(hostname: str, port: int):
    port_result = check_port_status(hostname, port)
    return port_result

def check_port_status(hostname: str, port: int) -> dict:
    """
    Checks if a specific TCP port is open on the given hostname.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # קובע Timeout של שנייה אחת לניסיון החיבור

    try:
        # נסי להתחבר לשרת בפורט הנתון
        result_code = sock.connect_ex((hostname, port))
        # connect_ex מחזיר 0 אם החיבור הצליח
        if result_code == 0:
            status = "open"
        else:
            status = "closed" # או "filtered" אם יש חומת אש
    except socket.gaierror: # לא ניתן לתרגם את שם השרת לכתובת IP
        status = "hostname_not_found"
    except socket.error: # שגיאת רשת כללית
        status = "connection_error"
    finally:
        sock.close() # חשוב לסגור את הסוקט

    return {"host": hostname, "port": port, "status": status}