import pickledb
import time
import random
from datetime import datetime

# Tạo và ghi dữ liệu vào PickleDB
db = pickledb.load("example.db", auto_dump=False)

# Tạo 1 triệu dữ liệu
data_size = 10**6
print("Đang ghi dữ liệu vào PickleDB...")
start = time.time()
for i in range(data_size):
    timestamp = datetime.now().isoformat()
    value = random.random()
    db.set(f"key_{i}", {"timestamp": timestamp, "value": value})
db.dump()  # Lưu dữ liệu xuống file
end = time.time()
print(f"Thời gian ghi dữ liệu vào PickleDB: {end - start:.2f} giây.")

# Đọc dữ liệu từ PickleDB
print("Đang đọc dữ liệu từ PickleDB...")
start = time.time()
for key in db.getall():
    db.get(key)
end = time.time()
print(f"Thời gian đọc dữ liệu từ PickleDB: {end - start:.2f} giây.")
