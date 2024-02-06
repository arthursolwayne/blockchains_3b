import hashlib
import os

def hash_collision(k):
    if not isinstance(k,int):
        print("hash_collision expects an integer")
        return(b'\x00',b'\x00')
    if k < 0:
        print("Specify a positive number of bits")
        return(b'\x00',b'\x00')

    # Define the hash function
    def H(s):
        return hashlib.sha256(s).hexdigest()[-k:]

    # Initialize x and y
    x = os.urandom(20)
    y = H(x)

    # Main loop
    while H(x) != H(y):
        x = H(x)
        y = H(H(y))

    # Find the position μ of first repetition
    mu = 0
    x = os.urandom(20)
    while x != y:
        x = H(x)
        y = H(y)
        mu += 1

    # Find the length λ of the shortest cycle starting from x
    lambda_ = 1
    y = H(x)
    while x != y:
        y = H(y)
        lambda_ += 1

    return mu, lambda_
