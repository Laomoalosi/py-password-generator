import random
from string import digits
from string import punctuation
from string import ascii_letters

symbols = ascii_letters + digits + punctuation
secure__random = random.SystemRandom()
password = "".join(secure__random.choice(symbols)
                    for i in range(20))
print(password)