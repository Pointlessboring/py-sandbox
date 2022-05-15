###############################
# PB: 22/05/15 
#
# I really like this program: simple, powerful

def middle(n):  
    return n[1]  

lines = ""
try:
    with open('alice.txt', encoding='utf-8') as f:
        lines = f.read()
except FileNotFoundError:
    print("File Alice.txt is missing")
    exit()

words = lines.split()
unique_words = sorted(set(words))
word_counts = []
for word in unique_words:
    occurances = 0
    while word in words:
        occurances += 1
        words.remove(word)
    entry = (word, occurances)
    word_counts.append(entry)
print(sorted(word_counts, reverse = False, key=middle))


