def readm1(filename):
    file = open(filename, "r")
    lines = file.readlines()
    a = []
    for line in lines:
        b = []
    for x in line.strip('\n').split(' '):
        b.append(int(x))
        a.append(b)
    return a


def main():
    hwm1 = readm1('hw2-m1.txt')
    hwm2 = readm1('hw2-m2.txt')
    len1 = len(readm1('hw2-m1.txt'))
    len2 = len(readm1('hw2-m2.txt'))
    ans = [[0 for hwm1 in range(len1)] for y in range(len2)]
    for i in range(len1):
        for j in range(len1):
            ans[i][j] = hwm2[i][j] + hwm1[i][j]

        for r in ans:
            print(r)

    if r != range(len1):
        print('the matrix dimensions do not match')


main()




# Program to add two matrices using nested loop

# X = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# Y = [[9, 8, 7],
#      [6, 5, 4],
#      [3, 2, 1]]
#
# result = [[0, 0, 0],
#           [0, 0, 0],
#           [0, 0, 0]]
#
# # iterate through rows
# for i in range(len(X)):
#     # iterate through columns
#     for j in range(len(X[0])):
#         result[i][j] = X[i][j] + Y[i][j]
#
# for m in result:
#     print(m)
