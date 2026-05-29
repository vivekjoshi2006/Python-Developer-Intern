import random

print("\n" + "="*50)
print(f"{'PRODUCTION COUNTER SYSTEM':^50}")
print("="*50)

try:
    target_units = int(input("Enter total production target units        : "))
    workers_per_shift = int(input("Enter number of workers per shift          : "))
    defect_rate = float(input("Enter expected defect rate percentage (%)  : "))

    if target_units <= 0 or workers_per_shift <= 0 or defect_rate < 0 or defect_rate > 100:
        raise ValueError("\nInvalid input metrics. Please check values and ranges.")

    total_produced_items = 0
    total_defects = 0

    shift_production = {1: 0, 2: 0, 3: 0}
    shift_defects = {1: 0, 2: 0, 3: 0}
    target_achieved_early = False

    print("\n" + "-"*50)
    print(f"{'STARTING PRODUCTION SIMULATION':^50}")
    print("-"*50)

    for shift in range(1, 4):
        print(f"\n▶ [SHIFT {shift}] In Progress...")

        for cycle in range(1, 21):

            if random.uniform(0, 100) <= defect_rate:
                total_defects += 1
                shift_defects[shift] += 1
                continue 
            
            total_produced_items += 1
            shift_production[shift] += 1
            
            if total_produced_items >= target_units:
                target_achieved_early = True
                print(f"  └─ Target of {target_units} units reached at Cycle {cycle}!")
                break
                
        if target_achieved_early:
            break

    print("\n" + "="*50)
    print(f"{'PRODUCTION METRICS SUMMARY':^50}")
    print("="*50)
    print(f" Target Goal      : {target_units} units")
    print(f" Total Good Items : {total_produced_items} units")
    print(f" Total Defective  : {total_defects} units")
    print(f" Production Goal  : {'SUCCESS ✅' if total_produced_items >= target_units else 'INCOMPLETE ❌'}")
    print("-" * 50)
    
    print(f"{'\nPER-SHIFT PERFORMANCE REPORT':^50}")
    print("-" * 50)
    
    for shift in range(1, 4):
        good_items = shift_production[shift]
        defects = shift_defects[shift]
        
        productivity = good_items / workers_per_shift if workers_per_shift > 0 else 0
        
        print(f" [Shift {shift} Metrics]")
        print(f"   ├── Items Produced : {good_items}")
        print(f"   ├── Defective Items: {defects}")
        print(f"   └── Worker Productivity: {productivity:.2f} items/worker")
        print()

except ValueError as e:
    print(f"\n{'CONFIGURATION ERROR':^50}")
    if "\nInvalid input metrics" in str(e):
        print(f"\nError: {e}")
    else:
        print("\nError: Please provide clean numeric integer digits for your system inputs.")

print("="*50 + "\n")