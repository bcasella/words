#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re, collections
import os

class Words():

    def __init__(self):
        self.word = None
        self.NWORDS = self.train(self.words(open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)),
                         'palavrasptbr.txt'), 'r').read()))
        self.alphabet = 'aãáâbcçdeẽéêfghiíjklmnoõóôpqrstuúvwxyz'
        #print(self.NWORDS)

    def isPalindrome(self, word):
        if word is None:
            return False
        tamanho = len(word)
        for i in range(tamanho):
            if word[i].upper() not in word[tamanho-1-i].upper():
                return False
        return True

    #################################################################
    # Spell Corrector function based on Peter Norvig function       #
    # http://norvig.com/spell-correct.html                          #
    # Changes were made to get it to work with brazilian portuguese #
    # It uses dict words and two Machado de Assis books as words DB #
    #################################################################
    def words(self, text): return re.findall('[a,ã,á,â,b,c,ç,d,e,ẽ,é,ê,f,g,h,i,í,j,k,\
        l,m,n,o,õ,ó,ô,,p,q,r,s,t,u,ú,v,w,x,y,z]+', text)

    def train(self, features):
        model = collections.defaultdict(lambda: 1)
        for f in features:
            model[f] += 1
        return model

    def edits1(self, word):
       splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
       deletes    = [a + b[1:] for a, b in splits if b]
       transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
       replaces   = [a + c + b[1:] for a, b in splits for c in self.alphabet if b]
       #print(replaces)
       inserts    = [a + c + b     for a, b in splits for c in self.alphabet]
       return set(deletes + transposes + replaces + inserts)

    def known_edits2(self, word):
        return set(e2 for e1 in self.edits1(word) for e2 in self.edits1(e1) if e2 in self.NWORDS)

    def known(self, words): return set(w for w in words if w in self.NWORDS)

    def correct(self, word):
        candidates = ( self.known([word]) or self.known(self.edits1(word)) or
                                           self.known_edits2(word) or [word] )
        return max(candidates, key=self.NWORDS.get)
