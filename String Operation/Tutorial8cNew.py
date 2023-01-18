codebook=["yhspqedirgvxwlukzofjambntc",
"rlhpndkqgjvszobmfiaeutcyxw",
"lizncrmbtouhdxsfapeqjvwkyg",
"kqlhazijdusvcrwnoxfpytebgm",
"gpfersjxwlokqacznutdhvbmyi",
"hjplgsdyxmoubnftqczawvkire",
"vmpeysukjtlwichdfobaqngzrx",
"yujmdqvtegrinhsolkwazfbpxc",
"mzgfoherplkuaxbicdjtnsvqwy",
"openjagrvqtxhdwzblcuiysfmk"]

def encrypt(s):
    count=0
    for i in s:
        if i.isalpha():
            if i.isupper():
                row=count%10
                count+=1
                column=ord(i)-65
                print((codebook[row][column]).upper(), end="")
            else:
                row=count%10
                count+=1
                column=ord(i)-97
                print((codebook[row][column]), end="")
        else:
            count+=1
            print(i, end="")
def decrypt(s):
    count=0
    for i in s:
        if i.isalpha():
            if i.isupper():
                j=i.lower()
                row=count%10
                count+=1
                d=((codebook[row]).index(j))+97
                alphabet=chr(d)
                print(alphabet.upper(), end="")
            else:
                row=count%10
                count+=1
                d=((codebook[row]).index(i))+97
                alphabet=chr(d)
                print(alphabet, end="")
        else:
            count+=1
            print(i, end="")

a=input()
if a[0]=="e":
    a=a[1:]
    encrypt(a)
else:
    a=a[1:]
    decrypt(a)
