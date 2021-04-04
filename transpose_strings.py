def transpose(L):
    splitted = [s.split(' ') for s in L]
    zipped = zip(*splitted)
    out = [' '.join(a) for a in zipped]
    return out

L = ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']
print(transpose(L))