import string
import nltk
nltk.download('words', quiet=True)
from nltk.corpus import words

def encrypt(string, key) -> str:
    encryption = ''
    for c in string:
        if c.isupper():
            c_index = ord(c) - ord('A')
            c_shifted = (c_index + key) % 26 + ord('A')
            c_new = chr(c_shifted)
            encryption += c_new
        elif c.islower():
            c_index = ord(c) - ord('a')
            c_shifted = (c_index + key) % 26 + ord('a')
            c_new = chr(c_shifted)
            encryption += c_new
        elif not c.isalpha():
            encryption += c 
    return encryption


def decrypt(string, key) -> str:
    decryption = ''
    for c in string:
        if c.isupper():
            c_index = ord(c) - ord('A')
            c_shifted = (c_index - key) % 26 + ord('A')
            c_new = chr(c_shifted)
            decryption += c_new 
        if c.islower():
            c_index = ord(c) - ord('a')
            c_shifted = (c_index - key) % 26 + ord('a')
            c_new = chr(c_shifted)
            decryption += c_new 
        elif not c.isalpha():
            decryption += c 
    return decryption
    # OR JUST DO: 
    # return encrypt(string, -key)

def crack(string):
    count = []
    list_of_words = words.words()
    for k in range(26):
        decryption = decrypt(string, k)
        text_list = decryption.split(' ')
        for word in text_list:
            count.append(0)
            if word in list_of_words:
                count[k] += 1
    max_count = count.index(max(count))
    return decrypt(string, max_count)

