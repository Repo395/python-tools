import random 
import string 
 
def randomStringDigits(stringLength=24): 
    """Generate a random string of letters and digits """ 
    lettersAndDigits = string.ascii_letters + string.digits 
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength)) 
 
print ("Generating a Password") 
print ("Password is  ", randomStringDigits(24)) 
