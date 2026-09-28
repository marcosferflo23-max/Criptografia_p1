# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:52:36 2026

@author: marco
"""


def to_numbers(text: str) -> list[int]: # normalised text -> 0..25
    sol_list=[]
    for i in range(0, len(text)):
        sol_list.append(ord(text[i])-65)


    return sol_list

def to_letters(nums: list[int]) -> str: # 0..25 -> text
    word=""
    for i in range(0, len(nums)):
        word+=chr(nums[i]+65)
    return word

def egcd(a: int, b: int) -> tuple[int, int, int]:
    if a == 0:
        return b, 0, 1
    gcd, x_aux, y_aux = egcd(b % a, a)
    x = y_aux - (b // a) * x_aux
    y = x_aux
    return gcd, x, y

    #6,9   --->  3, 6x+9y= 3      mcd=3        x=-1     y=1
    #3,6
    #0,3            9,0,1        9,0,1         x= 0 - 3*0*1=-1          y=1
    #3,1,0


   # ax + by = mcd(a,b)
    #devuelve (mcd,x,y)
    
    
    
#def modinv(a: int, m: int) -> int:
#    if egcd(a,m)[0]!=1:
#        raise ValueError
#    result=0
#    while result*a % m !=1:
#        result +=1
#    return result


def modinv(a: int, m: int) -> int:
    m_pos= abs(m)
    mcd, x, y= egcd(a, m_pos)
    if mcd != 1:
        raise ValueError
    return x % m_pos
    
    
def xor_bytes(data: bytes, key: bytes) -> bytes: # key repeats cyclically
    if len(key) == 0:
        raise ValueError
        
    answer = bytearray()
    for i in range(len(data)):
        byte = data[i] ^ key[i % len(key)]
        answer.append(byte)
    return bytes(answer)
