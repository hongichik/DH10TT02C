def TamGiacVuong(n):
    for i in range (n) :
        print (" * "*i)

TamGiacVuong(5)
print ("=======")
def TamGiacCan (n) :
    for i in range (n) :
        print ("  "*(n-1) , end="")
        print (" * "*(2*1+1) )
        print()
    TamGiacCan(4)


