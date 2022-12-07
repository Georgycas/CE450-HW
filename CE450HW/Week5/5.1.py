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

    def search_item(self, x):
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Item found")
                return True
            n = n.ref
        print("item not found")
        return False


def cntn_link(s, elm):
    new_linked_list = LinkedList()
    for y in range(len(s)):
        if s[y].isdigit():
            new_linked_list.insert_at_end(int(s[y]))
    new_linked_list.search_item(elm)


cntn_link('link(1, link(2, link(3, empty)))', 1)
cntn_link('link(1, link(2, link(3, empty)))', 4)
