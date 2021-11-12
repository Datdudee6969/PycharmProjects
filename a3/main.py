def linear_search(list, key):
    numSteps = 0
    for num in list:
        numSteps += 1
        if num == key:
            break
    return numSteps


def average(list):
    total = 0
    average = 0
    for num in list:
        total += num
    average = total / len(list)
    return average


def binary_search(list, key):
    mid = 0
    low = 0
    high = len(list) - 1
    numsteps = 0
    while (high >= low):
        numsteps += 1
        mid = int((high + low) / 2)
        if (list[mid] > key):
            high = mid - 1
        elif (list[mid] < key):
            low = mid + 1
        else:
            break
    return numsteps


def readSorted(filename):
    file = open(filename, "r")
    lines = file.readlines()
    linesNew = [int(x) for x in lines]
    return linesNew


def readKeys(filename):
    file = open(filename, "r")
    line = file.readline()
    values = []
    for value in line.split(' '):
        values.append(int(value))
    return values


def main():
    linearAverage = 0
    binaryAverage = 0
    linearStepHolder = []
    binaryStepHolder = []
    sortedLinear = readSorted("sortedLinearInput.txt")
    sortedBinary = readSorted("sortedBinaryInput.txt")
    keyLinear = readKeys("keyLinear.txt")
    keyBinary = readKeys("keyBinary.txt")
    for num in keyLinear:
        linearStepHolder.append(linear_search(sortedLinear, num))
    linearAverage = average(linearStepHolder)
    for num in keyBinary:
        binaryStepHolder.append(binary_search(sortedLinear, num))
    binaryAverage = average(binaryStepHolder)

    print("Linear Step Counts:", end="")
    print(linearStepHolder)
    print("Linear Step Average: " + str(linearAverage) + "\n")

    print("Binary Step Counts:", end="")
    print(binaryStepHolder)
    print("Binary Step Average: " + str(binaryAverage))


main()

# from HERE ON
# def read(str):
#         file = open("sortedLinearInput.txt", "r")
#         lines = file.readlines()
#         linesNew = [int(x) for x in lines]
#         return linesNew
#
#
#
# def linear_search(linesNew, key):
#
#     comparisons_lin = 0
#     for i in range(len(linesNew)):
#         comparisons_lin = comparisons_lin + 1
#         if linesNew[i] != key:
#             continue
#         else:
#             return comparisons_lin
#     return -1
#
#
# def binary_search(linesNew, key):
#
#
#     low = 0
#     mid = len(linesNew) // 2
#     high = len(linesNew) - 1
#     comparisons_bi = 0
#
#     while high >= low:
#         mid = (high + low) // 2
#         comparisons_bi = comparisons_bi + 1
#         if linesNew[mid] < key:
#             low = mid + 1
#
#         elif linesNew[mid] > key:
#             high = mid - 1
#
#         else:
#             return comparisons_bi,mid
#
#     return -1,-1 # not found
#
#
#
# def main():
#     key = read("keyBinary.txt")
#     for i in range(len(key)):
#         binComp,binIndex = binary_search(read("sortedBinaryInput.txt"), key[i])
#         if binComp == -1:
#             print(key[i] + " was not found.")
#         else:
#             print("Found " + str(key[i]) + " at the index " + str(binIndex) + ". \n With an comparison of: " + str(binComp))
#         linAns = linear_search(read("sortedLinearInput.txt"), key[i])
#         if linAns == -1:
#             print(key + " was not found.")
#         else:
#             print("Found " + str(key[i]) + " at the index " + str(linAns) + ". \n With an comparison of: " + str(linAns))
#
# main()
#


# def binRead():
#         file = open("sortedBinaryInput.txt", "r")
#         lines = file.readlines()
#         linesNew = [int(x) for x in lines]
#         return linesNew
#
# def binKeyRead():
#         file = open("keyBinary.txt", "r")
#         lines = file.readlines()
#         linesNew = [int(x) for x in lines]
#         return linesNew
#
# def linKeyRead():
#         file = open("keyLinear.txt", "r")
#         lines = file.readlines()
#         linesNew = [int(x) for x in lines]
#         return linesNew
#
# def linRead():
#         file = open("sortedLinearInput.txt", "r")
#         lines = file.readlines()
#         linesNew = [int(x) for x in lines]
#         return linesNew
#
# def main():
#     binKey = binKeyRead()
#     linKey = linKeyRead()
#     for i in range(len(binKey)):
#         binComp,binIndex = binary_search(binRead(), binKey[i])
#         if binComp == -1:
#             print(binKey[i] + " was not found.")
#         else:
#             print("Found " + str(binKey[i]) + " at the index " + str(binIndex) + ". \n With an comparison of: " + str(binComp))
#     for i in range(len(linKey)):
#         linAns = linear_search(linRead(), linKey[i])
#         if linAns == -1:
