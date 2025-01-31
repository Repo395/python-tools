# Password must be at least 14 characters in length
# Password must contain at least one character from each of the following four character sets:
# Uppercase characters (string.ascii_uppercase)
# Lowercase characters (string.ascii_lowercase)
# Numerical Digits (string.digits)
# Special Characters (string.punctuation)
# Password cannot contain more than three consecutive characters from the same character set.
# Password cannot contain whitespace characters (string.whitespace)
# Returns True if a valid password. False, otherwise.

import re
def pword(password):
       
 
       if len(password) <=14:
               print("Your password must be 14 characters long.")
               return False
       elif not re.findall(r'^\s+', password):
               print("Password can not contain spaces.")
               return False			   
       elif not re.findall(r'\d+', password):
               print("You need a number in your password.")
               return False
       elif not re.findall(r'[A-Z]+', password):
               print("You need a capital letter in your password.")
               return False
            
       elif not re.findall(r'[|\"|\'|~|!|@|#|$|%|^|&|*|(|)|_|=|+|\||,|.|/|?|:|;|[|]|{\}|<|>]', password):
               print("You need a Special Character in your password.")
               return False
       elif not re.findall(r'[a-z]+', password):
               print("You need a lowercase in your password.")
               return False
       else:
               print("Password Accepted")
               return True
 
passwordValid = False
while not passwordValid:
   password = input("Type in your password: ")
   passwordValid = pword(password)
 
