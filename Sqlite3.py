import sqlite3
import time
import random
from datetime import datetime

# Tạo và ghi dữ liệu vào SQLite
conn = sqlite3.connect("example.sqlite")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, timestamp TEXT, value REAL)")

data_size = 10**6
print("Đang ghi dữ liệu vào SQLite...")
start = time.time()
for i in range(data_size):
    timestamp = datetime.now().isoformat()
    value = random.random()
    cursor.execute("INSERT INTO data (timestamp, value) VALUES (?, ?)", (timestamp, value))
conn.commit()
end = time.time()
print(f"Thời gian ghi dữ liệu vào SQLite: {end - start:.2f} giây.")

# Đọc dữ liệu từ SQLite
print("Đang đọc dữ liệu từ SQLite...")
start = time.time()
cursor.execute("SELECT * FROM data")
rows = cursor.fetchall()
end = time.time()
print(f"Thời gian đọc dữ liệu từ SQLite: {end - start:.2f} giây.")
conn.close()
