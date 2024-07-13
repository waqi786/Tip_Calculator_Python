print("Welcome to the tip calculator.")
a = float(input("What was the total bill? $"))
b = int(input("What percentae tip would you like to give? 10, 12, or 15?"))
c = int(input("How many people to split the bill? "))
d = a/c
e = a*b/100+a
f = round(e,2)
print(f"Each person should pay:, ${f}")