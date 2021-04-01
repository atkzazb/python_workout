def pl_sentence():
    sent = input('Enter string: ')
    words = sent.split(' ')
    res = []
    for word in words:
        if word[0] in 'aeiou':
            res.append(word + 'way')
        else:
            res.append(word[1:] + word[0] + 'ay')
    return ' '.join(res)

print(pl_sentence())