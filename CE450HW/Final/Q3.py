def deep_rvrs(tup):
    return tuple(deep_rvrs(z) if isinstance(z, tuple) else z for z in reversed(tup))


a = (11, 12, 13, 14)
print(deep_rvrs(a))
tpl = (11, (12, (13, 113), 14), 15)
print(deep_rvrs(tpl))
