def get_number():
    number = int(input())
    return number
fac = []
print("Plase Insert 3 Numbers for Ability to draw a triangle : ")

for i in range(0, 3):
    fac.append(get_number())
    fac.sort()
if (fac[-2] + fac[-3]) > fac[-1]:
    print("Yes Ability to draw a triangle")
else:
    print("Not Ability to draw a triangle")