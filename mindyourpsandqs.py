#mind your Ps and Qs ctf script: rsa encryption
#public key is pair (e, n)
# private key is pair (d, n)

# (message^e) % n = ciphertext 
# (ciphertext^d) % n = message

c = 240986837130071017759137533082982207147971245672412893755780400885108149004760496
n = 831416828080417866340504968188990032810316193533653516022175784399720141076262857
e = 65537

#factorialized n with online tool
p = 1593021310640923782355996681284584012117
q = 521911930824021492581321351826927897005221

phi = 831416828080417866340504968188990032809792688581518853605812107051211928595245520

def phiCalc():
    return "phi is " + str((p-1)*(q-1))

print("\n" + phiCalc() + ", d is the inverse of e mod phi")

def findD(): 
    return pow(e, -1, phi)

d = findD()
print("d: " + str(d))

def decrypt():
    return bytearray.fromhex(hex(pow(c, d, n))[2:]).decode("ascii")

print(decrypt())
