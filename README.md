# assignment_1-BIGDATA
## Question_1

```py
current_year = 2025  # initializing the current year
name = input("Enter your name: ")  # asking the user to put the name
year = int(input("Enter your birth year:"))  # asking the user to input their birthyear

def ageCalculation(year):  # define the function of the age cslculation
  age = current_year - year  # age calculation
  return age

print("f{name}, your age is {ageCalculation(year)}")  # displaying the name and calling the function of the ageCalculation
```
