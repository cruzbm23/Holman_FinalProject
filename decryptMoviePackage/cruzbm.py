# Name: Brianna Cruz (Holman)
# email: cruzbm@mail.uc.edu
# Assignment Title: Assignment Final Project
# Due Date: 20231207
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: This uses the cryptography.fernet Fernet library to decrpyt an encrypted string using a key from the instructor
# Citations: https://www.tutorialspoint.com/how-to-encrypt-and-decrypt-data-in-python
# Anything else that's relevant: N/A

from cryptography.fernet import Fernet 

def decode():
    f = Fernet('8viv7QrLsAKgvcV3JsZkKjZwQiinhtPQhUvbS2B14LM=')
    decrypted_data = f.decrypt(b'gAAAAABlTNM62RYBY5Huiye05gtL0mvbJuLkaCwJU4YbZdjSWbUVGo1uZLGbmuWq4Wh3zanqeFGheUHmrh62Oh5auLav5msayaFcLmfiAn9U_i-L4rAqGnY=')
    print(decrypted_data.decode())

if __name__ == "_main__":
    decode()