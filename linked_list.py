class Node:
    data=None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


class Linked_list:

    def __init__(self):
        self.head = None

#empty method
    def is_empty(self):
        return self.head == None

#size method
    def size(self):
        count = 0
        current = self.head
        
        while current:
            count += 1
            current = current.next_node
        return count

#prepend method
    def add(self,data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

#search method
    def search(self,key):
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

#Insert method
    def insert(self, data, index):
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)
            position = index
            current = self.head
        
            while position > 1:
                current = Node.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

#Delete method
    def remove(self,key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

