list = ['Pizza', 'Burgers', 'Chips']

print("Here are the items in the food list:")
print(list)
print()

change = input("Which item should I change? ")
new = input("Enter the new value: ")
print()

if change in list:
    i = list.index(change)
    list.remove(change)
    list.insert(i, new)

print("Here is the revised list: ")
print(list)
