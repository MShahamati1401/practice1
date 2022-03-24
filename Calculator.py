from math import *

def getnumber():# two numbers get argoman
    number1 = float(input("Plase Insert First Number"))
    number2 = float(input("Plase Insert Second Number"))
    return number1, number2
def convert_radian_to_degre():# one number get argoman
    degree = float(input('''Plase Insert Degree: '''))
    degree = degree * (pi / 180)  # convert degree to radian  ###x = 2.5 * (180/ pi) convert radian to degree
    return degree
def factorial_numbers():
    fac = int(input())
    return fac
################################################################################################
print("1- if Operator is +")
print("2- if Operator is -")
print("3- if Operator is *")
print("4- if Operator is /")
print("5- if Operator is sin")
print("6- if Operator is cos")
print("7- if Operator is tan")
print("8- if Operator is cot")
print("9- Calculate factorial")
print("10- Calculate radical")

op = input("Please choose Number or Operator")# * / - + sin cos tan cot factorial radical

if op == "1" or op == "+":
    number1, number2 = getnumber()
    output = number1 + number2
    print(number1, " + ", number2, " =", output)
elif op == "2" or op == "-":
    number1, number2 = getnumber()
    output = number1 - number2
    print(number1, " - ", number2, " =", output)
elif op == "3" or op == "*":
    number1, number2 = getnumber()
    output = number1 * number2
    print(number1, " * ", number2, " =", output)
elif op == "4" or op == "/":
    number1, number2 = getnumber()
    if number2 == 0:
        print("error not choose zero number for operator")
    else:
        output =round((number1 / number2), 2)
        print(number1, " / ", number2, " =", output)
elif op == "5" or op == "sin":
    degre = convert_radian_to_degre()
    output = round(sin(degre), 2)
    print("Sin(",degre,")", " =", output)
elif op == "6" or op == "cos":
    degre = convert_radian_to_degre()
    output = round(cos(degre), 2)
    print("Cos(",degre,")", " =", output)
elif op == "7" or op == "tan":
    degre = convert_radian_to_degre()
    output =round(tan(degre), 2)
    print("tan(",degre,")", " =", output)
elif op == "8" or op == "cot":
    degre = convert_radian_to_degre()
    output = round(1/tan(degre), 2)
    print("Cot(",degre,")", " =", output)
elif op == "9" or op == "factorial":
    print("Please Number for factorial:")
    fac = factorial_numbers()
    output = factorial(fac)
    print(fac,"!", " =", output)
elif op == "10" or op == "radical":
    print("Please Number for Second Root :", end=" ")
    fac = factorial_numbers()
    output = sqrt(fac)
    print("Second Root ", fac, " =", output)