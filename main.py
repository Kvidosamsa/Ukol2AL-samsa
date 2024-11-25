import random

# 1.pole s nahodnyma cislama do 100
pole = [random.randint(0, 100) for _ in range(10)]
print("Náhodné pole:", pole)

# 2.pole serazene pomoci sort
serazene_pole = sorted(pole)
print("Seřazené pole:", serazene_pole)
# ------------------------------------------------------------

pole = [88, 76, 3, 90, 21, 10, 1, 65, 43, 28]

def bubble_sort():
    n = len(pole)
    for i in range(n-1):
        for j in range (0,n-i-1):
            if pole[j] > pole[j + 1]:  
                pole[j], pole[j + 1] = pole[j + 1], pole[j]
            print(pole)
    return pole

pole = [88, 76, 3, 90, 21, 10, 1, 65, 43, 28]
serazene_pole = bubble_sort()
print("Seřazené pole pomocí bubble sort:", serazene_pole)
