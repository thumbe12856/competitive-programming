class Node:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return self.val

a = Node(2)
b = Node(1)
c = [a, b]
print(sorted(c))
