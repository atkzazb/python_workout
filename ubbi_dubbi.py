def ubbi_dubbi(s):
    out = []
    for c in s:
        if c in 'aeoui':
            out.append('ub'+c)
        else:
            out.append(c)
    return ''.join(out)

print(ubbi_dubbi('milk'))