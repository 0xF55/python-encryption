"""
Affine Cipher
Written by: 0xF55
Date: 2025/8/25
"""

def affine(text="",key=(5,2),decrypt=False):
    
    text = text.upper()
    
    if len(key) != 2:
        print("Error: Key length must be 2")
        return -1
    
    a = key[0]
    b = key[1]
    
    a_inv = pow(a,-1,26)
    
    cipher = ""
    
    if not decrypt:
        for t in text:
            if t.isalpha():
                c = ord(t) - ord("A")
                c = ( (a*c) + b) % 26
        
                cipher += chr(ord("A") + c)
            else:
                cipher += t
    else:
        for t in text:
            if t.isalpha():
                c = ord(t) - ord("A")
                x = (a_inv * (c - b)) % 26
                cipher += chr(x + ord("A"))
            else:
                cipher += t
   
            
    return cipher
    