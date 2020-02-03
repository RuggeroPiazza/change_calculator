"""
The program takes the amount to be paid and the money given by a customer,
calculates the change and returns it in form of coins/notes to be given back.
"""

money = {
         50: '50 pounds',
         20: '20 pounds',
         10: '10 pounds',
         5: '5 pounds',
         2: '2 pounds',
         1: '1 pound',
         0.50: '50 cents',
         0.20: '20 cents',
         0.10: '10 cents',
         0.05: '5 cents',
         0.02: '2 cents',
         0.01: '1 cents'}

result = []


def finding_coins(change):
    """recursive function;
       INPUT: float;
       OUTPUT: append to a list and calls the function again."""
    for value in money:
        if change < value:
            pass
        else:
            difference = round(change - value, 2)
            result.append(value)
            return finding_coins(difference)


def validate_input(user_input):
    """INPUT: string, user input;
       OUTPUT: float, user input;
       The function takes a user input string, validate it and
       return it as a float."""
    while True:
        try:
            amount = float(input(user_input))
            if amount <= 0:
                print("Invalid input: any of the amounts entered can't be zero or negative.")
                continue
        except ValueError:
            print("Invalid input: please make sure you are typing numbers.")
        else:
            return amount


if __name__ == "__main__":
    to_pay = validate_input("Please enter the amount to be paid: ")
    money_given = validate_input("Please enter the amount given: ")

    change = round(money_given - to_pay, 2)
    finding_coins(change)
    print(f"Change: {change} pounds")
    for item in result:
        print(f"{money[item]}")
