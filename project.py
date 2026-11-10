# __AGE CALCULATOR AND BMI CALCULATOR___

print("Welcome to the Age and BMI Calculator!")
print("Please enter your details below:")

birth_year = int(input("Enter your birth year (YYYY): "))
birth_month = int(input("Enter your birth month (MM): "))
birth_day = int(input("Enter your birth day (DD): "))

current_year = int(input("Enter current year (YYYY): "))    
current_month = int(input("Enter current month (MM): "))
current_day = int(input("Enter current day (DD): "))


age = current_year - birth_year

if (current_month, current_day) < (birth_month, birth_day):
    age -= 1

if age < 0:
    print("Invalid date of birth!")

else:
    print(f"Your age is: {age}")

height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in kilograms: "))

if height > 0 and weight > 0:
    bmi_ = weight / ((height / 100) ** 2)
    print(f"Your BMI is: {round(bmi_, 2)}")

else:
    print("Please enter valid height and weight!")

print(f"Your BMI is: {round(bmi_, 2)}")

if age >= 20:

    if bmi_ < 18.5:
        print("Category: Underweight")

    elif bmi_ < 25:
        print("Category: Healthy weight")

    elif bmi_ < 30:
        print("Category: Overweight")

    else:
        print("Category: Obesity")

else:
    print("BMI-for-age assessment required.")
    print("Please refer to age-specific growth charts.")
    




































































