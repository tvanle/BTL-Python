from datetime import datetime
import pymysql
import time
import random

def mysql_test(data_size):
    connection = pymysql.connect(
        host='localhost',
        port=3307,
        user='root',
        password='123456',
        database='test'
    )
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS data (id INT AUTO_INCREMENT PRIMARY KEY, timestamp VARCHAR(255), value FLOAT)")

    # Writing data
    start = time.time()
    for i in range(data_size):
        timestamp = datetime.now().isoformat()
        value = random.random()
        cursor.execute("INSERT INTO data (timestamp, value) VALUES (%s, %s)", (timestamp, value))
    connection.commit()
    write_time = time.time() - start

    # Reading data
    start = time.time()
    for i in range(1, data_size + 1):
        cursor.execute("SELECT * FROM data WHERE id = %s", (i,))
        cursor.fetchone()
    read_time = time.time() - start

    connection.close()
    return write_time, read_time

if __name__ == "__main__":
    data_size = 10**3
    write_time, read_time = mysql_test(data_size)
    print(f"Thời gian ghi: {write_time:.2f} giây")
    print(f"Thời gian đọc: {read_time:.2f} giây")