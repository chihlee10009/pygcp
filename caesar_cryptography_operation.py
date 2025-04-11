#take the symkey and encrypt using caesar cipher

def caesar(msg, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890="
    encmsg = ""
    for letter in msg:
        num = alphabet.index(letter)
        num += key
        num %= len(alphabet)
        encmsg += alphabet[num]
    return encmsg

if __name__ == "__main__":
    encmsg = caesar("blah", 23)
    decodedmsg = caesar(encmsg, -23)
    print("encoded message=", encmsg, "\ndecodedmsg=", decodedmsg)
