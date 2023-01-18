s=input()
s1=s.split(",")

for c in s1:
    s2=c.strip()
    if "0x" in s2:
        print(int(s2, 16), end=" ")
    elif ("0x" not in s2) and ("x" in s2):
        s3="0"+s2[1:]
        print(int(s3, 16), end=" ")
    else:
        print(str(s2), end=" ")
