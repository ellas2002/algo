class Node:
    def __init__(self, data): #NODES!!!!!!
        self.data = data #need data :0
        self.prev = None #previosu node set to None
        self.next = None #next node set to None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        


if __name__ == "__main__":
    # Create a doubly linked list with 3 nodes
    head = Node(1)
    second = Node(2)
    third = Node(3)

    head.next = second
    second.prev = head
    second.next = third
    third.prev = second

    print("Forward Traversal:")
    forward_traversal(head)

    print("Backward Traversal:")
    backward_traversal(third)