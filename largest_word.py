def large_word(stream):
    lines = stream.readlines()
    max_word = ''
    for line in lines:
        for word in line.split():
            if len(word) > len(max_word):
                max_word = word
    return max_word

f = open('new.txt', 'w')
f.write('How you like that\n')
f.write('You gonna like that\n')
f.write('Look at me, now look at you\n')
f.close()

y = open('new.txt')
print(large_word(y))