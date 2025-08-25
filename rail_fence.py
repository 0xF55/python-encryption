"""
Rail Fence Cipher
Written by: 0xF55
Date: 2025/8/24
"""

def rail(text="",key=3,decrypt=False):

    tlen = len(text)
    rails = [[''] * tlen for _ in range(key)]
    row,direction = 0,1

    for i,c in enumerate(text):
        rails[row][i] = c if not decrypt else '*'
        if row == key - 1:
            direction = -1
        if row == 0:
            direction = 1
        row += direction
    
    if not decrypt:
        cipher = ""
        print("Rails Format:")
        for rail in rails:
            print(rail)
            cipher += ''.join(rail)
        print("Encrypted:")
        print(cipher)
        return cipher

    else:

        i = 0
        for r in range(key):
            for c in range(tlen):
                if rails[r][c] == "*" and i < tlen:
                    rails[r][c] = text[i]
                    i+=1

        cipher = ""
        for c in range(tlen):
            for r in range(key):
                if rails[r][c] != '':
                    cipher += rails[r][c]

        print("Decrypted:")
        print(cipher)

