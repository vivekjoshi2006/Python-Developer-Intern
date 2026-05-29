print("\nYour Personal Profile Card\n")
print("Give me your name, age, city & fav sub seprated by space\n")

name, age_str, city, subject = input("Enter details: ").split()
age = int(age_str)
birth_year = 2024 - age

print("\n" + "="*40)
print(f"{'PERSONAL PROFILE CARD':^40}")
print("="*40)
print(f" Name          : {name}")
print(f" Age           : {age} years old")
print(f" Birth Year    : {birth_year}")
print(f" City          : {city}")
print(f" Fav Subject   : {subject}")
print("="*40, "\n")