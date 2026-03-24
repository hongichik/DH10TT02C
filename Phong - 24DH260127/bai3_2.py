def TamGiacVuong(n):
    for i in range(n):
        print(" * "*i)

TamGiacVuong(5)
print("-------------------")
def TamGiacVuong(n):
    for i in range(n):
        print(" * "*(n-i), end="")
        print("*"*(2*i+1))
    print()
