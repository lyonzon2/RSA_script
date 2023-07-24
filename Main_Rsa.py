import RSA_Algo 
import time 

def encode_string(string):
    encoded = 0
    for char in string:
        encoded = encoded * 256 + ord(char)
    return encoded

def decode_string(encoded_number):
    decoded = ""
    while encoded_number > 0:
        char_code = encoded_number % 256
        decoded = chr(char_code) + decoded
        encoded_number //= 256
    return decoded

while True :
    choice = input("DO u want encryption(C) or decryption(D) !! :")
    if choice == "C":
        message = input("enter the message or ciphertext C : ")
        message_encoded = [ord(ch) for ch in message]
        e = int(input("enter e : "))
        n = int(input("enter n : "))
        encyptiontext = [RSA_Algo.exp_mod(ch,e,n) for ch in message_encoded]
        encyptiontext = "".join(chr(ch) for ch in encyptiontext )
        print(f"encrption cipher  is [{encyptiontext}]")
        break

    if choice == "D":
        message = input("Enter the encrypted text to decrypt: ")
        message_decoded = [ord(ch) for ch in message]
        print(message_decoded)
        d = int(input("enter d  : "))
        n = int(input("enter n : "))
        decryptedtext = [RSA_Algo.exp_mod(ch,d,n) for ch in message_decoded]
        decryptedtext = "".join(chr(ch) for ch in decryptedtext)
        print(f"{choice}: The original plaintext/message was : [{decryptedtext}]")
        break

time.sleep(5)