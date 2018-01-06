fin = open('words.txt')

forbiddenLetters = input('Enter a string of forbidden letters')

for line in fin:
    word = line.strip()
    
    if(not forbiddenLetters in word):
        print(word)
    

 


