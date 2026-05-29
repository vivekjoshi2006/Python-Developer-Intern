print("\n" + "*"*40)
print(f"{'SMART TEMPERATURE ADVISOR':^40}")

try:
    temperature = float(input("\nEnter temperature (°C): "))

    print("\n" + "*"*40)
    print(f"{'WEATHER ADVICE\n':^40}")

    if temperature < 0:
        print("Advice   : 'Freezing! Stay indoors and wear heavy clothing.'")
        
    elif 0 <= temperature <= 15:
        print("Advice   : 'Cold. A jacket is recommended'")
        
    elif 16 <= temperature <= 25:
        print("Advice   : 'Pleasant weather! Great for outdoor activities.'")
        
    elif 26 <= temperature <= 35:
        print("Advice   : 'Hot. Stay hydrated and use sunscreen.'")
        
    else:  
        print("Advice   : 'Extreme heat! Avoid going outside.'")

except ValueError:
    print("Error    : Please enter a valid decimal or integer value.")

print("\n" + "*"*40 + "\n")