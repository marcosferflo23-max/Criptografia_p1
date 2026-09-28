# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 20:10:21 2026

@author: marco
"""

from vigenere import decrypt, cosets, encrypt
from break_caesar import break_caesar

DICTIONARY_OF_FREQUENCES_ENGLISH= {
    'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702, 'F': 2.228,
    'G': 2.015, 'H': 6.094, 'I': 6.966, 'J': 0.153, 'K': 0.772, 'L': 4.025,
    'M': 2.406, 'N': 6.749, 'O': 7.507, 'P': 1.929, 'Q': 0.095, 'R': 5.987,
    'S': 6.327, 'T': 9.056, 'U': 2.758, 'V': 0.978, 'W': 2.360, 'X': 0.150,
    'Y': 1.974, 'Z': 0.074
}

DICTIONARY_OF_FREQUENCES_SPANISH= {
    'A': 12.525, 'B': 1.417, 'C': 4.675, 'D': 5.860, 'E': 13.681, 'F': 0.692,
    'G': 1.008, 'H': 0.703, 'I': 6.247, 'J': 0.443, 'K': 0.011, 'L': 4.967,
    'M': 3.157, 'N': 6.712, 'O': 8.683, 'P': 2.510, 'Q': 0.877, 'R': 6.871,
    'S': 7.977, 'T': 4.632, 'U': 2.927, 'V': 1.138, 'W': 0.017, 'X': 0.215,
    'Y': 1.008, 'Z': 0.467
}

ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def chi_squared(text: str, table: dict[str, float]) -> float:
    text_ncharacters= len(text)
    if text_ncharacters == 0:
        raise ValueError
        
    sum_chi2=0
    for i in range(0,26):
        prob_of_letter_in_text=text.count(ALPHABET[i])*100/text_ncharacters
        sum_chi2+= ((prob_of_letter_in_text-table[ALPHABET[i]])**2)/table[ALPHABET[i]]
        
    return sum_chi2

def break_vigenere(ciphertext: str, m: int, language: str = "en") -> tuple[str, str]:
    """m is the key length, given to you. Returns (key, plaintext)."""
    if language == "en":
        freq_table = DICTIONARY_OF_FREQUENCES_ENGLISH
    else:
        freq_table = DICTIONARY_OF_FREQUENCES_SPANISH
    
    
    vig_cosets = cosets(ciphertext, m)
    
    solution_key = ""
    
    for coset in vig_cosets:
        solution_number_caesar, solution_text_caesar = break_caesar(coset, language=language)
        
        key_letter = chr(solution_number_caesar + 65)
        solution_key += key_letter
        

    final_plaintext = decrypt(ciphertext, solution_key)
    
    return solution_key, final_plaintext



#Measurement task.
EN_TEXT= (
    "YOUWILLREJOICETOHEARTHATNODISASTERHASACCOMPANIEDTHECOMMENCEMENTOFANENTERP"
    "RISEWHICHYOUHAVEREGARDEDWITHSUCHEVILFOREBODINGSIARRIVEDHEREYESTERDAYANDMY"
    "FIRSTTASKISTOASSUREMYDEARSISTEROFMYSWELFAREANDINCREASINGCONFIDENCETOTHESU"
    "CCESSOFMYUNDERTAKINGWHICHYOUKNOWIHAVEBEENANXIOUSTOACCOMPLISHFORSOONALONGP"
    "ERIODANDNOWITHINKITISTIMEFORTHESALTTRAVELTOBEGINANDIHOPEYOUWILLSENDMELET"
    "TERSOFENCURAGEMENTSOONASPOSSIBLE"
)
    
    
import random as rdm

def simulate(text, lang_text, lang_attack, lengths, m):
    print(f"\n--- Text: {lang_text} | Table: {lang_attack} ---")
    for L in lengths:
        correct_ans = 0
        for _ in range(200):
            # Extract a random fragment
            ini = rdm.randint(0, len(text) - L)
            frag = text[ini : ini + L]
            
            # Encipher with a random key
            k_real = "".join(rdm.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(m))
            cipher = encrypt(frag, k_real)
            
            # Attack blind
            k_pred, _ = break_vigenere(cipher, m, language=lang_attack)
            
            if k_pred == k_real:
                correct_ans += 1
                
        print(f"Length {L}: {(correct_ans / 200) * 100:.1f}% recovery rate")

if __name__ == "__main__":
    longs = [60, 120, 200, 300]
    

    simulate(EN_TEXT, "en", "en", longs, m=3)
    simulate(EN_TEXT, "en", "en", longs, m=5)
    simulate(EN_TEXT, "en", "en", longs, m=7)


