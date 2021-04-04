def longest_word(f):
    text = open(f)
    out = ''

    for line in text.readlines():
        for word in line.split():
            if not word.isalpha():
                continue
            if len(word) > len(out):
                out = word
    return out
            