def read(filename):
    file = open(filename, "r")
    lines = file.readlines()
    linesNew = [int(x) for x in lines]
    return linesNew


def TowerOfHanoi(elements, source, destination, auxiliary):
    if elements == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    TowerOfHanoi(elements - 1, source, auxiliary, destination)
    print("Move disk", elements, "from source", source, "to destination", destination)
    TowerOfHanoi(elements - 1, auxiliary, destination, source)


elements = len(read('HanoiTower.txt'))
TowerOfHanoi(elements, 'A', 'C', 'B')
