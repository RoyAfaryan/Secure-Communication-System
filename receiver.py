# imports
import rsa
from Crypto.Cipher import AES
import os
import hmac
import hashlib


class receiver:
    
    # generate rsa keys
    def rsa_key_generation(self):
        
        # generate keys
        public_key, private_key = rsa.newkeys(1024)

        # private key only accessible in receiver class
        self.private_key = private_key

        # return public key
        return public_key
    
    # decrypt message encrypted by aes key
    def aes_message_decryption(self, ciphertext, iv, aes_key):

        # create cipher
        cipher = AES.new(aes_key, AES.MODE_CBC, iv)

        # decrypt ciphertext
        plaintext = cipher.decrypt(ciphertext)

        # return plaintext
        return plaintext
    
    # decrypt aes key
    def aes_key_decryption(self, encrypted_aes_key):

        # encrypt aes key usuing rsa public key
        aes_key = rsa.decrypt(encrypted_aes_key, self.private_key)

        # return encrypted aes key
        return aes_key
    
    # Read ciphertext, IV, and encrypted AES key from file
    def read_ciphertext(self, file_path):

        with open(file_path, "rb") as file:
            content = file.read()
    
        parts = content.split(b'\n-----\n')
        ciphertext = parts[0]
        iv = parts[1]
        encrypted_aes_key = parts[2]
        mac_key = parts[3]
        mac = parts[4]
    
        return ciphertext, iv, encrypted_aes_key, mac_key, mac
    
    def verify_mac(self, plaintext, mac, mac_key):

        hmac_calculated = hmac.new(mac_key, plaintext, hashlib.sha256)
        hmac_digest = hmac_calculated.digest()

        if hmac.compare_digest(mac, hmac_digest):
            print("MAC verification successful.")
        else:
            print("MAC verification failed.")