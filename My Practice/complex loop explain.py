##how many cookies they want to buy?
## For 6 or less they receive no discount
## For 7 - 12 they receive a 5% discount
## For 13 - 24 they receive a 10% discount.
## For amounts over 25 they receive a 20% discount
## needs to allow the user to keep entering cookie
## All cookies are $.50 each.
## determine a subtotal before the discount,
## the discount and the total for each batch of cookies purchased.


rate = float()
discount = float()
subtotal = float()
total = float()
answer = str()
while answer != 'quit':
     num_cookies = int(input("Enter the number of cookies:  "))
     if num_cookies <= 6:
          rate = 0.0
     elif num_cookies <= 12:
          rate = 0.5
     elif num_cookies <= 24:
          rate = 0.1
     else:
          rate = 0.2
     #determining the subtotal
     subtotal = num_cookies * 0.5
     #determining the discount
     discount = subtotal * rate
     #determining the total
     total = subtotal - discount
     #print out subtotal, discount and total
     print("Subtotal:  $", subtotal)
     print("Discount:  $", discount)
     print("Total:  $", total)
     #ask the user if they want to enter another batch
     answer = input("Enter 'quit' to end the program:  ")
