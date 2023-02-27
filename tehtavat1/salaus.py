def encrypt(s):
    # TODO
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # print(len(alphabet))
    encryptedWord = ''
    i = 1
    for character in s:
        alphabetId = alphabet.find(character)
        # encrypt the character
        encryptedCharId = (alphabetId + i) % 26
        encryptedWord += alphabet[encryptedCharId]
        i += 1

    return encryptedWord

if __name__ == "__main__":
    print(encrypt("abc")) # bdf
    print(encrypt("xz")) # yb
    print(encrypt("kkkkkkkk")) # lmnopqrs
    print(encrypt("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")) # bcdefghijklmnopqrstuvwxyzabcde