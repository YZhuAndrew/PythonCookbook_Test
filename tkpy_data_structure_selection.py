# -*- coding: utf-8 -*-
__author__ = 'Yun'
__project__ = 'PythonCookbook_Test'

import string


def del_punctuation(file):
    readFile = open(file).readlines()
    new_eachWord = []
    for eachLine in readFile:
        for eachWord in eachLine.split():
            new_eachWord.append(eachWord.strip())
    print new_eachWord


del_punctuation('word3.txt')