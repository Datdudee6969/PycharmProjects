from node import Node


def length(head):
    """Returns the number of items in the linked structure
    referred to by head."""
    probe = head
    count = 0
    # ADD CODE HERE: Count the number of nodes in the structure
    # while probe is not None:
    while probe:
        probe = probe.next
        count += 1
    return count


def insert(newItem, head):
    """Inserts newItem at the correct position (ascending order) in
    the linked structure referred to by head.
    Returns a reference to the new structure."""
    node = Node(newItem)
    newNode = Node(newItem)
    tempNode = Node(newItem)
    if node.next is None:
        # node is empty make data equal to node in list followed by a pointer to the head
        node.next = head
        node.data = newItem
        return
    while node.data < newItem:  # ex (data 22) < (item 45)
        if node.next.data < newItem:  # next data in list (data 33) < (item 45)
            insert(newItem, node.next)  # where newItem is, insert node.next instead
        else:
            newNode.data = newItem
            newNode.next = node.next
            node.next = id(newNode)
            return head
    while node.data > newItem:  # ex (data 22) < (item 45)
        if node.next.data > newItem:  # next data in list (data 33) < (item 45)
            insert(newItem, node.next)  # where newItem is, insert node.next instead
        else:
            newNode.data = newItem
            newNode.next = node.next
            node.next = id(newNode)
            return head
        # ADD CODE HERE       need to create every node


def printStructure(head):
    """Prints the items in the structure referred to by head."""
    print(head)



def main():
    """Gets words from the user and inserts in the
    structure referred to by head."""
    head = None
    while True:
        userInput = input('Please enter a word (or just hit enter to end): ')
        if userInput == '':
            break
        head = insert(userInput, head)

    print('The structure contains', length(head), 'items:')
    printStructure(head)


if __name__ == "__main__": main()
