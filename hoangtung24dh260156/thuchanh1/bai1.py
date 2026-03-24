def tamgiacvuong(n):
    for i in range(n):
        print(" * "*i)

        tamgiacvuong(5)
        print("---------------------")
        def tamgiaccan(n):
            for i in range(n):
                for i in range(n):
                    print("     "*(n-1), end="")
                    print(" * "*(2*i+1))
                print()
            tamgiaccan(4)            