# imports
import os
from sender import *
from receiver import *
from Crypto.Util.Padding import pad

def send_message(receiver_rsa_public_key):
   
   # generate AES key
   aes_key = os.urandom(16)

   # get message and pad it
   message = input("Please enter a message: ")
   message = bytes(message, 'utf-8')
   padded_message = pad(message, 16)

   # generate mac
   mac_key, mac = sender_obj.generate_mac(padded_message)

   # encrypt message using aes cbc
   ciphertext, iv = sender_obj.aes_message_encryption(padded_message, aes_key)
   
   # encrypt AES key with receiver's RSA public key
   encrypted_aes_key = sender_obj.aes_key_encryption(aes_key, receiver_rsa_public_key)


   # create transmitted_data folder if it doesn't exist
   os.makedirs("transmitted_data", exist_ok=True)
   
   # write ciphertext, IV, and encrypted AES key to a file in transmitted_data folder
   file_path = os.path.join("transmitted_data", "ciphertext.txt")
   with open(file_path, "wb") as file:
        file.write(ciphertext)
        file.write(b"\n-----\n")
        file.write(iv)
        file.write(b"\n-----\n")
        file.write(encrypted_aes_key)
        file.write(b"\n-----\n")
        file.write(mac_key)
        file.write(b"\n-----\n")
        file.write(mac)

def read_message():

   # extract ciphertext, iv, and encrypted_aes_key from ciphertext
   file_path = os.path.join("transmitted_data", "ciphertext.txt")
   ciphertext, iv, encrypted_aes_key, mac_key, mac = receiver_obj.read_ciphertext(file_path)

  
   # decrypt aes_key
   aes_key = receiver_obj.aes_key_decryption(encrypted_aes_key)

   # decrypt message
   plaintext = receiver_obj.aes_message_decryption(ciphertext, iv, aes_key)
   
   # verify mac 
   receiver_obj.verify_mac(plaintext, mac, mac_key) 

   # write plaintext to file
   plaintext_file_path = os.path.join("transmitted_data", "plaintext.txt")
   with open(plaintext_file_path, "wb") as plaintext_file:
        plaintext_file.write(plaintext)


def clear_folder():
    folder_path = "transmitted_data"
    
    # Check if the folder exists
    if os.path.exists(folder_path):
        # Iterate over all files in the folder
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            
            # Check if it is a file
            if os.path.isfile(file_path):
                # Delete the file
                os.remove(file_path)
    
    print("All files in the transmitted_data folder have been deleted.")
        
def main():

   clear_folder()

   # create sender and receiever objects
   global sender_obj
   global receiver_obj
   sender_obj = sender()
   receiver_obj = receiver()

   # get RSA keys
   sender_rsa_public_key = sender_obj.rsa_key_generation()
   receiver_rsa_public_key = receiver_obj.rsa_key_generation()

   # function calls
   send_message(receiver_rsa_public_key)
   read_message()

  
if __name__ == "__main__":
      main()
