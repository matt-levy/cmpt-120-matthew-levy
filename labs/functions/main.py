from functions import *
plain_text = "hello, world!"
cipher_text = caesar_cipher(plain_text, -15)
deciphered_text = caesar_cipher(cipher_text, 15)

print(f"The cipher text of {plain_text} is {cipher_text}.")
print(f"When we decipher {cipher_text} we get {deciphered_text}.")
print(f"Are they equal?: {plain_text == deciphered_text}")