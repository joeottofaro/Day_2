# Tip Calculator
print("Welcome to the tip calculator!")
# Store Bill,Tip and amount of people as vars
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# Math to get the amount each person ows to 2 decimal points
total_each_person = round((tip / 100 * bill + bill) / people, 2)

print(f"Each person should pay: ${total_each_person}")
