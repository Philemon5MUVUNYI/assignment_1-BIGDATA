current_year = 2025
name = input("Enter your name: ")
year = int(input("Enter your birth year:"))

def ageCalculation(year):
  age = current_year - year
  return age

print("f{name}, your age is {ageCalculation(year)}")
