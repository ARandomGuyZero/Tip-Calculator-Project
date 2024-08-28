"""
Tip Calculator Project

Author: Alan
Date: August 20th 2024

This script calculates the amount each person needs to pay when splitting a bill,
including the tip. The user is prompted to enter the total bill amount,
the desired tip percentage, and the number of people sharing the bill.
The script then calculates and outputs the amount each person should pay.
"""

# Welcome message
print("Welcome to the tip calculator!")

# Get the user's bill
bill = float(input("What was the total bill? $"))

# Get the user's desired tip percentage
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Get the number of people to split the bill
people = int(input("How many people to split the bill? "))

# Calculate the tip amount as a percentage of the bill
tip_as_percent = tip / 100

# Calculate the total amount of the tip
tip_amount = bill * tip_as_percent

# Calculate the total bill including the tip
bill_total = bill + tip_amount

# Calculate the amount each person should pay
bill_per_person = bill_total / people

# Round the final amount to 2 decimal places for currency format
final_amount = round(bill_per_person, 2)

# Print the final amount each person should pay
print(f"Everyone should pay: ${final_amount}")