from RSAEncryptDecrypt import encryption, decryption

p = 29
q = 37
e = 11
n = p*q
privateN = (p - 1)*(q - 1)
PublicKey = (n, e)
PrivateKey = 275

message = input('enter the message:  ')

encryptedMessage = encryption(message, n, e)

print(encryptedMessage)

decryptedMessage = decryption(encryptedMessage, n, PrivateKey)

print(decryptedMessage)










