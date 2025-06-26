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
##Question_2

```py
originalString = input("Enter string for palindrome check") #asking the user to put the string that can be checked

def checkPalindrome(originalString): # declaring the function to check if the String is palindrome
  reversed = ""                      # declare a variable called reversed with empty string
  for char in originalString:        # the loop that takes every character that is stored in original string starting to the back character
    reversed = char + reversed       # The new empty string will accumullate character by character until the whole string is inside but reversed
    if (originalString == reversed): # comparison if the string and it's reverse are the same
      print("Yes it's palindrome")   # Message
    else:
      print("No it's not palindrome")

checkPalindrome(originalString)      # Call function
```
