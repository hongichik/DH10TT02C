def tamgiacvuong(n):
    for i in range(n):
       print("*"*i)
tamgiacvuong(5)
print("----------------")

def tamgiacvuong(n):
    for i in range(n):
        print(" "*(n-i), end="")
        print("*"*(2*i+1))

