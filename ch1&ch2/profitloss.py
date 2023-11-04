''' If cost price and selling price of an item is input through the keyboard, write a program to determine whether the seller has made profit or incurred loss or no profit no loss. Also determine how much profit he made or loss he incurred. '''

cost_price = int(input("Enter the cost price:"))
selling_price = int(input("Enter the selling price:"))

# if sp is more than cp -> profit
if selling_price > cost_price:
    profit = selling_price - cost_price
    print("We have made profit of", profit)
# if sp is less than cp -> loss
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("We have incurred loss of:", loss)
# if sp is equal to cp -> no profit no loss
else:
    print("We have made no profit no loss")
