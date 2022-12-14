class tree:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children


def has_itm(t, e):
    if t is None:
        return False
    if t.value == e:
        return True
    for child in t.children:
        if has_itm(child, e):
            return True
    return False


t = tree(11, [tree(12), tree(13, [tree(14), tree(15)])])
y = tree(11, [tree(12), tree(13, [tree(14), tree(15)])])

print(has_itm(t, 11))
print(has_itm(y, 16))
