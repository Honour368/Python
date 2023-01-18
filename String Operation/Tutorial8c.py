codebook=[["y","h","s","p","q","e","d","i","r","g","v","x","w","l","u","k","z","o","f","j","a","m","b","n","t","c"],
["r","l","h","p","n","d","k","q","g","j","v","s","z","o","b","m","f","i","a","e","u","t","c","y","x","w"],
["l","i","z","n","c","r","m","b","t","o","u","h","d","x","s","f","a","p","e","q","j","v","w","k","y","g"],
"k q l h a z i j d u s v c r w n o x f p y t e b g m".split(),
"g p f e r s j x w l o k q a c z n u t d h v b m y i".split(),
"h j p l g s d y x m o u b n f t q c z a w v k i r e".split(),
"v m p e y s u k j t l w i c h d f o b a q n g z r x".split(),
"y u j m d q v t e g r i n h s o l k w a z f b p x c".split(),
"m z g f o h e r p l k u a x b i c d j t n s v q w y".split(),
"o p e n j a g r v q t x h d w z b l c u i y s f m k".split()]

#'''for i in range(10):
#    for j in range(26):
#        print(codebook[i][j], end="")
#    print()'''

def encrypt(s):
    b=s.split()     #lists of strings
    counter=0
    for i in range(len(b)):
        c=b[i].lower()      #each string in lower case
        c1=c.strip(",")
        c2=c1.strip("-")
        for j in range(len(c2)):
            if c2[j]==".":
                print(".", end="")
                counter+=1
            elif c2[j]=="@":
                print("@", end="")
                counter+=1
            else:
                row=counter%10
                counter+=1
                #print(row, end=" ")
                d=c2[j]            #accessing the jth letter in c2
                column=(ord(d)-97)
                e=b[i][j]
                if 64<ord(e)<91:    #to check if its capital letter or not
                    print((codebook[row][column]).capitalize(), end="")
                else:
                    print(codebook[row][column], end="")
        counter+=1
        if "," in c:
            counter+=1
            print(",", end="")
        if "-" in c:
            counter+=1
            print("-", end="")
        print(" ", end="")

def decrypt(s):
    b=s.split()    #list of strings
    counter=0
    for i in range(len(b)):
        c=b[i].lower()         #each string in lower case
        c1=c.strip(",")       #strings without comma
        c2=c1.strip("-")
        for j in range(len(c2)):
            if c2[j]==".":
                print(".", end="")
                counter+=1
            elif c2[j]=="@":
                print("@", end="")
                counter+=1
            else:
                row=counter%10
                counter+=1
                d=c2[j]   #accessing the individual letters
                columnno=(codebook[row]).index(d)
                #print(columnno)
                e=b[i][j]
                f=chr(columnno+97)
                if 64<ord(e)<91:    #to check if its capital letter or not
                    print(f.capitalize(), end="")
                else:
                    print(f, end="")
        counter+=1
        if "," in c:
            counter+=1
            print(",", end="")
        if "-" in c:
            counter+=1
            print("-", end="")
        print(" ", end="")
            
a=str(input())
if a[0]=="e":
    b=a[1:]
    encrypt(b)
else:
    b=a[1:]
    decrypt(b)


    
