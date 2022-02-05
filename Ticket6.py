# Revision 1 Feb 4, 2022
## Begin Derek J. Ruggirello (Feb 1, 2022)


import random

Password = ""

dictionary = []

dictionary_List = ["123456", "12345", "123456789", "password","iloveyou","princess","1234567","rockyou","12345678","abc123","nicole","daniel","babygirl","monkey","lovely","jessica","654321","michael","ashley","qwerty","111111","iloveu","000000","michelle","tigger","sunshine","chocolate","password1","soccer","anthony","friends","butterfly","purple","angel","jordan","liverpool","justin","loveme"]

i = 0

while i < 40:
    x = random.randint(1, 12)
    j = 0
    while j <= x:
        Password = Password + chr(random.randint(63, 122))
        j+=1
    if Password in dictionary_List:
        break
    else:
        dictionary.append(Password)
    Password = ""
    i+=1

print(dictionary)

# Revision 1 Feb 4, 2022
## End Derek J. Ruggirello here
# Omega Group/ Ram Valud/ Michael Walker/ project greenwood321 #