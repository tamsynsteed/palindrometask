#if the string is made of no letters or just one letter, then it is a palindrome.
def palindrome(s):
    if len(s) < 1:
        return True

#check if first and last letters are the same
    else:
        if s[0] == s[-1]:
# if the first and last letters are the same. Strip them from the string, and determine whether the string that remains is a palindrome. This function checks the middle, substring.
            return palindrome(s[1:-1])
        else:
            return False
a=input("Enter string:")
if(palindrome(a)==True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")

