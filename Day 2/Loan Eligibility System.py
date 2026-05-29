print("\n" + "*"*40)
print(f"{'LOAN ELIGIBILITY SYSTEM':^40}")

try:
    salary = int(input("\nEnter your salary = Rs "))
    age = int(input("Your age          = "))

    print("\nEmployment types: 'S' for Salaried, 'SE' for Self-employed")
    employment_status = input("\nEnter your employment status: ").strip().upper()

    if employment_status not in ['S', 'SE']:
        raise ValueError("\nInvalid employment code entered.")

    employment = "salaried" if employment_status == "S" else "self-employed"

    print("\n" + "-"*40)
    print(f"{'EVALUATION REPORT\n':^40}")

    if not (21 <= age <= 60):
        print(f"Status   : Rejected")
        print(f"Reason   : Age must be between 21 and 60")

    elif salary <= 25000:
        print(f"Status   : Rejected")
        print(f"Reason   : Salary must be at least ₹25,000")

    else:
        if 21 <= age <= 30 and salary <= 30000:
            print("Status   : Conditional Approval")
            print("Message  : 'Needs guarantor' (Age between 21–30 with salary under ₹30,000)")
            
        elif age >= 55 and employment == "self-employed":
            print("Status   : High Risk Review")
            print("Message  : 'High risk, senior review needed.'")
            
        else:
            print("Status   : Approved")
            print("Message  : All eligibility criteria successfully met.")


except ValueError as e:
    if "Invalid employment code" in str(e):
        print("\nError: Please use exactly 'S' or 'SE' for employment status.")
    else:
        print("\nError: Please enter numerical digits only.")

print("\n" + "*"*40 + "\n")