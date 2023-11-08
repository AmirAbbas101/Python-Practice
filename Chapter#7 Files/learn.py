fhand = open("../mbox-short.txt")
for line in fhand:
    print(line.isupper())
print(dir(str))