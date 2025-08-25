"""
Ceaser Cipher
Written by: 0xF55
Date: 2025/8/24
"""

def check_range(char):
    if ord(char) - ord("A") in range(26):
        return True
    return False

def ceaser(text="",key=3,decrypt=False):
    cipher = ""
    if not decrypt:
        for t in text.upper():
            if check_range(t):
                # getting number based on alphabetic order
                pos = ord(t) - ord("A")
                # get offset to the new char
                shifted = (pos + key) % 26
                # getting the new char
                new = chr(shifted + ord("A"))
                cipher += new
            else:
                cipher += t    
    else:
        for t in text.upper():
            if check_range(t):
                pos = ord(t) - ord("A")
                shifted = (pos - key) % 26
                new = chr(shifted + ord("A"))
                cipher += new
            else:
                cipher += t

    return cipher

