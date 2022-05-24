def get_inputs():

    print("Welcome to the tip calculator.")
    _bill_amount = float(input("What was the total bill? $"))
    _tip_percentage = (
        float(input("What percentage tip would you like to give? 10, 12, or 15? "))
        / 100
    )
    _num_people = int(input("How many people to split the bill? "))

    return _bill_amount, _tip_percentage, _num_people


def tip_calculate(bill, percentage, num):
    """
    the total money incuding tips  each person should pay
    """
    return bill / num * (1 + percentage)


if __name__ == "__main__":

    bill_amount, tip_percentage, num_people = get_inputs()

    tip = tip_calculate(bill_amount, tip_percentage, num_people)

    print(f"Each person should pay:${round(tip,2)}")
