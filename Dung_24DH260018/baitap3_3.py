def tamGiacCan(n):
    for i in range(n):
        # Tạo cách, dòng dưới = trên -1, dòng cuối không cách
        print(" "*(n-1-i),end=" ")
        # Dòng dưới = dòng trên * 2 + 1
        print("*"*(2*i+1))
tamGiacCan(4)