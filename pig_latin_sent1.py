def pl_sentence1(f):
    out = []

    for n, line in enumerate(f.readlines()):
        words = line.split()

        if not words: #if the line is empty, skip and continue
            continue

        if n >= 10: #if n exceeded 10 lines, that's enough, break
            break

        if n >= len(words):
            out.append(words[-1])
        else:
            out.append(words[n])

    return ' '.join(out)

f = open('text.txt')
print(pl_sentence1(f))