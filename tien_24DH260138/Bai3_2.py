def TamGiacVuong(n): 
    for i in range(n):
        print("*"*i)
TamGiacVuong(5)
print("--------------------")
def TamGiacCan(n):
    for i in range(n):
        print(" "*(n-i-1),end="")
        print("*"*(2*i+1),end="")
    print()
TamGiacCan(4)                