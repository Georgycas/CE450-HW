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
        l = ''
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                l = l + str(n.item)
                n = n.ref
        return l

    def chang(self, u, v):
        l = ''
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                if str(n.item) == u:
                    l = l + v
                else:
                    l = l + str(n.item)
                n = n.ref
            return l


def change(lnk, u, v):
    new_linked_list = LinkedList()
    for y in range(len(lnk)):
        if lnk[y].isdigit():
            new_linked_list.insert_at_end(int(lnk[y]))

    print(new_linked_list.traverse_list())
    return new_linked_list.chang(u, v)


l = 'link(1, link(2, link(3, empty)))'
n = change(l, '3', '1')
m = change(n, '1', '2')
change(m, '5', '1')
