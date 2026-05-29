print(f"{'\nSMART BILL SPLITTER\n':^40}")

total_bill = float(input("Enter total bill amount                     : "))
number_of_people = int(input("Enter number of people splitting the bill   : "))
tip_percentage = float(input("Enter tip percentage                        : "))

tip_amount = total_bill * (tip_percentage / 100.0)
grand_total = total_bill + tip_amount
share_per_person = grand_total / number_of_people
leftover_pennies = grand_total % number_of_people
adjusted_total_before_remainder = grand_total - leftover_pennies
final_share = round(share_per_person, 2)

print("\n" + "="*60)
print(f"{'\n          BILL SPLIT SUMMARY\n'}")
print(f" Original Bill                  : Rs{total_bill:,.2f}")
print(f" Tip Amount ({tip_percentage}%)             : Rs{tip_amount:,.2f}")
print(f" Grand Total                    : Rs{grand_total:,.2f}")
print(f" Number of People               : {number_of_people}")
print(f" Amount Per Person              : Rs{final_share:,.2f}\n")
print("="*60, "\n")