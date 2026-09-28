# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 20:11:28 2026

@author: marco
"""
import pytest
import caesar
import affine
import vigenere

def test_caesar_encrypt():
    assert caesar.encrypt("MYSECRETMESSAGE", 3) == "PBVHFUHWPHVVDJH"

def test_caesar_decrypt():
    assert caesar.decrypt("PBVHFUHWPHVVDJH", 3) == "MYSECRETMESSAGE"

def test_affine_encrypt():
    assert affine.encrypt("A", 5, 8) == "I"

def test_affine_decrypt():
    assert affine.decrypt("I", 5, 8) == "A"

def test_affine_invalid_key():
    with pytest.raises(ValueError):
        affine.encrypt("HELLO", 2, 5)

def test_vigenere_encrypt():
    assert vigenere.encrypt("ATTACKATDAWN", "LEMON") == "LXFOPVEOFNHR"

def test_vigenere_decrypt():
    assert vigenere.decrypt("LXFOPVEOFNHR", "LEMON") == "ATTACKATDAWN"

def test_vigenere_invalid_key():
    with pytest.raises(ValueError):
        vigenere.encrypt("HELLO", "")
