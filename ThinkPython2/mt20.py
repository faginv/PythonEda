fin = open('words.txt')


total_line = 0
no_e = 0
for line in fin:
    word = line.strip()
    
    total_line += 1

    if(not 'e' in word):
        no_e += 1

print(no_e / total_line * 100)

 


