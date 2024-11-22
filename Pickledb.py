import random
import time
from datetime import datetime
import pickledb

def pickledb_test(data_size):
    db = pickledb.load('test_pickle.db', auto_dump=True)

    # Writing data
    start = time.time()
    for i in range(1, data_size + 1):
        timestamp = datetime.now().isoformat()
        value = random.random()
        db.set(str(i), {'timestamp': timestamp, 'value': value})
    write_time = time.time() - start

    # Reading data
    start = time.time()
    for i in range(1, data_size + 1):
        val = db.get(str(i))
    read_time = time.time() - start

    db.dump()
    return write_time, read_time

if __name__ == "__main__":
    data_size = 10**3
    write_time, read_time = pickledb_test(data_size)
    print(f"Thời gian ghi: {write_time:.2f} giây")
    print(f"Thời gian đọc: {read_time:.2f} giây")