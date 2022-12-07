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
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            print("<", end=" ")
            while n is not None:
                print(n.item, end=" ")
                n = n.ref
            print(">")


def prnt_lnk(s):
    new_linked_list = LinkedList()
    for y in range(len(s)):
        if s[y].isdigit():
            new_linked_list.insert_at_end(int(s[y]))
    new_linked_list.traverse_list()


prnt_lnk('link(1, link(2, link(3, link(4, empty))))')
