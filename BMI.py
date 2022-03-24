def get_number():
    number = float(input())
    return number
#############################################################
print("Please Inter weight based on Kg : ", end=" ")
weight = get_number()
print("Please Inter Height based on Metres : ", end=" ")
height = float(input())
output = weight/(height ** 2)
if output < 18.5:
    print("BMI is Underweight")
elif 18.5 <= output < 25:
    print("BMI is Normal")
elif 25 <= output < 30:
    print("Overweight")
elif 30 <= output < 35:
    print("Obesity")
elif 35 <= output:
    print("Extremely_Obese")