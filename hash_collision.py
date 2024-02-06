import hashlib
import os

def hash_collision(k):
    if not isinstance(k, int):
        print("hash_collision expects an integer")
        return (b'\x00', b'\x00')
    if k <= 0:
        print("Specify a positive number of bits")
        return (b'\x00', b'\x00')
    found = False
    while not found:
        x = os.urandom(16) 
        y = os.urandom(16)
        hash_x = hashlib.sha256(x).digest()
        hash_y = hashlib.sha256(y).digest()
        bit_mask = (1 << k) - 1 
        if (int.from_bytes(hash_x, byteorder='big') & bit_mask) == (int.from_bytes(hash_y, byteorder='big') & bit_mask):
            found = True

    return (x, y)
