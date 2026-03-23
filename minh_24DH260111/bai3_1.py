def TamGiacVuong(n):
    for i in range(n):
        print("*"*i)

TamGiacVuong(5)
print("-----------------")

def TamGiacCan(N):
    for i in range(N):
        print(" "*(N-i), end="")
        print("*"*(2*i+1))

TamGiacCan(4)