'''
Exercise 3: Sometimes when programmers get bored or want to have a
bit of fun, they add a harmless Easter Egg to their program. Modify
the program that prompts the user for the file name so that it prints a
funny message when the user types in the exact file name “na na boo
boo”. The program should behave normally for all other files which
exist and don’t exist. Here is a sample execution of the program:
python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt
python egg.py
Enter the file name: missing.tyxt
File cannot be opened: missing.tyxt
python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!
We are not encouraging you to put Easter Eggs in your programs; this
is just an exercise.
'''
fileName = input("Enter file name: ")
fileName = "../"+fileName
if fileName == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    count = 0
    try:
        with open(fileName,"r") as fhand:
            for line in fhand:
                count += 1
        if count > 0:
            print(f"There were {count} subject lines in {fileName[3:]}")
    except:
        print(f"File cannot be opened: {fileName[3:]}")
    