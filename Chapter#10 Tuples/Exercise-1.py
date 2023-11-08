'''
Exercise 1: Revise a previous program as follows: Read and parse the
“From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary. Then
sort the list in reverse order and print out the person who has the most
commits.
Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
'''

dic = {}
with open("../mbox-short.txt") as f:
    for line in f:
        if line.startswith("From"):
            words = line.split()
            senderEmail = words[1]
            dic[senderEmail] = dic.get(senderEmail, 0) + 1
    lst = sorted([(v,k) for (k,v) in dic.items()],reverse=True)
    for v, k in lst:
        print(f"{k} {v}")
        break
