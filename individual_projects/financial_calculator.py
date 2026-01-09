# GNB - 1st - Financial Calculator

choice = int(input("Welcome to the best financial calculator in the world, User. Choose which type of calculator you'd like to use(Type in the number - e.g. 5): \n1. Savings Time Calculator\n2. Compound Interest Calculator \n3. Budget Allocator \n4. Sale Price Calculator \n5. Tip Calculator\n"))

if choice == 1:
    def saving_time():
        help

elif choice == 2:
    def compound_interest():
        help
elif choice == 3:
    def budgeting():
        help
elif choice == 4:
    def sale_price():
        help
elif choice == 5:
    def tipping(item_cost):
        item_cost = float(input("What is the total cost of the item(s)? (Only add the number without a dollar sign - e.g. 75.32): "))
else:
    print("Not an option, User")