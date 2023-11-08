'''
Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the
converted temperature.
'''

celsTemp = float(input("Eter temperatrue in Celsius : "))
fahrnTemps = (celsTemp * 9/5) +32
print(f"Temperature in Fahrenheit : {fahrnTemps}")