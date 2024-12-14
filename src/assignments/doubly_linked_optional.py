class Node:
    def __init__(self, data): #NODES!!!!!!
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedListOpt:
    def __init__(self):
        self.head = None
        self.tail = None

    #############returs a rep with the elements in reverse########
    def __str__(self):
        current = self.tail
        elements = []
        result = '<'
        while current:
            result += str(current.data)
            if current.prev:  # Add a comma if there's a next element
                result += ', '
            current = current.prev
        result += '>'
        return result


    def add_front(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def add_back(self, data):
        old_node = Node(data)
        if not self.tail:
            self.tail = self.head = old_node
        else:
            old_node.prev = self.tail
            self.tail.next = old_node
            self.tail = old_node

    def remover(self, data):
        item = Node(data)

        if self.head == self.tail:  # Only one element in the list
            self.head = self.tail = None #None in the list

        if(item == self.head):
            self.head = self.head.next  # moves hea
            self.head.prev = None

        if(item == self.tail):
            self.tail = self.tail.prev
            self.tail.next = None









    def remove_front(self):
        if not self.head:
            print("empty")
        if self.head == self.tail:  # Only one element in the list
            self.head = self.tail = None #None in the list
        else:
            self.head = self.head.next #moves hea
            self.head.prev = None


    def remove_back(self):
        if not self.tail:
            print("empty")
        if self.tail == self.head:
            self.tail = self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None


###############puts the items into reverse order###############
    def reversed(self):
        current = self.head

        if not self.head:
            print("empty")

        self.head, self.tail = self.tail, self.head

        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev

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

list = DoublyLinkedListOpt()
new_list = DoublyLinkedListOpt()

list.add_back(1)
list.add_back(2)
list.add_back(4)
list.add_back(3)
list.add_back(4)
list.add_back(4)

new_list.add_front(1)
new_list.add_front(2)
new_list.add_front(3)
new_list.add_front(4)


print("List after adding nodes:")
print(list)

# list.reversed()
# print("list in reversed order")
# print(list)

list.remover(4)
print("list without 4")
print(list)

#
# list.add_back(8)
# print("list after add back")
# print(list)
#
# list.remove_front()
# print("List after removing the front node:")
# print(list)
#
# list.remove_back()
# print("List after removing the last node:")
# print(list)
#
# list.concatenate(new_list)
# print("List after concatenating:")
# print(list)