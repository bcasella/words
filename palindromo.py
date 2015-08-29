#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Word():

    def __init__(self):
        word = None
        
    def setWord(self, word):
        self.word = word

    def isPalindrome(self):
        if self.word is None:
            return False
        tamanho = len(self.word)
        for i in range(tamanho):
            if self.word[i].upper() not in self.word[tamanho-1-i].upper():
                return False
        return True

