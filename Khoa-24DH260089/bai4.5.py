list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2
print(list3)

for i in range(len(list3)):
    list3[i] = list3[i]*2
    print(list3)