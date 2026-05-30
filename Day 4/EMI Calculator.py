import math

print("\n" + "="*60)
print(f"{'FINANCIAL EMI CALCULATOR MODULE':^60}")
print("="*60)

try:
    principal = float(input("\nEnter principal loan amount (Rs)       : "))
    annual_rate = float(input("Enter annual interest rate (%)         : "))
    tenure_years = float(input("Enter loan tenure (in years)           : "))

    if principal <= 0 or annual_rate <= 0 or tenure_years <= 0:
        raise ValueError("\nLoan parameters must be positive numbers greater than zero.")

    total_months = int(tenure_years * 12)
    monthly_rate = (annual_rate / 12) / 100

    # Formula: E = [P * r * (1+r)^n] / [(1+r)^n - 1]

    compounding_factor = math.pow(1 + monthly_rate, total_months)
    monthly_emi = (principal * monthly_rate * compounding_factor) / (compounding_factor - 1)
    
    total_repayment = monthly_emi * total_months
    total_interest_payable = total_repayment - principal

    print("\n" + "-"*60)
    print(f"{'LOAN AMORTIZATION SUMMARY REPORT':^60}")
    print("-"*60)

    print(f"\nTotal Tenure Period          : {total_months} Months ({tenure_years} Years)")
    print(f" Equated Monthly Installment : Rs {monthly_emi:,.2f}")
    print(f" Principal Component Amount  : Rs {principal:,.2f}")
    print(f" Total Interest Component    : Rs {total_interest_payable:,.2f}")
    print(f" Total Cumulative Outflow    : Rs {total_repayment:,.2f}")

except ValueError as e:
    print(f"{'\nFINANCIAL METRIC CONFIGURATION ERROR':^60}")

    if "positive numbers" in str(e):
        print(f" Error : {e}")
    else:
        print("\nError  : Please provide valid decimal digits for financial fields.")

print("\n" + "="*60 + "\n")