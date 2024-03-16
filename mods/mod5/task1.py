class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None

class Stack:
    def __init__(self):
        self.end = None

    def pop(self):
        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        node = Node(val)
        node.pref = self.end
        self.end = node

    def print(self):
        node = self.end
        while node is not None:
            print(node.data)
            node = node.pref