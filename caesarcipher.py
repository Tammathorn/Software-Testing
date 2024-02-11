def caesarCipher(s, k):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def encrypt_char(char, shift):
        if char.lower() in alphabet:
            index = (alphabet.index(char.lower()) + shift) % 26
            return alphabet[index].upper() if char.isupper() else alphabet[index]
        return char

    encrypted_string = [encrypt_char(char, k) for char in s]
    return ''.join(encrypted_string)