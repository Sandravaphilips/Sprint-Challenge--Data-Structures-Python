
from doubly_linked_list import DoublyLinkedList, ListNode


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.storage = DoublyLinkedList()
        self.storage.add_to_head(value)

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:                
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else: self.right.insert(value)
        self.storage.add_to_head(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        return self.storage.get_max()

    def iter(self):        
        current = self.storage.head
        while current:
            item = current.value
            current = current.next
            yield item

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        for i in self.iter():
            cb(i)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)
        else: return



    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if node:
            node_list = DoublyLinkedList()
            node_list.add_to_head(node)

            while len(node_list) > 0:
                current = node_list.remove_from_head()
                print(current.value)

                if current.left:
                    node_list.add_to_tail(current.left)
                if current.right:
                    node_list.add_to_tail(current.right)
        else: return


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        if node:            
            node_list = DoublyLinkedList()
            node_list.add_to_head(node)

            while len(node_list) > 0:
                current = node_list.remove_from_head()
                print(current.value)

                if current.left:
                    node_list.add_to_head(current.left)
                if current.right:
                    node_list.add_to_head(current.right)
        else: return

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            print(node.value)
            self.pre_order_dft(node.left)
            self.pre_order_dft(node.right)
        else: return

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)
            print(node.value)
        else: return


