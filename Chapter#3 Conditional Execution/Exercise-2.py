'''
Exercise 2: Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the
program:
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input
'''

try:
    hours = int(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except:
    print("Erorr, Please enter numeric input")

pay = 0.0
if hours>40:
    pay = ((hours-40)*1.5*rate)+40*rate
else: 
    pay = rate*hours
print(f"Pay: {pay}")