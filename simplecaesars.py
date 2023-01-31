def caesar_encrypt(text):
    result = ""
    for i in range(len(text)): 
        #ord() obtains ascii value
        pos = ord((text[i])) - 97
        newPos = ((pos + 3)%26)+97
        result += chr(newPos)
        print(result)
    return result

def caesar_decrypt(cipherText):
    result = ""
    for i in range(len(cipherText)):
        pos = ord(cipherText[i])-97
        newPos = ((pos-3)%26)+97
        result += chr(newPos)
        print(result)
    return result

text = "picoctf"
print(f"plain text: {text}")
cipherText = caesar_encrypt(text)
print(f"Encrypted: {cipherText}")
print(f"decrypted: {caesar_decrypt(cipherText)}")
