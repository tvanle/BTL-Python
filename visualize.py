import matplotlib.pyplot as plt

# Kết quả đo thời gian (giả định bạn đã chạy và thu thập thời gian từ các đoạn mã trên)
databases = ["PickleDB", "SQLite", "MySQL"]
write_times = [12.34, 3.21, 1.45]  # Thời gian ghi (giây) - ví dụ
read_times = [10.12, 2.34, 0.98]   # Thời gian đọc (giây) - ví dụ

# Biểu đồ cột
plt.figure(figsize=(12, 6))

# Ghi dữ liệu
plt.bar(databases, write_times, color='skyblue', label="Ghi dữ liệu")
# Đọc dữ liệu
plt.bar(databases, read_times, color='orange', label="Đọc dữ liệu", alpha=0.8)

# Thêm nhãn và tiêu đề
plt.title("So sánh thời gian đọc và ghi giữa các cơ sở dữ liệu", fontsize=14)
plt.ylabel("Thời gian (giây)", fontsize=12)
plt.xlabel("Loại cơ sở dữ liệu", fontsize=12)
plt.legend()

# Hiển thị biểu đồ
plt.tight_layout()
plt.show()