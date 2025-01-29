# menu list
menu = ['Pancakes', 'Biscuits', 'Muffins', "Sandwich", 'Coffee']

# stock, has quantity for each menu items
stock = {'Pancakes': 10, 'Biscuits': 5, 'Muffins': 20,
         'Sandwich': 30, 'Coffee': 15}

# The cost price of my Products
price = {'Pancakes': 15, 'Biscuits': 14.50, 'Muffins': 10,
         'Sandwich': 30.00, 'Coffee': 12.00}

# The total cost of my stock in the cafe worth
total_inventory = 0.0

for items in menu:
    # calculation of cost multiplied by quantity
    quantity = stock[items]
    cost_price = price[items]
    # updating total stock with current item worth
    total_inventory = total_inventory + quantity * cost_price

print('Total inventory value for the cafe : R', total_inventory)