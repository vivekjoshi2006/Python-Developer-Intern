print("\n" + "="*50)
print(f"{'NUMBER PATTERN GENERATOR':^50}")
print("="*50)

try:
    n = int(input("\nEnter a positive integer (n) for the patterns: "))
    if n <= 0:
        raise ValueError("\nInput must be a positive integer greater than 0.\n")

    # -------------------------------------------------------
    # Right Triangle of Stars (using nested loops and range)
    # -------------------------------------------------------

    print("\nRight Triangle of Stars:")
    print("-" * 30 + "\n")
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()


    # --------------------------------------------------------------
    # Inverted Triangle of Numbers (using nested for with step -1)
    # --------------------------------------------------------------

    print("\nInverted Triangle of Numbers:")
    print("-" * 30 + "\n")
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


    # ------------------------------------------------------------------
    # Pascal's Triangle First n Rows (using nested loops + accumulator)
    # ------------------------------------------------------------------

    print("\nPascal's Triangle (First N Rows):")
    print("-" * 30 + "\n")
    for i in range(n):
        current_val = 1
        print(" " * (n - i - 1), end="")
        
        for j in range(0, i + 1):
            print(current_val, end=" ")
            current_val = current_val * (i - j) // (j + 1)
        print()


    # -----------------------------------------------------------
    # Prime Numbers Up to n (using the strict for-else pattern)
    # -----------------------------------------------------------

    print("\nPrime Numbers Up to N:")
    print("-" * 30 + "\n")
    prime_list = []
    
    for num in range(2, n + 1):
        for factor in range(2, int(num**0.5) + 1):
            if num % factor == 0:
                break
        else:
            prime_list.append(num)
            
    if prime_list:
        print(f"Primes found: {', '.join(map(str, prime_list))}")
    else:
        print("No prime numbers found in this range.")

except ValueError as e:
    print(f"{'\nINPUT ERROR':^50}")
    if "greater than 0" in str(e):
        print(f"\nError: {e}")
    else:
        print("\nError: Please enter clear numeric whole numbers only.")

print("\n" + "="*50 + "\n")