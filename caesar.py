# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:14:55 2026

@author: marco
"""
#B1 Caesar


def encrypt(plaintext: str, k: int) -> str:
    lenght=len(plaintext)
    answer=""
    for i in range(0, lenght):
        answer += chr(((ord(plaintext[i]) + k -65) % 26)+65)
    return answer
    


def decrypt(ciphertext: str, k: int) -> str:
    lenght=len(ciphertext)
    answer=""
    for i in range(0, lenght):
        answer += chr(((ord(ciphertext[i]) - k -65) % 26)+65)
    return answer





#K+20= E o F
#75+20= 95
#mi rango es de 65 a 90
#deberia ser 70 (o 5)

#75 + 20 = 95-65=30 % 26 = 4 + 65= 69=E