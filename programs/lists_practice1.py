#Allison Gentry
#Lists Practice with your mom's spaghetti

#A variable that holds more than one value is a list
groceries = ['Bread', 'Milk', 'Eggs']
#You can get items fom a list by their index
print(groceries[0])

#Start an empty list
cart = []

#For every item in my grocery list:
#Add that item to the cart
for item in groceries:
    cart.append(item)
print(cart)