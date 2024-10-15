import math

""" Body Mass Index """
print("Calculate Body Mass Index")
print("-" * 30)

def calculate_bmi(weight, height):
    """ The height will be converted to meter type """
    m_height = height / 100
    bmi = weight / math.pow(m_height, 2)
    return bmi

weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

""" Invoke the function """
bodyMassIndex = calculate_bmi(weight, height)

""" Result"""
print(f"Your BMI is {bodyMassIndex:.2f}")


""" Status is according to body mass index """
if bodyMassIndex < 18.5:
    status = "Underweight"
elif 18.5 <= bodyMassIndex < 25:
    status = "Normal"
elif 25 <= bodyMassIndex < 39:
    status = "Overweight"
else:
    status = "Obese"

print(f"Status: {status}")