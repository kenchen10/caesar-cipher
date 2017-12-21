"""Caesar Cipher"""

"""A dictionary of letters: numbers"""
d0 = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26)))
"""A dictionary of numbers: letters"""
d1 = dict(zip(range(26), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
"""A dictionary of letter frequencies in the English language"""
englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41,
'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77,
'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
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
