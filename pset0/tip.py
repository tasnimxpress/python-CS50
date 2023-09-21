def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


# remove the leading $, and return the amount as a float.
def dollars_to_float(d):
    amount = d.replace('$', '')
    return float(amount)

# remove the trailing %, and return the percentage as a float
def percent_to_float(p):
    percentage = p.replace('%', "")
    return float(percentage)/100

main()