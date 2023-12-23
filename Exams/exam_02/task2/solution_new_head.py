class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def add(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.get_data(), end =" ");
            current = current.get_next()

    def removeComplex(self,k):
        """Function to solve."""
        if not self.head:
            return
        
        # Find the new head - first element not divisible by k
        current = self.head
        while current and current.data % k == 0:
            current = current.next_node
        self.head = current
        
        if not self.head:
            return
        
        # Continue removing by having the prev element
        prev = current
        current = current.next_node
        
        while current:
            if current.data % k == 0:
                prev.next_node = current.next_node
            else:
                prev = prev.next_node
            current = current.next_node
        
        
l = LinkedList();
n = input();
numbers = list(map(int, input().split()))
for i in numbers:
    l.add(i);
k = int(input())

l.removeComplex(k)
l.print_list();