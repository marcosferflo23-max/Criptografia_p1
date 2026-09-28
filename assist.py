# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 20:10:57 2026

@author: marco
"""
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


EJEMPLO= "HOLAMELLAMOMARCOSFERNANDEZFLORESYMEENCANTAELLA"

def report(ciphertext: str, language: str = "en") -> str:
    if language == "en":
        freq_lang = DICTIONARY_OF_FREQUENCES_ENGLISH
    else:
        freq_lang = DICTIONARY_OF_FREQUENCES_SPANISH
        
    dictionary_letters_freq={}
    for i in ALPHABET:
        count= ciphertext.count(i)
        freq= (count*100)/len(ciphertext)
        freq_letter= freq_lang[i]
        dictionary_letters_freq[i]= (count, freq,freq_letter)
          
    shorted_dict= sorted(dictionary_letters_freq.items(), key=lambda x: x[1][0], reverse=True)
    
    
    trigrams_dict={}
    for i in range(0, len(ciphertext)-2):
        trigram= ciphertext[i:i+3]
        if trigram in trigrams_dict:
            trigrams_dict[trigram].append(i)
        else:
            trigrams_dict[trigram]= [i]
            
    bigrams_dict={}
    for i in range(0, len(ciphertext)-1):
        bigram= ciphertext[i:i+2]
        if bigram in bigrams_dict:
            bigrams_dict[bigram].append(i)
        else:
            bigrams_dict[bigram]= [i]
            
    top_bigrams = sorted(bigrams_dict.items(), key=lambda x: len(x[1]), reverse=True)
    top_10_bigrams= top_bigrams[0:10]
    
    
    doubled_letter_list=[]
    for i in range(0, len(ciphertext)-1):
        if ciphertext[i]==ciphertext[i+1]:
            doubled_letter_list.append([ciphertext[i], i, i+1])
    
            

    answer = "=== FREQUENCY REPORT ===\n"
    for letter, (count, freq, freq_letter) in shorted_dict:
        answer += f"{letter}, {count}, {freq:.3f}, expected={freq_letter:.3f}\n"

    answer += "\n=== REPEATED TRIGRAMS ===\n"
    for trigram, posiciones in trigrams_dict.items():
        if len(posiciones) > 1:
            answer += f"{trigram}: count={len(posiciones)}, positions={posiciones}\n"

    answer += "\n=== TOP 10 FREQUENT BIGRAMS ===\n"
    for bigram, posiciones in top_10_bigrams:  
        answer += f"{bigram}: {len(posiciones)} times\n"

    answer += "\n=== DOUBLED LETTERS ===\n"
    for letter, pos1, pos2 in doubled_letter_list:
        answer += f"Found doubled letter '{letter}' at positions {pos1}-{pos2}\n"


    shorted_lang = sorted(freq_lang.items(), key=lambda x: x[1], reverse=True)
    lang_letters = [letter for letter, _ in shorted_lang]

    answer += "\n=== SUGGESTED INITIAL MAPPING ===\n"
    # Recorremos tu ranking usando el índice numérico
    for idx in range(len(shorted_dict)):
        crypto_letter = shorted_dict[idx][0]  # Extrae la letra del criptograma
        theorical_letter = lang_letters[idx]    # Extrae la letra del idioma en la misma posición
        answer += f"{crypto_letter} -> {theorical_letter}\n"

    print(answer)
    return



