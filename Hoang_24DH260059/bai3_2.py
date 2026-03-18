def TamGiacVuong(n):
    for i in range(n):
        print("*"*i)

TamGiacVuong(5)
print("-----------")
def TamGiacCan(n):
    for i in range(n):
        print("   "*(n-1-n), end="")
        print(" * "*(2*i+1))
    print()
TamGiacCan(4)
