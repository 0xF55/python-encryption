def xorer(text,key):
    xored = ""
    for i in range(len(text)):
        xored += chr(ord(text[i]) ^ ord(key[i % len(key)]))

    return xored
