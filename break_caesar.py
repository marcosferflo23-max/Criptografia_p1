# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 20:09:35 2026

@author: marco
"""
from caesar import decrypt
from caesar import encrypt

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
        
    

    
    #frecuencia= num_apariciones_letra_en_texto/long_texto   *100
    
    #total=0
    #for i in range (0, 26):
    
        
def break_caesar(ciphertext: str, language: str = "en") -> tuple[int, str]:
    if language == "en":
        freq_table = DICTIONARY_OF_FREQUENCES_ENGLISH
    else:
        freq_table = DICTIONARY_OF_FREQUENCES_SPANISH
    
    
    solution_number=0
    solution_text= ciphertext
    sum_chi2_prov= float("inf")
    for i in range(0,26):
        new_ciphertext= decrypt(ciphertext, i)
        actual_number= chi_squared(new_ciphertext, freq_table)
        if actual_number < sum_chi2_prov:
            sum_chi2_prov= actual_number
            solution_number=i
            solution_text=new_ciphertext
    
    return solution_number, solution_text
    




#Measurement task.
EN_TEXT= "YOUWILLREJOICETOHEARTHATNODISASTERHASACCOMPANIEDTHECOMMENCEMENTOFANENTERPRISEWHICHYOUHAVEREGARDEDWITHSUCHEVILFOREBODINGSIARRIVEDHEREYESTERDAYANDMYFIRSTTASKISTOASSUREMYDEARSISTEROFMYSWELFAREANDINCREASINGCONFIDENC"
    
SP_TEXT="ENUNLUGARDELAMANCHADECUYONOMBRENOQUIEROACORDARMENOHAMUCHOTIEMPOQUEVIVIAUNHIDALGODELOSDELANZAINASTILLEROADARGALANTIGUAROCINFLACOYGALGOCORREDORUNAOLACOLLASMASVACESTAQUECARNEROLASSOMANUSTAPICADOSLOSSABADOSLANTE"
    
import random as rdm

def simulate(text, lang_text, lang_attack, lengths):
    print(f"\n--- Text: {lang_text} | Table: {lang_attack} ---")
    for L in lengths:
        correct_ans = 0
        for _ in range(200):
            # Extract a random fragment
            ini = rdm.randint(0, len(text) - L)
            frag = text[ini : ini + L]
            
            # Encipher with a random key
            k_real = rdm.randint(0, 25)
            cipher = encrypt(frag, k_real)
            
            # Attack blind
            k_pred, _ = break_caesar(cipher, language=lang_attack)
            
            if k_pred == k_real:
                correct_ans += 1
                
        print(f"Length {L}: {(correct_ans / 200) * 100:.1f}% recovery rate")

if __name__ == "__main__":
    longs = [20, 30, 40, 60, 100]
    
    simulate(EN_TEXT, "en", "en", longs)
    simulate(SP_TEXT, "es", "es", longs)
    simulate(SP_TEXT, "es", "en", longs)
