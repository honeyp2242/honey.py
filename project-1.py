print ("Welcome to the Interactive date collector")

name = (input("Enter your name: "))
age = (input("Enter your age: "))
height = float(input("Enter your height in meters: "))
favourite_number = int(input("Enter your favourite_number: "))

print(name)
print(age)
print(height)
print(favourite_number)

birth_year = 2025 - 19

print("\n🙍🏻‍♀️ Here is the summary of your information:")
print(f"name: {name}")
print(f"age: {age}years")
print(f"Estimated Birth Year: {birth_year}")
print(f"height: {height} meters")
print(f"favourite number: {favourite_number}")

print("\n🧠 Type Conversion Note:")
print("-> age was converted from string to integer using int().")
print("-> height was converted from string to float using float().")

print("\n🔍 Variable Summary")
print(f"name -> Value: {name}, Type:{type(name)}, Memory ID: {id(name)}")
print(f"age -> Value: {age}, Type:{type(age)}, Memory ID: {id(age)}")
print(f"height -> Value: {height}, Type:{type(height)}, Memory ID: {id(height)}")
print(f"favourite_number -> Value: {favourite_number}, Type:{type(favourite_number)}, Memory ID: {id(favourite_number)}")
print(f"birth_year -> Value: {birth_year}, Type:{type(birth_year)}, Memory ID: {id(birth_year)}")

print("🙏🏻 Thank you for using the Personal Date Collector!")