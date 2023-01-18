print("Enter your height in m:",end='')
height = float(input())  #height in m
print("Enter your weight in kg:",end='')
weight = float(input())  #weight in kg

BMI = weight/(height**2)

print("Your BMI is {:0.2f}".format(BMI))
