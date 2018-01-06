def uses_only(word, letters):
    only = False

    for w in word:
        if(w in letters):
            only = True
        else:
            only = False
    return only

print(uses_only('asdfg', 'gfdsa'))
print(uses_only('asdfg fghk', 'gfdsa'))
