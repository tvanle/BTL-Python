import sqlite3
import random
import time
from datetime import datetime


def sqlite_test(data_size):
    connection = sqlite3.connect('test_sqlite.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp TEXT, value REAL)")

    # Writing data
    start = time.time()
    for i in range(data_size):
        timestamp = datetime.now().isoformat()
        value = random.random()
        # cursor.execute("INSERT INTO data (timestamp, value) VALUES (?, ?)", (timestamp, value))
    connection.commit()
    write_time = time.time() - start

    # Reading data
    start = time.time()
    for i in range(1, data_size + 1):
        cursor.execute("SELECT * FROM data WHERE id = ?", (i,))
        row = cursor.fetchone()
    read_time = time.time() - start

    connection.close()
    return write_time, read_time


if __name__ == "__main__":
    data_size = 10 ** 3
    write_time, read_time = sqlite_test(data_size)
    print(f"Thời gian ghi: {write_time:.2f} giây")
    print(f"Thời gian đọc: {read_time:.2f} giây")
