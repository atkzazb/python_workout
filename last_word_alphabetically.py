def last_word_alphabetically(f):
    text = open(f)
    out = ''

    for line in text:
        for word in line.split():
            if not word.isalpha():
                continue
            if word > out:
                out = word
    return out

new = open('text.txt', 'w')
new.writelines(['If only you could see that', 'If only you could', 'wannabe no', 'ye ye ye', 'like', 'apple'])
new.close()

name = 'text.txt'

print(last_word_alphabetically(name))