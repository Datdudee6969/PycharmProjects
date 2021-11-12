from node import Node

def middleSplit(head):
    if head == None or head.next == None:
        return head, None

    moveOne = head
    moveTwo = head.next

    while moveTwo is not None:
        moveTwo = moveTwo.next 
        if moveTwo is not None:
            moveOne = moveOne.next
            moveTwo = moveTwo.next 
    return moveOne

def mergeSplit(head):
    if head == None or head.next == None:
        return head

    breakSpot = middleSplit(head)
    nextStart = breakSpot.next 
    breakSpot.next = None
    leftSide = mergeSplit(head)
    rightSide = mergeSplit(nextStart)

    return mergeSort(leftSide, rightSide)

def mergeSort(leftValue, rightValue):
    listContainer = None
    if leftValue == None:
        return rightValue
    elif rightValue == None:
        return leftValue

    if leftValue.data <= rightValue.data:
        listContainer = leftValue
        listContainer.next = mergeSort(leftValue.next, rightValue)
    else:
        listContainer = rightValue
        listContainer.next = mergeSort(leftValue, rightValue.next)

    return listContainer

def createList(fileName, head):
    file = open(fileName, "r")
    line = file.readline()
    currNode = head
    for value in line.split(" "):
        node = Node(int(value))
        if head.data == None:
            head.data = node.data
            head.next = None
        else:
            while currNode.next:
                currNode = currNode.next 
            currNode.next = node
            currNode = head
    return head

def printStructure(head):
    currNode = head
    while currNode:
        print(currNode.data, end=" ")
        currNode = currNode.next 

def main():
    head = Node(None)
    createList("hw5-2.txt", head)
    head = mergeSplit(head)
    printStructure(head)

main()
