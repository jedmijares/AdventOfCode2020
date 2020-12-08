input = open(r"./input/d1p1.txt", "r")

availableNumbers = [False] * 2021 

for line in input:
    num = int(line)
    availableNumbers[num] = True

for number, present in enumerate(availableNumbers):
    if(present):
        if (availableNumbers[2020 - number]):
            print(number * (2020 - number))
            break