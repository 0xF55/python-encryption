"""
Vigenere Cipher
Written by: 0xF55
Date: 2025/8/24
"""

def vigenere(text="",key="",decrypt=False):
    
    text = text.upper().replace(" ","")
    tlen = len(text)
    klen = len(key)
    cipher = ""

    if not decrypt:
        for i in range(tlen):
            alphaT = ord(text[i]) - ord("A")
            alphaK = ord(key[i % klen]) - ord("A")
            new = chr(((alphaT + alphaK) % 26) + ord("A"))
            cipher += new
    else:
        # Decrypt
        for i in range(tlen):
            alphaT = ord(text[i]) - ord("A")
            alphaK = ord(key[i % klen]) - ord("A")
            new = chr(((alphaT - alphaK + 26) % 26) + ord("A"))
            cipher += new

    print(cipher)
    return cipher

