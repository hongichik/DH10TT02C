def Tamgiacvuong(n):
    for i in range(n):
        print(" * "*i)


Tamgiacvuong(5)
print("-------------")
def Tamgiaccan(n):
    for i in range(n):
        print("  "*(n-i), end="")
        print("  *  "*(2*i+1))
    print()