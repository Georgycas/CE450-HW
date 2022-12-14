class tree:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children
        self.num_nodes = 1
        for child in children:
            self.num_nodes += child.num_nodes


def calc_avg(t):
    if t is None:
        return 0
    total_value = t.value
    total_nodes = 1
    for child in t.children:
        child_avg = calc_avg(child)
        total_value += child_avg * child.num_nodes
        total_nodes += child.num_nodes
    return total_value / total_nodes


print(calc_avg(tree(11, [tree(12), tree(13, [tree(14), tree(15)])])))
