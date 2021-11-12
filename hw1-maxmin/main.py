# group: 40
#
# Kyron Claitt U74837309

def minMax(numArray):
    minNum = 99999
    maxNum = -99999
    for num in numArray:
        if num > maxNum:
            maxNum = num
        if num < minNum:
            minNum = num
    return minNum, maxNum

def read():
    file = open("TestInputHW1.txt", "r")
    print("Name of the file: ", file.name)
    line = file.readline()
    values = []
    for value in line.split(' '):
        values.append(int(value))
        file.readline()
    return values




# numRange = minMax([1, 4, 9, 11, 8, 3, 2, 5, 10])
# print("The minimum of the array is: {}\n The maximum of the array is: {}".format(numRange[0], numRange[1]))

numbers = read()
changePoints = []
for num in range(1, len(numbers) - 1):
    if numbers[num - 1] < numbers[num] and numbers[num + 1] < numbers[num]:
        changePoints.append(numbers[num])
        changePoints.append(numbers[num + 1])
    elif numbers[num - 1] > numbers[num] and numbers[num + 1] > numbers[num]:
        changePoints.append(numbers[num])
        changePoints.append(numbers[num + 1])
print("change points: {}".format(changePoints))
