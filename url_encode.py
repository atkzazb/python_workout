import string

def url_encode(s):
    other = string.ascii_letters + string.digits
    out = []

    for c in s:
        if c in other:
            out.append(c)
        else:
            out.append(hex(ord(c)).replace('0x', '%'))
    return ''.join(out)

print(url_encode('hel fdg '))