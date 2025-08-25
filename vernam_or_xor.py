"""
Vernam Stream Cipher || XOR Encryption
Written by: 0xF55
Date: 2025/8/24
"""

def vernam(text="",key=0xf,decrypt=False): # any key in hex
    cipher = ""
    for t in text:
        xored = ord(t) ^ key
        cipher += chr(xored)

    return cipher

