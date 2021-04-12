def mysum(*args):
    if not args:
        return args
    total = args[0]
    for arg in args[1:]:
        total += arg
    return total

print(mysum('abc', 'def'))