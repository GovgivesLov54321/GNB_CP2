# GNB - 1st - Financial Calculator

choice = input("Welcome to the best financial calculator in the world, User. Choose which type of calculator you'd like to use(Type in the number - e.g. 5): \n1. Savings Time Calculator\n2. Compound Interest Calculator \n3. Budget Allocator \n4. Sales Price Calculator \n5. Tip Calculator\n")
def saving_time():
    savings_goal = float(input("What amount are you saving to: "))
    
    frequency_choice = input("How often are you contributing?: \n1. Weekly\n2. Monthly\nEnter 1 or 2: ").strip()
    contribution_amount = float(input("How much are you contributing each time: "))

    if contribution_amount <= 0:
        print("Contribution amount must be greater than 0.")
        return

    if frequency_choice == "1":
        weeks_needed = savings_goal / contribution_amount
        weeks_needed_rounded = int(weeks_needed) if weeks_needed.is_integer() else int(weeks_needed) + 1

        months_needed = round(weeks_needed_rounded / 4, 1)
        print(f"\nIt will take approximately {months_needed} months to save ${savings_goal:.2f}")

    elif frequency_choice == "2":
        months_needed = savings_goal / contribution_amount
        months_needed_rounded = round(months_needed, 0) 

        print(f"\nIt will take {months_needed_rounded} months to save ${savings_goal:.2f}")

    else:
        print("Invalid choice. Please select 1 or 2.")

def compound_interest():
    starting_amount = float(input("What is the beginning amount of money? (Only add the number without a dollar sign - e.g. 75.32): "))
    interest_rate = float(input("What is the yearly interest rate?: "))
    compounding_time = int(input("How many years is the money going to compound for?: "))

    compounded_equation = starting_amount * (1 + (interest_rate / 100)) ** compounding_time
    compounded_equation_rounded = round(compounded_equation, 2)

    print(f"At the end of {compounding_time} years, your ${starting_amount} will become ${compounded_equation_rounded}.")
def budgeting():
    def calculate_amount(income, percent):
        return (income * percent) / 100

    categories = []
    percentages = []

    num_categories = int(input("How many budget categories do you have: "))

    for i in range(num_categories):
        category_name = input(f"\nCategory {i + 1}: ")
        categories.append(category_name)

    monthly_income = float(input("\nWhat is your monthly income: "))

    for category in categories:
        percent = float(input(f"\nWhat percent is your {category}: "))
        percentages.append(percent)

    print()

    for i in range(num_categories):
        allocated_amount = calculate_amount(monthly_income, percentages[i])
        allocated_amount_rounded = round(allocated_amount, 2)

        if categories[i].lower() == "groceries":
            print(f"{categories[i]} are ${allocated_amount_rounded}")
        else:
            print(f"{categories[i]} is ${allocated_amount_rounded}")

def sale_price():
        item_cost = float(input("What's the original cost of the item? (Only add the number without a dollar sign - e.g. 75.32): "))
        discount_percentage = float(input("What's the percentage of the discount?: "))

        discount_amount = item_cost * (discount_percentage / 100)
        discount_amount_rounded = round(discount_amount, 2)

        new_item_cost = item_cost - discount_amount_rounded
        print(f"The discounted cost for the item is ${new_item_cost}.")
def tipping():
        item_cost = float(input("What is the bill? (Only add the number without a dollar sign - e.g. 75.32): "))
        tip_percentage = float(input("What is the percentage of a tip that you're giving?: "))
        
        tip_cost = item_cost * (tip_percentage / 100)
        tip_cost_rounded = round(tip_cost, 2)

        total_cost =  tip_cost_rounded + item_cost
        print(f"The tip amount is ${tip_cost_rounded}, so the total cost for the bill and tip is ${total_cost}.")

if choice == "1":
    saving_time()
elif choice == "2":
    compound_interest()
elif choice == "3":
    budgeting()
elif choice == "4":
    sale_price()
elif choice == "5":
    tipping()
else:
    print("Not an option, User.")