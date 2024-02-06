import hashlib
import os

def hash_collision(k):
    if not isinstance(k,int):
        print("hash_collision expects an integer")
        return(b'\x00',b'\x00')
    if k < 0:
        print("Specify a positive number of bits")
        return(b'\x00',b'\x00')

    # Initialize dictionary to store hashes
    hash_dict = {}

    while True:
        # Generate a random string
        x = os.urandom(20)
        # Compute its hash
        x_hash = hashlib.sha256(x).hexdigest()

        # Get the last k bits of the hash
        x_hash_last_k = x_hash[-k:]

        # If the last k bits of the hash is already in the dictionary,
        # we have found a collision
        if x_hash_last_k in hash_dict:
            return x, hash_dict[x_hash_last_k]

        # Otherwise, add it to the dictionary
        hash_dict[x_hash_last_k] = x