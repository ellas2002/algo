

###################################################################
#######Home Work: Ella Stiller######################################
###################################################################

class Node:
    def __init__(self, data): #NODES!!!!!!
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        current = self.head
        elements = []
        result = '<'
        while current:
            result += str(current.data)
            if current.next:  # Add a comma if there's a next element
                result += ', '
            current = current.next
        result += '>'
        return result


    def add_front(self, data):
        # "creates a new node using data"
        new_node = Node(data)
        # "checks tp see if list is empty and if so update point to create new node"
        if not self.head:
            self.head = self.tail = new_node
        # if not empty
        else:
            # new nodes next pointer is set to current head node
            new_node.next = self.head
            # "current head nodes prev point is updated to point to new_nodes"
            self.head.prev = new_node
            # "head point is updated to new node and becomes first node in the list"
            self.head = new_node


    def add_back(self, data):
        old_node = Node(data)
        if not self.tail:
            self.tail = self.head = old_node
        else:
            #current nodes previous points is set to current tail node
            old_node.prev = self.tail
            #current tail node next point is set to point to old node
            self.tail.next = old_node
            #current tail is set to old node
            self.tail = old_node


    def remove_front(self):
        #if empty, print cannot remove
        if not self.head:
            print("empty")
        if self.head == self.tail:  # Only one element in the list
            self.head = self.tail = None #None in the list
        else:
            # removes node becasue the current head now will be the new head for the next node
            self.head = self.head.next #moves hea
            # sets the new head as not longer points t the previous node, because new head is now first node
            self.head.prev = None


    def remove_back(self):
        if not self.tail:
            print("empty")
        if self.tail == self.head:
            self.tail = self.head = None
        else:
            # removes node becasue the current tail now will be the new tail for the next node
            self.tail = self.tail.prev
            #sets the new tail to no longer points to the next node, because new tail is now first node
            self.tail.next = None


    def concatenate(self, list):
        if list.head is None: #empty
            print("empty")
        if self.head is None: #empty
            self.head = list.head
            self.tail = list.tail
        else:
            #update next in tail to be head of new list
            self.tail.next = list.head
            #update new list head to be tail of current list
            list.head.prev = self.tail
            #update tail of current list to be tail of new list
            self.tail = list.tail


#######################################################
############################test it#####################
#######################################################

list = DoublyLinkedList()
new_list = DoublyLinkedList()

list.add_back(1)
list.add_back(2)
list.add_back(3)
list.add_back(4)

new_list.add_front(1)
new_list.add_front(2)
new_list.add_front(3)
new_list.add_front(4)

print("List after adding nodes:")
print(list)

list.add_back(8)
print("list after add back")
print(list)

list.remove_front()
print("List after removing the front node:")
print(list)

list.remove_back()
print("List after removing the last node:")
print(list)

list.concatenate(new_list)
print("List after concatenating:")
print(list)







