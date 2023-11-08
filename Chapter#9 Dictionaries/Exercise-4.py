'''
Exercise 4: Add code to the above program to figure out who has the
most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to find who has
the most messages and print how many messages the person has.
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
'''

histoGram = {}
lst = list()
maximum = None
try:
    with open("../mbox-short.txt","r") as fhand:
        for line in fhand:
            if line.startswith("From"):
                email = line.split()[1]
                histoGram[email] = histoGram.get(email, 0)+1
        for k in histoGram: # k is key for itrator
            if maximum is None or histoGram[k]>histoGram[maximum]:
                maximum = k
        print(f"{maximum}, {histoGram[maximum]}")
except Exception as error:
    print(error)