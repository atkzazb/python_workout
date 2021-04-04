import string

def ubbi_dubbi(s):
    out = []
    for c in s[1:]:
        if c in 'aeoui':
            out.append('ub'+c)
        else:
            out.append(c)

    if s[0] in string.ascii_uppercase:
        out[0] = out[0].capitalize()

    return ''.join(out)
    
print(ubbi_dubbi('Milk'))