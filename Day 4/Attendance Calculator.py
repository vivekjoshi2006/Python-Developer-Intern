print("\n" + "="*60)
print(f"{'INSTITUTIONAL COMPLIANCE ATTENDANCE CALCULATOR':^60}")
print("="*60)

try:
    classes_conducted = int(input("\nEnter total number of classes conducted  : "))
    classes_attended  = int(input("Enter number of classes attended total   : "))

    if classes_conducted <= 0 or classes_attended < 0:
        raise ValueError("Invalid parameters. Verify that tracking values sit in legal metrics.")
        
    if classes_attended > classes_conducted:
        raise ValueError("Attended count cannot exceed total conducted tracking metrics.")

    current_attendance_pct = (classes_attended / classes_conducted) * 100

    print("\n" + "-"*60)
    print(f"{'COMPLIANCE EVALUATION REPORT':^60}")
    print("-"*60)
    print(f" \nCurrent Attended Metrics  : {classes_attended}/{classes_conducted} Sessions")
    print(f" Logged Attendance Rate   : {current_attendance_pct:.2f} %")

except ValueError as e:
    print(f"\nTracking Exception: {e if 'Invalid' in str(e) or 'exceed' in str(e) else 'Integers only for class records.'}")


print("\n" + "="*60 + "\n")