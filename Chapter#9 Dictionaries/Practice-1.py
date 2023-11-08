import string
d = {}
with open("../mbox-short.txt","r") as fhand:
    for line in fhand:
        line = line.rstrip()
        line = line.translate(line.maketrans("","",string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words:
            d[word]  = d.get(word, 0)+1
print(d)