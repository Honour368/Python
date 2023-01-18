m=int(input())  #rows
n=int(input())  #columns

for m in range(1, (int(m)+1), 1):
    for n in range(1, (int(n)+1), 1):
        p=(m*n)
        print(f"{p:>5}", end="")
    print()
