#doc "r"
file = open("demo.txt", "r", encoding="utf-8")
data = file.readlines()
title = data[0].strip().split(",")
name_index = title.index("name")
for line in data:
    print(line.strip().split(","))
file.close()