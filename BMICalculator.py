height = float(input("enter your height in cm: "))
weight = float(input("enter your weight in kg: "))

BMI = round(weight / (height/100 * height/100))
Print("Welcome")
if BMI < 18.5:
    print("Your BMI is " + str(BMI) + ", " + "you are underweight.")
elif BMI < 25:
    print("Your BMI is " + str(BMI) + ", " + "you have a normal weight.")
elif BMI < 30:
    print("Your BMI is " + str(BMI) + ", " + "you are slightly overweight.")
elif BMI < 35:
    print("Your BMI is " + str(BMI) + ", " + "you are obese.")
else:
    print("Your BMI is " + str(BMI) + ", " + "you are clinically obese.")
