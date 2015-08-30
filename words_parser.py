#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

from words import Words


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--palin', action='store', dest='words', nargs='+',
                        help='Store a word to be checked as palindrome')

    parser.add_argument('--correct', action='store', dest='frase', nargs='+',
                        help='Store a(n) word(s) to be checked if it is correct\
                         in portuguese' )


    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    results = parser.parse_args()

    words_treat = Words()
    if results.words is not None:
        for word in results.words:
            print 'The word "{0}" is palindrome? {1}\n'.format(
                   word, words_treat.isPalindrome(word))
        
    if results.frase is not None:
        print "The phrase spelled correct: "
        for word in results.frase:
            print words_treat.correct(word.lower()),

