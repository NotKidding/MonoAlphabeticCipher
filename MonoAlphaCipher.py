import string
import random

chars = string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
cipher = chars.copy()

def encrypt():
    plaintext = input("enter plaintext: ")
    ciphertext = ''
    for i in plaintext:
        index = chars.index(i)
        ciphertext += cipher[index]
    print(f"\nPlaintext : {plaintext}")
    print(f"Ciphertext: {ciphertext}")

def decrypt():
    ciphertext = input("enter ciphertext: ")
    plaintext = ''
    for i in ciphertext:
        key = cipher.index(i)
        plaintext += chars[key]
    print(f"\nCiphertext: {ciphertext}")
    print(f"Plaintext : {plaintext}")

def main():
    random.shuffle(cipher)
    while True:
        print("\nMono-Alphabetic Cipher")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            encrypt()
        elif choice == '2':
            decrypt()
        elif choice == '3':
            print("Bye..")
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
