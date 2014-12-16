# -*- coding: utf-8 -*-
__author__ = 'Yun'
__project__ = 'PythonCookbook_Test'


def has_no_e(word):
    if 'e' in word:
        return False
    print word
    return True


def avodis(word, letters):
    for letter in letters:
        if letter in word:
            return False
    return True


def uses_only(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    return True


def is_abecedarian(word):
    word = word.upper()
    for i in range(len(word)):
        for j in range(i + 1, len(word)):
            # print word[i], word[j]
            if word[i] > word[j]:
                return False
    return True


def is_abecedarian2(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    print word[1:]
    return is_abecedarian2(word[1:])


input_word = raw_input("Enter a word: ")
# input_str = raw_input("Enter some forbidden letters: ")
# print has_no_e(input_str)
# print avodis('yzhuandrew', input_str)
# print uses_only(input_word, input_str)
print is_abecedarian2(input_word)