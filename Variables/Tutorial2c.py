print("Please enter the number of seconds: ",end='')
time = int(input())  #input time in seconds

minute = time//60  #time in minute
seconds = time%60  #remaining time in seconds

print(f"{time} second(s) = {minute} minute(s) {seconds} second(s)")
