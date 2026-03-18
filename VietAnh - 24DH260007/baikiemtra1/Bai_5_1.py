# viet "w"
file = open("demo.txt", "w", encoding="utf-8")
file.writelines("Hello,this is a demo file.")
file.write("Chung ta dang hoc ve file trong Python.")
file.writelines(["\nDòng 1\n","Dòng 2\n", "Dòng 3\n" ])
file.close()

