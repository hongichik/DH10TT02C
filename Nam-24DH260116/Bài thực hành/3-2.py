n = 4

def TamGiacVuong(n):
    for i in range(n):
        print("*"*i)

TamGiacVuong(5)
def TamGiacCan(n):
    for i in range(n):
        print("*"*(n - i), end="")
        print("*"*(2*i+1))
    print()
TamGiacCan(4)