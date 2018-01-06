

def avoids (word, forbiddenLetters):
    return not forbiddenLetters in word

print(avoids('see', 'e'))
print(avoids('awds', 'e'))


