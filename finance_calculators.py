import math

# Prompt user to select between 'investment' or 'bond'
str_selection = input("Choose either 'investment' or 'bond' from the menu below to proceed:\
    \n\ninvestment - to calculate the amount of interest you'll earn on your investment\
    \nbond       - to calculate the amount you'll have to pay on a home loan\
    \n\nEnter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# If user selects investment
if str_selection == "investment":
    # Get inputs for investment calculation
    float_investment_amount = float(input("Enter the amount of money you are depositing: "))
    float_interest_rate = float(input("Enter the interest rate (as a percentage without the sign): "))
    float_years = float(input("Enter the number of years you plan on investing for: "))
    interest = input("Enter the type of interest (simple or compound): ").lower()

    # Calculate simple or compound interest based on user input
    if interest == "simple":
        float_simple_interest = float_investment_amount * (1 + (float_interest_rate / 100) * float_years)
        print(f"\nAfter {float_years} years, you will have R{float_simple_interest:.2f}")
    elif interest == "compound":
        float_compound_interest = float_investment_amount * math.pow((1 + float_interest_rate / 100), float_years)
        print(f"\nAfter {float_years} years, you will have R{float_compound_interest:.2f}")
    else:
        print("Invalid interest type. Please enter either 'simple' or 'compound'.")

# If user selects bond
elif str_selection == "bond":
    # Get inputs for bond repayment calculation
    float_present_value = float(input("Enter the present value of the house: "))
    float_interest_rate = float(input("Enter the interest rate (as a percentage without the sign): "))
    float_months = float(input("Enter the number of months you plan to take to repay the bond: "))

    # Calculate monthly bond repayment
    monthly_interest_rate = (float_interest_rate / 100) / 12
    monthly_repayment = (monthly_interest_rate * float_present_value) / (1 - math.pow(1 + monthly_interest_rate, -float_months))
    
    print(f"\nYour monthly repayment will be R{monthly_repayment:.2f}")

# If user enters an invalid selection
else:
    print("Invalid selection. Please enter either 'investment' or 'bond'.")
