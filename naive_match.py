def naive_matching(p, t):
    occurences = []
    characters = 0
    alignments = 0
    for i in range(len(t) - len(p) + 1):
        alignments += 1
        match = True
        for j in range(len(p)):
            characters += 1
            if t[i + j] != p[j]:
                match = False
                break
            if match:
                occurences.append(i)
    return occurences, characters, alignments


o, c, a = naive_matching(P, T)
print('Number of occurences = %d' % len(o))
print('Number of characters compared = %d' % c)
print('Number of alignments compared = %d' % a)
