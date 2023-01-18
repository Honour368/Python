print("Please enter the number of seconds: ",end='') #the "end=''" prevents python from going to the next line
time = int(input())  #input time in seconds

hour = time//3600         #time in hours
minute = (time%3600)//60  #remaining time in minute
seconds = time%60         #remaining time in seconds

print(f"{time} second(s) = {hour} hour(s) {minute} minute(s) {seconds} second(s)")
