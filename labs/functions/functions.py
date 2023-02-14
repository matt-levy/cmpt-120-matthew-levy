# takes elements in a list of strings and concatinates them in one line with no spaces
def join_strings(strings):
   
    str = ""
    
    for i in strings:
        str += i

    return str

# mad lib sentence with three variables
def mad_libs(name, noun, event):

    return f"{ name } is too cool for { noun } class. Instead she/he will be attending the { event }"

# cipher/decipher text
def caesar_cipher(text, shift):

    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for i in text:
        if i in alphabet:
            index = alphabet.find(i)
            shifted_index = (index + shift) % 26
            enciphered = alphabet[shifted_index]
            result += enciphered
        else:
            result += i

    return result

