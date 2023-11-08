'''
Exercise 2: Write a program to prompt for a file name, and then read
through the file and look for lines of the form:
X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with “X-DSPAM-Confidence:”
pull apart the line to extract the floating-point number on the line.
Count these lines and then compute the total of the spam confidencevalues from these lines. When you reach the end of the file, print out
the average spam confidence.
Enter the file name: mbox.txt
Average spam confidence: 0.894128046745
Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519
Test your file on the mbox.txt and mbox-short.txt files
'''
count = 0
total_confidence = 0.0
try:
    with open("../mbox-short.txt","r") as fhand:
        for line in fhand:
            if line.startswith("X-DSPAM-Confidence:"):
                confidence_str = line.split(":")[1]
                confidence = float(confidence_str)
                count +=1
                total_confidence = confidence

    if count>0:
        average_confidence = total_confidence / count
        print(f"Average spam confidence: {average_confidence}")
    else:
        print("No lines starting with 'X-DSPAM-Confidence:' found in the line.")
except Exception as error:
    print(error)