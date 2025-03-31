import string
import random
def generate(n):
    c = string.ascii_letters+string.digits+string.punctuation
    password =''.join(random.choice(c) for _ in range(n))
    return password

n = int(input("Enter n"))
r=generate(n)
print(r)
