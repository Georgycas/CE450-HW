class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.start_node = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node;

    def traverse_list(self):
        z = 0
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                z = z + n.item
                n = n.ref
            print(z)


def sum_lnk(lnk, g):
    new_linked_list = LinkedList()
    for y in range(len(lnk)):
        if lnk[y].isdigit():
            new_linked_list.insert_at_end(g(int(lnk[y])))
    new_linked_list.traverse_list()


sqr = lambda x: x * x
dbl = lambda y: 2 * y

lnk1 = 'link(1, link(2, link(3, link(4, empty))))'
sum_lnk(lnk1, sqr)
lnk2 = 'link(3, link(5, link(4, link(6, empty))))'
sum_lnk(lnk2, dbl)
