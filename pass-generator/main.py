import string
from random import *
mixchars = string.ascii_letters+string.digits+string.punctuation
randompass = "".join(choice(mixchars) for x in range(randint(8, 20)))
print("Your Random Password is: ", randompass)