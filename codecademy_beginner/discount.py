"""
8. Give me the discount

Create a function in Python that accepts two parameters.
The first should be the full price of an item as an integer.
The second should be the discount percentage as an integer.

The function should return the price of the item after the discount has been applied.
For example, if the price is 100 and the discount is 20, the function should return 80.
"""

def disc(price, discount):
    perc = (100-discount)/100
    price = price*perc
    return price


print(disc(1000, 30))
