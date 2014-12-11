# coding='utf-8'
__author__ = 'Yun Zhu'

import string

allChars = string.maketrans('', '')


def makefilter(keep):
    delChars = allChars.translate(allChars, keep)

    def theFilter(s):
        return s.translate(allChars, delChars)

    return theFilter


if __name__ == '__main__':
    just_vowels = makefilter('aeiouy')
    print(just_vowels('four score and seven years ago'))