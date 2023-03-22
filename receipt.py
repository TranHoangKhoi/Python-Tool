import datetime
# Define the receipt items and their prices
items = [("Item 1", 10), ("Item 2", 20), ("Item 3", 30)]

# Calculate the total price
total = sum([item[1] for item in items])

# Get the current date and time
date = datetime.datetime.now().strftime("%m/%d/%Y %I:%M %p")

# Print the receipt
print("==============================")
print("       AME Digital Store       ")
print("==============================")
print("Date: " + date)
print("==============================")
for item in items:
    print("{:<10} {:>10}".format(item[0], item[1]))
print("==============================")
print("{:<10} {:>10}".format("Total", total))
print("==============================")
