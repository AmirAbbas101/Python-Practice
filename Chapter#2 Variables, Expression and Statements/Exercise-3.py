'''
Exercise 3: Write a program to prompt the user for hours and rate per
hour to compute gross pay.
Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25

We won’t worry about making sure our pay has exactly two digits after the decimal
place for now. If you want, you can play with the built-in Python round function
to properly round the resulting pay to two decimal places.
'''

hours = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
pay = hours * rate
print(f"Pay: {round(pay,2)}")
print(pay)
