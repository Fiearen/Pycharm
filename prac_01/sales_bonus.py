"""

Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


bonus = 0
while True:
    sales = float(input("Enter sales: $"))
    if sales < 0:
        break
    elif sales < 1000:
        bonus = (sales/100)*10
    else:
        bonus = (sales/100)*15
    print(bonus)