originalString = input("Enter string for palindrome check")

def checkPalindrome(originalString):
  reversed = ""
  for char in originalString:
    reversed = char + reversed
    if (originalString == reversed):
      print("Yes it's palindrome")
    else:
      print("No it's not palindrome")

checkPalindrome(originalString)
