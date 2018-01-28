import string
import random

def process_file(fileName):
    hist = dict()
    fp = open(fileName)
    for line in fp:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

hist = process_file('emma.txt')

def total_words(hist):
    return sum(hist.values())

def different_words(hist):
    return len(hist)

print('Total number of words:', total_words(hist))
print('Number of different words:', different_words(hist))

def most_common(hist):
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort(reverse=True)
    return t

t = most_common(hist)
print('The most common words are:')
for freq, word in t[:20]:
    print(word, freq, sep='\t')

# def subtract(d1, d2):
#    res = dict()
#    for key in d1:
#        if key not in d2:
#            res[key] = None
#    return res

#words = process_file('words.txt')
#diff = subtract(hist, words)

#print('Words in the book that are not in the word list:')
#for word in diff:
#    print(word, end=' ')

def random_word(h):
    t = []
    for word, freq in h.items():
        t.extend([word] * freq)

    return random.choice(t)

print('random word: ', random_word(hist))

