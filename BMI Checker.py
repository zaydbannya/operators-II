height=float(input("Enter your height in cm:"))
weight=float(input("Enter your weight in Kg:"))
BMI=weight/(height/100)**2
print("your BMI is",BMI)
if BMI<=18.4:
    print("your are under weight")
elif BMI<=24.9:
    print("you are healthy")
elif BMI<=29.9:
    print("you are over weight")
elif BMI<=34.9:
    print("you are servesly over weight")
elif BMI<=39.9:
    print("you are obese")
else:
    print("you are servely obese")