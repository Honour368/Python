a = round(float(input()), 2)
b = '{:0.2f}'.format(a)           #this format style works for other things and not just the "print" function.
c = str(b).replace('.' , ',')     #'replace' only works with strings
print(c)



#b = f"{a:0.2f}" also works
