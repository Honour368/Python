s=input()
s1=s.split(",")

for c in s1:
    if "x" in c:
        print(int(c, 16), end=" ")
    else:
        print(str(c), end=" ")
