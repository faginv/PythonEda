def uses_all(word, letters):
    
    uall = False

    for w in word:
        if(w in letters):
            uall = True

    return uall


print(uses_all('asdfg', 'ag'))
print(uses_all('asdfg', 'qa'))
print(uses_all('asdfg', 'qw'))
