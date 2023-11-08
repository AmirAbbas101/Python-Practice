import re
count = {}
with open("../mbox-short.txt") as fhand:
    fhand = fhand.read()
    emils = re.findall(r"\S+@\S+",fhand)
    for email in emils:
        count[email] = count.get(email,0)+1
    for k,v in count.items():
        print(f"{k}  {v}")