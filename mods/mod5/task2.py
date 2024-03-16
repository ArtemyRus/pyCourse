class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def pop(self):
        val = self.start.data
        self.start = self.start.nref
        return val

    def push(self, val):
        node = Node(val)
        if self.start is None:
            self.start = node
            self.end = self.start
        else:
            self.end.nref = node
            node.pref = self.end
            self.end = node

    def insert(self, n, val):
        insertNode = Node(val)
        node = self.start
        if(n < 1):
            node.pref = insertNode
            insertNode.nref = node
            self.start = insertNode
            return
        while node is not None and n > 0:
            n -= 1
            node = node.nref
        if node is None:
            last = self.end
            last.nref = insertNode
            insertNode.pref = last
            self.end = insertNode
        else:
            prevNode = node.pref
            prevNode.nref = insertNode
            insertNode.pref = prevNode
            insertNode.nref = node
            node.pref = insertNode

    def print(self):
        node = self.start
        while node is not None:
            print(node.data)
            node = node.nref