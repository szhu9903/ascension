
class Node():

    def __init__(self,values):
        self._value = values
        self._children = []

    def __iter__(self):
        return iter(self._children)

    def add_children(self,node):
        self._children.append(node)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    child3 = Node(3)
    child4 = Node(4)
    child5 = Node(5)
    child6 = Node(6)
    root.add_children(child1)
    root.add_children(child2)
    child1.add_children(child3)
    child1.add_children(child4)
    child2.add_children(child5)
    child2.add_children(child6)
    for ch in root.depth_first():
        print(ch._value)


