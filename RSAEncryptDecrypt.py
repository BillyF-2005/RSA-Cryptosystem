

def encryption(message, n, e):
    encryptedMessage = []
    for char in message:
        m = ord(char)
        c = (m**(e))%n
        encryptedMessage.append(c)
    return(encryptedMessage)

def decryption(encryptedMessage, n, d):
    decryptedCode = []
    decryptedMessage = []
    for int in encryptedMessage:
        m = (int**d)%n
        decryptedCode.append(m)
        mi = chr(m)
        decryptedMessage.append(mi)
    return(decryptedMessage)
