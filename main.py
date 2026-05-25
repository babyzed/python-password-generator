# Enter the necessary library

import random
import string

# Define the characters from which the password is made

chars = string.ascii_letters + string.digits + "!@#$%^&*()-=_+"

# Getting the length of the password from the user

length = int(input("password length: "))

# Random password build

password = "".join(random.choice(chars) for _ in range(length))

# View and result

print("Generated password: ")
print(password)
