from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) >= self.capacity:
            if self.current == None:
                self.current = self.storage.head
            if self.current == self.storage.tail:
                next_value = self.storage.head
                self.storage.remove_from_tail()   
                self.storage.add_to_tail(item) 
            else:
                next_value = self.current.next
                self.storage.insert_after(self.current, item)
                self.storage.delete(self.current)
            self.current = next_value
        else:
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current = self.storage.head
        while current:
            list_buffer_contents.append(current.value)
            current = current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None]* capacity
        self.current = 0

    def append(self, item):
        self.storage[self.current] = item
        self.current += 1
        if self.current == self.capacity:
            self.current = 0
        

    def get(self):
        return [i for i in self.storage if i]
