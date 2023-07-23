import RSA_Algo 
import time 
while True :
    choice = input("DO u want encryption(C) or decryption(D) !! :")
    if choice == "C":
        C = int(input("enter the message or ciphertext C : "))
        e = int(input("enter e : "))
        n = int(input("enter n : "))
        encyptiontext = RSA_Algo.exp_mod(C,e,n)
        print(f"encrption cipher of {C} is {encyptiontext}")
        break
    if choice == "D":
        D = int(input("Enter the encrypted text to decrypt: "))
        d = int(input("enter d  : "))
        n = int(input("enter n : "))
        decryptedtext = RSA_Algo.exp_mod(D,d,n)
        print(f"{choice}: The original plaintext/message was : {decryptedtext}")
        break

time.sleep(5)