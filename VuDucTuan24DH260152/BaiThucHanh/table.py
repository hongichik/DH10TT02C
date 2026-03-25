import csv

with open('dansoTG.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)

    du_lieu_manh = []

    print("--- Các nước trong thập kỷ 2010s ---")
    for row in reader:
        if row[6] == '2010s':
            print(f"{row[0]}\t{row[2]}\t{row[3]}")

        if row[4] != "" and float(row[4]) > 200000000:
            du_lieu_manh.append(row)

with open('DansoManh.csv', 'w', newline='', encoding='utf-8') as f_out:
    writer = csv.writer(f_out)
    writer.writerow(header)
    writer.writerows(du_lieu_manh)

print("\nĐã lưu danh sách các nước tăng trưởng mạnh vào DansoManh.csv")
