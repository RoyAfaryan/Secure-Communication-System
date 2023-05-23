# Secure Message Transfer System

The Secure Message Transfer System is designed to securely send and receive messages between a sender and a receiver. It utilizes RSA, AES, and HMAC algorithms for encryption, decryption, and message authentication.

## System Design

The system consists of two main classes: the "Sender" class and the "Receiver" class.

### Sender Class Attributes:

- `rsa_key_generation`: Generates public and private keys of size 1024.
- `aes_message_encryption`: Encrypts plaintext using AES CBC mode.
- `aes_key_encryption`: Encrypts the AES key using RSA public key.
- `generate_mac`: Generates a MAC key and returns a message authentication code.

### Receiver Class Attributes:

- `rsa_key_generation`: Generates public and private keys of size 1024.
- `aes_message_decryption`: Decrypts ciphertext using the AES key.
- `aes_key_decryption`: Decrypts the AES key using the RSA private key.
- `verify_mac`: Verifies the MAC to ensure message integrity.

The system also includes a file named "main.py" which runs the program using the functions from the Sender and Receiver classes to (1) send messages and (2) read messages.

## Algorithms Used

The following algorithms are used in the system:

- RSA: Used to generate key pairs and encrypt/decrypt the AES key.
- AES: Used for symmetric encryption of the plaintext message.
- HMAC: Used for generating and verifying the message authentication code.

## Key Lengths

- RSA key length: 1024 bits (for both sender and receiver)
- AES key length: 16 bytes
- MAC key length: 16 bytes

## Program Usage

1. Run "main.py" to start the program.
2. The program will prompt the user to enter a message.
3. The message will be encrypted using AES-CBC mode, and a MAC will be generated using HMAC-SHA256.
4. The AES key will be encrypted using the receiver's RSA public key.
5. The ciphertext message, IV, encrypted AES key, MAC key, and MAC will be stored in the "ciphertext.txt" file located in the "transmitted_data" folder.
6. The "read_message()" function will automatically be executed, which extracts the components from the "ciphertext.txt" file and outputs a "plaintext.txt" file. This file contains the decrypted message, which should match the original message entered during program execution.
7. The MAC of the decrypted message will be verified to ensure message integrity.

