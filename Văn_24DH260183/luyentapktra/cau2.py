import csv

# Mở file để đọc
file = open("dansoTG.csv", "r", encoding="utf-8")
doc = csv.reader(file)

# Bỏ dòng tiêu đề
next(doc)

print("Danh sách các nước trong thập kỷ 2010s:\n")

# Mở file để ghi
file_moi = open("DansoManh.csv", "w", newline="", encoding="utf-8")
ghi = csv.writer(file_moi)

# Ghi tiêu đề
ghi.writerow(["Country", "Year", "Population", "Population Growth"])

for dong in doc:
    country = dong[0]
    year = dong[2]
    population = dong[3]
    growth = dong[4]
    decade = dong[6]

    # 👉 Câu 2: in dữ liệu thập kỷ 2010s
    if "2010s" in decade:
        print(country, year, population)

    # 👉 Câu 3: ghi vào file nếu tăng trưởng > 200 triệu
    # (200 triệu = 200000000)
    if growth != "":
        if float(growth) > 200000000:
            ghi.writerow([country, year, population, growth])

# Đóng file
file.close()
file_moi.close()

print("\nĐã tạo file DansoManh.csv")