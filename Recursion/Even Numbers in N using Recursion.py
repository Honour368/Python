def even(n):
    if n==0:
        return n
    if n%2==0:
        print(f"{n}",end=" ")
    even(n-1)

even(int(input()))