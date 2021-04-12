def mysum_bigger_than(threshold, *args):
    if not args: return args
    total = 0
    for arg in args:
        if arg > threshold:
            total += arg
    return total

print(mysum_bigger_than(10, 5, 20, 30, 6))