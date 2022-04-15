
income  = int(input("Enter income: "))
expense = int(input("Enter expense: "))
profit = income-expense
if profit>0:
    print("your company is operating at a profit")
    print(f"you have profitability: {profit/income*100:.2f} %")
    number_of_people = int(input("Enter number of peopele: "))
    print(f"The company's profit per employee {profit/number_of_people:.2f}")
elif profit<0:
    print("your company has no profit")