import pymysql
import time
import random
from datetime import datetime

# Kết nối MySQL
connection = pymysql.connect(
    host='localhost',
    port=3307,
    user='root',
    password='123456',
    database='test'
)
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS data (id INT AUTO_INCREMENT PRIMARY KEY, timestamp VARCHAR(255), value FLOAT)")

data_size = 10**6
print("Đang ghi dữ liệu vào MySQL...")
start = time.time()
for i in range(data_size):
    timestamp = datetime.now().isoformat()
    value = random.random()
    cursor.execute("INSERT INTO data (timestamp, value) VALUES (%s, %s)", (timestamp, value))
connection.commit()
end = time.time()
print(f"Thời gian ghi dữ liệu vào MySQL: {end - start:.2f} giây.")

# Đọc dữ liệu từ MySQL
print("Đang đọc dữ liệu từ MySQL...")
start = time.time()
cursor.execute("SELECT * FROM data")
rows = cursor.fetchall()
end = time.time()
print(f"Thời gian đọc dữ liệu từ MySQL: {end - start:.2f} giây.")
connection.close()
