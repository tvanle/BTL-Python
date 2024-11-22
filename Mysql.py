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
cursor.execute("CREATE TABLE IF NOT EXISTS data (id INT PRIMARY KEY, timestamp VARCHAR(255), value FLOAT)")

data_size = 10**4  # Số lượng dữ liệu cần ghi
print("Đang ghi dữ liệu vào MySQL...")
start = time.time()
for i in range(1, data_size + 1):  # ID sẽ bắt đầu từ 1 và tăng dần
    timestamp = datetime.now().isoformat()
    value = random.random()
    cursor.execute("INSERT INTO data (id, timestamp, value) VALUES (%s, %s, %s)", (i, timestamp, value))
connection.commit()
end = time.time()
print(f"Thời gian ghi dữ liệu vào MySQL: {end - start:.2f} giây.")

# Đọc dữ liệu từ MySQL
print("Đang đọc dữ liệu từ MySQL...")
start = time.time()
for i in range(1, data_size + 1):  # Lặp qua từng ID
    cursor.execute("SELECT * FROM data WHERE id = %s", (i,))
end = time.time()
print(f"Thời gian đọc dữ liệu từ MySQL: {end - start:.2f} giây.")

connection.close()
