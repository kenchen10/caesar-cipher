"""Caesar Cipher"""

"""A dictionary of letters: numbers"""
d0 = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26)))
"""A dictionary of numbers: letters"""
d1 = dict(zip(range(26), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

def main():
    """Requests user phrase, key, and encryption/decryption."""
    phrase = input("Enter a phrase: ")
    key = int(input("Enter a key [1-26]: "))
    e_d = input("Would you like to encrypt or decrypt a message [e/d]: ")

    if e_d == "e":
        print("Encryption:", enc_dec(phrase, key, e_d))
    else:
        print("Decryption:", enc_dec(phrase, key, e_d))

def enc_dec(phrase, k, e_d):
    """This function encodes/decodes a message (phrase) given a key (k) and
    user input "e" or "d" (e_d). It acts as a Caesar Cipher implementation."""
    def helper(phrase, k, e_d, sign):
        if e_d == "d":
            sign = -1
        new_phrase = ""
        for letter in phrase.upper():
            letter = d1[d0[letter] + (sign * k)]
            new_phrase += letter
        return new_phrase
    return helper(phrase, k, e_d, 1)

main()
