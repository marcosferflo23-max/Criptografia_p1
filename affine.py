# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 20:06:33 2026

@author: marco
"""
from basics import egcd
from basics import modinv
def encrypt(plaintext: str, a: int, b: int) -> str:
    #gdc(a,26) must be 1
    if egcd(a,26)[0] != 1:
        raise ValueError
    
    lenght=len(plaintext)
    answer=""
    for i in range(0, lenght):
        answer += chr((((ord(plaintext[i]) -65)*a +b) % 26)+65)
    return answer


#a * (x) + b
#x= (ord(plaintext[i]) -65)   
    
    
    
def decrypt(ciphertext: str, a: int, b: int) -> str:
    lenght=len(ciphertext)
    answer=""
    for i in range(0, lenght):
        answer += chr(((((ord(ciphertext[i]) -65)-b) * modinv(a,26)) % 26)+65)
    return answer
    
    
#x= a inv * (y-b)
#y=(ord(ciphertext[i]) -65)
    
def valid_keys() -> list[tuple[int, int]]:
    sol_list=[]
    for a in range (0,26):
        if egcd(a, 26)[0] == 1:
            for b in range (0,26):
                sol_list.append((a,b))
    return sol_list
                