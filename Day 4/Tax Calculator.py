def compute_progressive_tax(income):
    tax_liability = 0.0
    tax_breakdown = []

    # Up to Rs 3,000,000 (0% Tax)

    if income <= 300000:
        tax_breakdown.append(("Up to Rs 3L @ 0%", 0.0))
        return tax_liability, tax_breakdown
    else:
        tax_breakdown.append(("Up to Rs 3L @ 0%", 0.0))


    # Rs 300,001 to Rs 6,000,000 (5% Tax)

    if income <= 600000:
        taxable_in_slab = income - 300000
        slab_tax = taxable_in_slab * 0.05
        tax_liability += slab_tax
        tax_breakdown.append(("Rs 3L - Rs 6L @ 5%", slab_tax))
        return tax_liability, tax_breakdown
    else:
        slab_tax = 300000 * 0.05
        tax_liability += slab_tax
        tax_breakdown.append(("Rs 3L - Rs 6L @ 5%", slab_tax))


    # Rs 600,001 to Rs 9,000,000 (10% Tax)

    if income <= 900000:
        taxable_in_slab = income - 600000
        slab_tax = taxable_in_slab * 0.10
        tax_liability += slab_tax
        tax_breakdown.append(("Rs 6L - Rs 9L @ 10%", slab_tax))
        return tax_liability, tax_breakdown
    else:
        slab_tax = 300000 * 0.10
        tax_liability += slab_tax
        tax_breakdown.append(("Rs 6L - Rs 9L @ 10%", slab_tax))


    # Above Rs 9,000,000 (20% Tax)

    taxable_in_slab = income - 900000
    slab_tax = taxable_in_slab * 0.20
    tax_liability += slab_tax
    tax_breakdown.append(("Above Rs 9L @ 20%", slab_tax))

    return tax_liability, tax_breakdown


print("\n" + "="*60)
print(f"{'PROGRESSIVE INCOME TAX CALCULATOR':^60}")
print("="*60 + "\n")

try:
    gross_annual_income = float(input("Enter your total gross annual income (Rs) : "))
    if gross_annual_income < 0:
        raise ValueError("\nAnnual financial income metrics cannot register as negative pools.")

    total_tax, slab_breakdown = compute_progressive_tax(gross_annual_income)
    effective_rate = (total_tax / gross_annual_income) * 100 if gross_annual_income > 0 else 0

    print("\n" + "-"*60)
    print(f"{'TAX LIABILITY STATEMENT BREAKDOWN':^60}")
    print("-"*60)
    print(f"\nGross Evaluated Income      : Rs {gross_annual_income:,.2f}")
    
    for label, amount in slab_breakdown:
        print(f"{label:<25}   : Rs {amount:,.2f}")
        
    print(f"\nNet Tax Payable Burden      : Rs {total_tax:,.2f}")
    print(f"Effective Average Tax Rate  : {effective_rate:.2f}%")
   
except ValueError as e:
    print(f"\nConfiguration Error: {e if 'negative' in str(e) else 'Please verify numerical payroll metrics.'}")

print("\n" + "="*60 + "\n")