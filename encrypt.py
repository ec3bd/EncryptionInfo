__author__='ec3bd'
#Eamon Collins

from Crypto.Cipher import DES
from Crypto.PublicKey import RSA
from os import path

def main():
    key = RSA.generate(2048)
    f = open('rsakey.pem','wb')
    f.write(key.exportKey(format='PEM'))
    f.close()

    #Testing secret_string
    privkeyfile = open('rsakey.pem','r')
    privkey = RSA.importKey(privkeyfile.read())
    privkeyfile.close()
    cipher = secret_string("Our little secret".encode('utf-8'), key.publickey())
    print(cipher)
    print(privkey.decrypt(cipher))

    print("")

    #Testing ecncrypt/decrypt file
    deskey = DES.new(b'ssrae32j')
    encrypt_file('test.txt', deskey)
    #with open("test.txt.enc") as f:
    #print(f.read())
    print(decrypt_file("test.txt.enc", deskey))
    with open("DEC_test.txt") as f:
        print(f.read())




def secret_string(secret,pubkey):
    ciphertext = pubkey.encrypt(secret,0)
    return ciphertext[0]

def encrypt_file(filename, symkey):
    file = open(filename, 'rb')
    data = file.read()
    file.close()
    encdata = symkey.encrypt(data)
    wfile = open(filename + ".enc", 'wb')
    wfile.write(encdata)
    wfile.close()

def decrypt_file(filename, symkey):
    file = open(filename, 'rb')
    data = file.read()
    file.close()
    filename = filename[:-4]
    print(data)
    bstring = symkey.decrypt(data)
    wfile = open('DEC_' + filename, 'wb')
    wfile.write(bstring)
    origfile = open(filename, 'rb')
    data2 = origfile.read()
    return data2 == bstring


if __name__=='__main__':
    main()