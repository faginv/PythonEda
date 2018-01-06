def is_abecedarian(word):
    
    abe = False
    
    length = len(word)
    index = 0

    while index < length:
        if index + 1 < length:
            if word[index] < word[index + 1]:
                abe = True
            else:
                abe = False
        index += 1
    return abe


print(is_abecedarian('abce'))
print(is_abecedarian('aabbcde'))
print(is_abecedarian('defghha'))
