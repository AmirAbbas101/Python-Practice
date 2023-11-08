'''
Exercise 2: Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average.
'''

total = 0
count = 0
numbers = []
while True:
    number = input("Enter a number: ")
    try:
        if number == "done":
            break
        else:
            number = int(number)
            numbers.append(number)
            total += number
            count +=1
    except:
        print("Invalid input")

print(f"{total} {count} {max(numbers)} {min(numbers)}")