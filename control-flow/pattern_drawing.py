# Develop a Python script named pattern_drawing.py. This script will prompt the user to enter a positive integer, then use nested loops to print a square pattern of that size made of asterisks (*).

size = int(input("Enter the size of the pattern: "))
i = 0
while i < size:
    j = 0
    for j in range(size):
        print("*", end=" ")
    print()
    i += 1
    j += 1