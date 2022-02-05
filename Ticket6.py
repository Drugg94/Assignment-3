# Revision 1 Feb 4, 2022
## Begin Derek J. Ruggirello (Feb 1, 2022)

import random

file_In = open("rockyou.txt", "r")

password = ""

i = 0

while i < 40:
    x = random.randint(1, 12)
    j = 0
    while j <= x:
        password = password + chr(random.randint(63, 122))
        j+=1
    print(password)
    password = ""
    i+=1

# Revision 1 Feb 4, 2022
## End Derek J. Ruggirello here
# Omega Group/ Ram Valud/ Michael Walker/ project greenwood321 #