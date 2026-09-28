# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 20:08:15 2026

@author: marco
"""


def encrypt(plaintext: str, key: str) -> str:
    if set(key) != set("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        raise ValueError

    lenght = len(plaintext)
    answer = ""
    for i in range(0, lenght):
        answer += key[(ord(plaintext[i])-65)]
    return answer


def decrypt(ciphertext: str, key: str) -> str:
    if set(key) != set("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        raise ValueError

    lenght = len(ciphertext)
    answer = ""

    for i in range(0, lenght):
        pos = key.index(ciphertext[i])
        answer += chr(pos + 65)
    return answer

# encrypt("HELLO", "MNBVCXZASDFGHJKLPOIUYTREWQ")  -->  "ACGGK"
# H  va a la 7 letra de key y la sustituye

# entonces en decrypt al contrario
# encrypt("ACGGK", "MNBVCXZASDFGHJKLPOIUYTREWQ")  -->  "HELLO"
# es ver donde esta la A en key (ver la posicion de la A) y luego susituir ese numero por la letra correspondiente (la H es 7)


def key_from_keyword(keyword: str) -> str:
    result = ""
    lenght = len(keyword)
    for i in range(0, lenght):
        if keyword[i] not in result:
            result += keyword[i]
            
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0, 26):
        if ALPHABET[i] not in result:
            result += ALPHABET[i]
    return result
