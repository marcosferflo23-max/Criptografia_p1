# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:14:55 2026

@author: marco
"""

#1-How to run everything, with verbatim commands. (Done with AI, I didn´t know how to do it)
Since this submission does not include a command-line interface engine, all cryptographic and breaking functions can be verified and executed directly using the automated test suite or manually via the interactive Python shell.

### 1. Running the Automated Test Suite (Verifies All Core Functions)
To execute all validation tests for encryption, decryption, and error raising, run this exact command in your terminal:
```bash
python tests/test_crypto.py
```

### 2. Running the Laboratory Simulation Scripts
To execute the random-fragment benchmark experiments and output the statistical tables for the analysis, run:
```bash
python experiment_c1.py
python experiment_c2.py
python experiment_c3.py
```

### 3. Running Functions Manually via Interactive Python Shell
To test any specific internal function (such as `to_numbers`, `to_letters`, or `chi_squared`) with your own inputs, open your terminal and execute the following sequence:

```bash
python
```

Once the interactive Python prompt (`>>>`) opens, you can import and call any function from any module with these verbatim commands:

```python
# Testing basic transformations
from basics import to_numbers, to_letters
to_numbers("ABCDEF")
to_letters([0, 1, 2, 3, 4, 5])

# Testing Caesar automated breaker
from break_caesar import break_caesar
break_caesar("PBVHFUHWPHVVDJH", language="en")

# Testing Affine automated breaker
from break_affine import break_affine
break_affine("CRIPTOGRAMA...", language="es")

# Testing Vigenere automated breaker
from break_vigenere import break_vigenere
break_vigenere("LXFOPV...", m=5, language="en")

# Testing the Frequency Assistant Report
from assist import report
print(report("QATNTYSMHQ...", language="en"))

# Exit the interactive shell when finished
exit()
```
    

#2-Key space size for each of the four ciphers, with the reasoning.
##   1-Caesar
     The key space is 26, because there are 26 letters in the English aplhabet.

##   2-Affine
     The keyspace is 312
     This is due to the possible values of a which are 12 because the greatest common divisor between a and 26 must be 1 so it leaves 12 choices for a
     and 26 for b which have no restrictions.
     The greatest common divisor between a and 26 must be 1 because a must be invertible modulo 26, or decryption is impossible
     The keyspace is 12 (a different possible values) multiplied by 26 (b different possible values) 12*26=312.

##   3-Monoalphabetic
     The keyspace is 26!.
     This is due to at first for the first letter you have 26 options to select the correspondient letter, then for the next you only have 25 and then 24...
     
##   4-Vigenere
     The keyspace is 26**m (m, m is the lenght of the keyword)
     This is due to aach character in the keyword can be chosen from the 26 letters of the alphabet. This results in 26 choices multiplied by itself m times, so it has 26**m total combinations.


#3-C1 Measurement
Measurement tables:

--- Text: en | Table: en ---
Length 20: 100.0% recovery rate
Length 30: 100.0% recovery rate
Length 40: 100.0% recovery rate
Length 60: 100.0% recovery rate
Length 100: 100.0% recovery rate

--- Text: es | Table: es ---
Length 20: 100.0% recovery rate
Length 30: 100.0% recovery rate
Length 40: 100.0% recovery rate
Length 60: 100.0% recovery rate
Length 100: 100.0% recovery rate

--- Text: es | Table: en ---
Length 20: 77.5% recovery rate
Length 30: 100.0% recovery rate
Length 40: 93.5% recovery rate
Length 60: 100.0% recovery rate
Length 100: 100.0% recovery rate


At which length does your breaker become reliable?
The breaker is 100% reliable from 20 letters when the table is correct in English and in Spanish.

This is due to the keyspace is very sort, only 26. Even in sorts texts of 20 letters, the average frequency of letters
of the language is strongest enough to make the correct key visible over the other 25 possibles keys, 
which produce caotic combinations

How much does the wrong language table actually cost you?
Using the wrong table costs exactly 22.5% in effectiveness for very short texts like 20 characters, 
where the rate drops from 100% to 77.5%. However, for texts of 30 characters or more, the cost is practically zero, 
because the algorithm has a 100% success rate. It helps that English and Spanish are similar language in therms of frequence of many letters.



#4-C2 Measurement
Measurment tables:
--- Text: en | Table: en ---
Length 20: 75.0% recovery rate
Length 30: 97.0% recovery rate
Length 40: 100.0% recovery rate
Length 60: 100.0% recovery rate
Length 100: 100.0% recovery rate

--- Text: es | Table: es ---
Length 20: 81.0% recovery rate
Length 30: 93.0% recovery rate
Length 40: 100.0% recovery rate
Length 60: 100.0% recovery rate
Length 100: 100.0% recovery rate

--- Text: es | Table: en ---
Length 20: 30.5% recovery rate
Length 30: 24.0% recovery rate
Length 40: 42.5% recovery rate
Length 60: 69.5% recovery rate
Length 100: 100.0% recovery rate


At which recovery is reliable?
It becomes 100% reliable starting at 40 letters in both languages . It is less efficient than Caesar, which had 100% with just 20 letters. 
This is due to the much larger key space (312 vs. 26), in very short texts like 20 letters ones, it is easy that an incorrect key order the 
letters on a way that it looks a real text randomly, tricking the Chi-square test. With 40 letters, this noise disappears.

With 312 candidate keys, the Chi-square test easily confuses the minor statistical differences between English and Spanish in small texts. 
False keys have more chances to force a Spanish text to fit badly in the English pattern. Only with 100 letters the recovery rate is 100.0%.
 


#5- C3 Measurement
M=3
--- Text: en | Table: en ---
Length 60: 87.5% recovery rate
Length 120: 100.0% recovery rate
Length 200: 100.0% recovery rate
Length 300: 100.0% recovery rate

M=5
--- Text: en | Table: en ---
Length 60: 39.0% recovery rate
Length 120: 100.0% recovery rate
Length 200: 100.0% recovery rate
Length 300: 100.0% recovery rate

M=7
--- Text: en | Table: en ---
Length 60: 1.5% recovery rate
Length 120: 47.0% recovery rate
Length 200: 100.0% recovery rate
Length 300: 100.0% recovery rate

What actually governs whether this works — the total length of the ciphertext, or something else?
Success does not depend on the total length of the text, it depends on the length of the text per coset(m). 
Since the algorithm divides the ciphertext into m interleaved sequences and attacks each one as an independent Caesar cipher, 
each individual sequence must accumulate enough letters for the chi-square statistic to function reliabily.


Say what the quantity is, and explain why a longer key makes Vigenère stronger even though the cipher itself has not changed:
A longer key (m bigger) distributes the characters in a larger number of independent blocks. This makes that, for a given total text length, each coset receives far fewer letters for analysis, thereby forcing the attacker to use much longer texts to break the cipher.

#6- C4 findings on the cryptogram given.
The algorithm only got right T -> E, H->I, U->V.
The single most useful line in the whole report for a human solver is the one that contains the trigrams repeated.
In this case QAT is repeated three times and the most used trigram in English is THE, and in this case QAT is THE, so it help us a lot to decrypt the text.

Rank alignment alone does not solve the cipher, specially, in short texts like this one (110 letters), the statistical sample is not big enough to have conclusions. 
The actual order of appearance of the letters in this paragraph varies a little from the theoretical average for the English language.

What really solves a monoalphabetic cipher is not counting individual letters, but rather analysing bigrams and trigrams, recognizing words as they take shape, 
looking for double letters, considering the subject matter of the text, and, if it is possible, knowing as much as we can about the author of the text, etc.




#7- AES-128.
The difference is in the fact that monoalphabetic encryption is linear and preserves the language's structure of the ciphertext,
this facilitates decryption using the tools implemented in assist.py, such as identifying trigrams, bigrams, 
and the most or least frequent letters. In contrast, AES-128 employs a non-linear substitution and permutation network (SPN)
applied ten times in succession. This creates an "avalanche effect," where changing only a single letter at the beginning
completely alters the final text. It eliminates language patterns, making the task of decryption significantly more difficult
for an attacker.



#8-Failures.
I dind´t do the D part.
The vigenere fail in the test but I think it is a good code.


#IA USE
I did some questions to Gemini only to orient in some aspects, I show the promts:

Pregunta a Gemini sobre el caesar breaker:
dime que debo seguir para hacer el chi-sqared, no me des la solucion ni el codigo, solo pautas que seguir. yo creo que lo primero es contar cuantas veces se repite cada palabra en el texto (no cuento un espacio ni un signo de puntuacion como caracter), luego hacer el chi cuadrado de cada letra, de la A a la Z. No se si hacer dos comparaciones una con el español y otra con el ingles, creo que hare eso.
Respuesta:
¡Vas por muy buen camino con tu razonamiento! Tus intuiciones son excelentes, aunque hay un pequeño matiz clave: en criptografía clásica no contamos palabras completas, sino letras individuales. El texto cifrado te vendrá como un bloque continuo de letras unidas (sin espacios ni signos, ya normalizado), por lo que contarás cuántas veces aparece cada carácter de la A a la Z.
Aquí tienes las pautas ordenadas paso a paso que debes seguir para diseñar tu función de Chi-cuadrado sin ver código:
1. Limpieza de seguridad (Opcional pero recomendable)
Aunque el enunciado dice que el texto ya viene limpio, asegúrate de medir solo los caracteres válidos. Mide la longitud total del texto (solo contando caracteres de la A a la Z). Si por algún motivo la longitud es cero, tu función debe reaccionar devolviendo una puntuación de error máxima para evitar errores matemáticos más adelante.
2. El bucle del alfabeto (A-Z)
Debes montar un bucle que recorra, una a una, las 26 letras del alfabeto estándar (de la A a la Z). Para cada una de esas letras individuales, vas a realizar los siguientes cálculos.
3. Obtener los dos datos de la fórmula por cada letra
Para cada letra del alfabeto, necesitas calcular dos valores numéricos:
•	La Frecuencia Observada (Lo que hay): Cuenta cuántas veces aparece físicamente esa letra dentro del texto descifrado que estás evaluando.
•	La Frecuencia Esperada (Lo que debería haber): Mira el porcentaje teórico de esa letra en el diccionario que te han pasado como argumento. Como ese porcentaje está basado en un grupo de 100 letras, calcula cuántas letras te corresponderían proporcionalmente multiplicando ese porcentaje por la longitud real de tu texto (y dividiendo entre 100).
4. Aplicar la matemática por letra y acumular
Una vez tienes cuánto se repite la letra en la realidad frente a cuánto debería repetirse según la teoría, aplicas la resta de ambos valores, elevas esa diferencia al cuadrado y divides el resultado entre el valor teórico esperado. Ve sumando este resultado en una variable "marcador" que empiece en cero.
5. El requisito obligatorio: Normalizar
Cuando tu bucle termine de sumar los resultados de las 26 letras, tendrás una puntuación total. El enunciado te exige explícitamente normalizarla. Para ello, coge esa suma final y divídela entre la longitud total del texto. Esto garantizará que un texto de 20 letras y uno de 100 letras compitan en igualdad de condiciones.
________________________________________
💡 Sobre tu duda de las dos comparaciones (Inglés vs Español):
¡Tu enfoque es correcto pero se gestiona un paso más adelante! Tu función chi_squared solo debe recibir un texto y un diccionario de idioma, y devolver un número (cuanto más bajo sea el número, más se parece el texto a ese idioma).
Será en la función break_caesar donde decidas qué diccionario pasarle: si el usuario pide "en", le pasas el de inglés; si pide "es", le pasas el de español. El programa probará los 26 desplazamientos usando esa tabla elegida y se quedará de forma automática con el desplazamiento que logre la puntuación más baja.
¿Qué te parece este mapa de pasos? Cuando lo tengas planteado en tu cabeza, dime si prefieres que veamos:
•	Las pautas para estructurar el bucle de los 26 desplazamientos en break_caesar.
•	O cómo enfocar el experimento del laboratorio para rellenar las tablas de aciertos.

Pregunta a Gemini:
en teoria el texto viene sin espacios ni signos de puntuacion?

Respuesta:
Sí, en teoría el texto te va a venir completamente limpio: solo letras mayúsculas de la A a la Z, sin espacios ni signos de puntuación [1, 2].
In Caesar_breaker, for the letters frequency tables, I have relied on Robert Lewand’s historical statistical data for English, and on studies by Jesús María Ruiz combined with data from the Real Academia Española for Spanish.

Pregunta a Gemini:
dime un texto en ingles y uno en español para poder probar el caesar breaker, con unos 200 caracteres (todo junto, sin signos de puntuacion y caracteres normales(evita las ñ) (las letras con tilde las pones sin tilde)
Respuesta:
Aquí tienes los dos textos de 200 caracteres exactos cada uno, completamente normalizados (solo letras de la A a la Z en mayúsculas, sin espacios, sin signos de puntuación, sin la letra Ñ y sin tildes), listos para que los uses en las pruebas de tu cifrador y de tu atacante César [C1].
🇬🇧 Texto de prueba en Inglés (200 caracteres)
Este texto está extraído del inicio de Frankenstein de Mary Shelley [C1]:
text
YOUWILLREJOICETOHEARTHATNODISASTERHASACCOMPANIEDTHECOMMENCEMENTOFANENTERPRISEWHICHYOUHAVEREGARDEDWITHSUCHEVILFOREBODINGSIARRIVEDHEREYESTERDAYANDMYFIRSTTASKISTOASSUREMYDEARSISTEROFMYSWELFAREANDINCREASINGCONFIDENC
Usa el código con precaución.
🇪🇸 Texto de prueba en Español (200 caracteres)
Este texto está extraído del inicio de Don Quijote de la Mancha de Miguel de Cervantes [C1]:
text
ENUNLUGARDELAMANCHADECUYONOMBRENOQUIEROACORDARMENOHAMUCHOTIEMPOQUEVIVIAUNHIDALGODELOSDELANZAINASTILLEROADARGALANTIGUAROCINFLACOYGALGOCORREDORUNAOLACOLLASMASVACESTAQUECARNEROLASSOMANUSTAPICADOSLOSSABADOSLANTE
Usa el código con precaución.



#MORE IA USE, NOT ONLY FOR ORIENT.
I used the IA Gemini to help me with the Measurement task of break_caesar.py, then I reused that in the Measurement task of break.affine.py and break.vigenere.py. I used it in the code from line 73 of break_caesar to the end.
I substituted some values and some variables but the structure is the same as Caesar, I did the substitution with no IA help.

I used IA Gemini in the assit.py, all before line 70 I did it by myself, but from line 70 to the end it is done by Gemini.
I used IA Gemini to do the #1 apart of the README