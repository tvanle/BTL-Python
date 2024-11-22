import pandas as pd
import matplotlib.pyplot as plt

from Mysql import mysql_test
from Pickledb import pickledb_test
from Sqlite3 import sqlite_test


def main():
    record_sizes = [100, 300, 500,800, 1000, 2000]  # Test with these record sizes
    results = []

    for size in record_sizes:
        print(f"Testing with {size} records...")
        mysql_write, mysql_read = mysql_test(size)
        sqlite_write, sqlite_read = sqlite_test(size)
        pickledb_write, pickledb_read = pickledb_test(size)

        x = {
            'Record Size': size,
            'MySQL Write': mysql_write,
            'MySQL Read': mysql_read,
            'SQLite Write': sqlite_write,
            'SQLite Read': sqlite_read,
            'PickleDB Write': pickledb_write,
            'PickleDB Read': pickledb_read
        }
        results.append({
            'Record Size': size,
            'MySQL Write': mysql_write,
            'MySQL Read': mysql_read,
            'SQLite Write': sqlite_write,
            'SQLite Read': sqlite_read,
            'PickleDB Write': pickledb_write,
            'PickleDB Read': pickledb_read
        })

    df = pd.DataFrame(results)

    # Plotting the results using pandas plot
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Plot write time comparison
    df.plot(x='Record Size', y=['MySQL Write', 'SQLite Write', 'PickleDB Write'], kind='bar', ax=axes[0], title='Write Time Comparison', xlabel='Number of Records', ylabel='Time (seconds)',
            legend=True)

    # Plot read time comparison
    df.plot(x='Record Size', y=['MySQL Read', 'SQLite Read', 'PickleDB Read'], kind='bar', ax=axes[1], title='Read Time Comparison', xlabel='Number of Records', ylabel='Time (seconds)', legend=True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
