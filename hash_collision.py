import hashlib
import os

def hash_collision(k):
    # Validate input
    if not isinstance(k, int):
        print("hash_collision expects an integer")
        return (b'\x00', b'\x00')
    if k <= 0:
        print("Specify a positive number of bits")
        return (b'\x00', b'\x00')

    # Initialize variables
    found = False
    while not found:
        # Generate two random byte strings
        x = os.urandom(16)  # You can adjust the size as needed
        y = os.urandom(16)

        # Compute SHA256 hashes
        hash_x = hashlib.sha256(x).digest()
        hash_y = hashlib.sha256(y).digest()

        # Convert the last k bits of both hashes into integers for easy comparison
        # Note: We're comparing bits, not hexadecimal characters, so we adjust the calculation accordingly
        bit_mask = (1 << k) - 1  # Generates a bitmask to isolate the last k bits
        if (int.from_bytes(hash_x, byteorder='big') & bit_mask) == (int.from_bytes(hash_y, byteorder='big') & bit_mask):
            found = True

    return (x, y)
