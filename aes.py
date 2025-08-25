from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b"notsecret1234566"

aes = AES.new(key=key,mode=AES.MODE_CBC,iv=key)

enc = aes.encrypt(pad(b"Hello World",block_size=16))
enc2 = aes.encrypt(pad(b"Hello World",block_size=16))


print("Encrypted Data:")
print(enc)
print(enc2)
