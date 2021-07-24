import random
import string

# Get 2 random characters for lowercase, uppercase,digits and punctuation
random_lowercase = random.sample(string.ascii_lowercase, 2)
random_uppercase = random.sample(string.ascii_uppercase, 2)
random_digit = random.sample(string.digits, 2)
random_punctuation = random.sample(string.punctuation, 2)

str_password = random_lowercase + random_uppercase + random_digit + random_punctuation

# join the characters to form password of 8 characters.
password = ''.join(random.sample(str_password, 8))
print(password)
