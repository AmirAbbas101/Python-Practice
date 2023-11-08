'''
Exercise 3: Write a program that reads a file and prints the letters
in decreasing order of frequency. Your program should convert all the
input to lower case and only count the letters a-z. Your program should
not count spaces, digits, punctuation, or anything other than the letters
a-z. Find text samples from several different languages and see how
letter frequency varies between languages. Compare your results with
the tables at https://wikipedia.org/wiki/Letter_frequencies.
'''
frequency = dict()
with open("../mbox-short.txt") as fhand:
    fhand = fhand.read().lower()
    for line in fhand:
        line = line.rstrip()
        words = line.split()
        for wrod in words:
            word = str(wrod)
            for c in word:
                if c.isalpha():
                    frequency[c]  = frequency.get(c,0)+1
    frequencylst = list()
    frequencylst = sorted([(k,v) for (k,v) in frequency.items()], reverse=False)
    frequency = dict(frequencylst)
    for k,v in frequency.items():
        print(f"{k} {v}")
