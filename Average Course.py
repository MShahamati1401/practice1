elif op == "13" or op == "average":
    number = 0
    name = input("name student: ")
    family = input("family student: ")
    for i in range(0, 3):
        number += float(input("Score Course1: "))
    average = number / 3
    if 12 <= average <17:
        status = "Normal"
    if 17 <= average <=20:
        status = "Great"
    if 0 <= average < 12:
        status = "Fail"
    print("The Students", name, " ", family, " ", "average Course = ", round(average, 2), "and Status =", status)
