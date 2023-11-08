def computepay(hours, rate):
    if hours>40:
        pay = (hours-40)*1.5*rate+40*rate
    else: 
        pay = rate*hours
    return pay

hours = int(input("Enter hours: "))
rate = float(input("Enter Rate: "))
print(f"Pay: {computepay(hours,rate)}")