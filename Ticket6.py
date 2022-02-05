# Revision 1 Feb 4, 2022
## Begin Derek J. Ruggirello (Feb 1, 2022)

# Imports 'random' module as requested per customer.
import random

# Variable to store password to be added.
Password = ""

# List of random passwords.
dictionary = []

# List of unacceptable passwords.
dictionary_List = ["123456", "12345", "123456789", "password","iloveyou","princess","1234567","rockyou","12345678","abc123","nicole","daniel","babygirl","monkey","lovely","jessica","654321","michael","ashley","qwerty","111111","iloveu","000000","michelle","tigger","sunshine","chocolate","password1","soccer","anthony","friends","butterfly","purple","angel","jordan","liverpool","justin","loveme"]

# Looping variable
i = 0

# Loop in order to determine the length of passwords and create them.
while i < 40:
    x = random.randint(1, 12)
    j = 0
    # Loop to add characters to Password string
    while j <= x:
        Password = Password + chr(random.randint(63, 122))
        j+=1
    # Branch that determines if the Password is in the unacceptable list and deletes it if true.
    if Password in dictionary_List:
        break
    else:
        # Adds password to dictionary list of acceptable passwords.
        dictionary.append(Password)
    Password = ""
    i+=1

# Outputs all passwords created that were acceptable.
print(dictionary)

# Revision 1 Feb 4, 2022
## End Derek J. Ruggirello here
# Omega Group/ Ram Valud/ Michael Walker/ project greenwood321 #