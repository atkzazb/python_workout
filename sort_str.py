def strsort(s):
    return ''.join(sorted(s))

print(strsort('cba'))

def lstsort(s):
    words = s.split(' ')
    words = sorted(words)
    return ' '.join(words)

print(lstsort('Tom Dick Harry'))