class IndexMinPQ:
    def __init__(self):
        self.index = {}
        self.list = []

    def is_empty(self):
        return len(self.list) == 0

    def enqueue(self, key, value):
        # if key is already in index
        if key in self.index:
            raise ValueError("already enqueued")

        # add element to end of heap (next available position)
        self.list.append([value, key])

        # index of last element
        current_index = len(self.list) - 1

        # update index first
        self.index[key] = current_index

        # compare the new element with parent and if less swap them
        while current_index > 0:
            parent_index = (current_index - 1) // 2

            if self.list[parent_index][0] > self.list[current_index][0]:
                # Update indices before swap
                self.index[self.list[current_index][1]] = parent_index
                self.index[self.list[parent_index][1]] = current_index
                # Swap elements
                self.list[current_index], self.list[parent_index] = self.list[parent_index], self.list[current_index]
                current_index = parent_index
            else:
                break

    def dequeue(self):
        if self.is_empty():
            raise IndexError("list empty")

        # Get the minimum
        min = self.list[0][1]

        # Swap the root with the last element
        self.list[0], self.list[-1] = self.list[-1], self.list[0]

        # Update index for the swapped element if it's not the last one
        if len(self.list) > 1:
            self.index[self.list[0][1]] = 0

        # Remove the last element and its index
        self.list.pop()
        del self.index[min]

        # Move the new root down to keep algo rules
        if self.list:  # Only compare if there are elements left
            self.compare(0)

        return min

    def compare(self, index):
        while True:
            smallest = index
            left_child = 2 * index + 1
            right_child = 2 * index + 2

            #if left child is less than te list and left child is smaller than the smallest
            if left_child < len(self.list) and self.list[left_child][0] < self.list[smallest][0]:
                # update smallest
                smallest = left_child

            #vise versa
            if right_child < len(self.list) and self.list[right_child][0] < self.list[smallest][0]:
                smallest = right_child

            if smallest == index:
                break

            # Update indices before swap
            self.index[self.list[index][1]] = smallest
            self.index[self.list[smallest][1]] = index
            # Swap elements
            self.list[index], self.list[smallest] = self.list[smallest], self.list[index]
            index = smallest

    def reduce_priority(self, key, value):
        if key not in self.index:
            raise KeyError("key not found")

        index = self.index[key]
        old_value = self.list[index][0]

        #value shouldn't exceed old value
        if value > old_value:
            raise ValueError("new value exceeds old value")

        # Update the value
        self.list[index][0] = value

        # Move the element upwards
        while index > 0:
            parent_index = (index - 1) // 2
            if self.list[parent_index][0] > self.list[index][0]:
                # Update indices before swap
                self.index[self.list[index][1]] = parent_index
                self.index[self.list[parent_index][1]] = index
                # Swap elements
                self.list[parent_index], self.list[index] = self.list[index], self.list[parent_index]
                index = parent_index
            else:
                break