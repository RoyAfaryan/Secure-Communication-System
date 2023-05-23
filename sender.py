# imports
import rsa
from Crypto.Cipher import AES
import os
import hmac
import hashlib


class sender:

    # generate rsa keys
    def rsa_key_generation(self):

        # generate keys
        public_key, private_key = rsa.newkeys(1024)

        # private key only accessible in sender class
        self.private_key = private_key

        # return public key
        return public_key
    
    # generate AES key and encrypt message
    def aes_message_encryption(self, message, aes_key):

        # generate cipher using aes key in cbc mode
        cipher = AES.new(aes_key, AES.MODE_CBC)

        # encrypt message
        ciphertext = cipher.encrypt(message)

        #return ciphertext as well as iv
        return ciphertext, cipher.iv
    
    # encrypt AES key using receiver public key
    def aes_key_encryption(self, aes_key, rsa_public_key):

        # encrypt aes key usuing rsa public key
        encrypted_aes_key = rsa.encrypt(aes_key, rsa_public_key)

        # return encrypted aes key
        return encrypted_aes_key
    
    def generate_mac(self, padded_message):

        # generate random key
        mac_key = os.urandom(16)

        # generate mac
        hmac_calculated = hmac.new(mac_key, padded_message, hashlib.sha256)
        mac = hmac_calculated.digest()
        
        # return mac
        return mac_key, mac




        

    
       


    
    

