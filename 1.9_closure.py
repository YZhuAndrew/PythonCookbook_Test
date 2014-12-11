# coding='utf-8'
__author__ = 'Yun Zhu'


# closure
def make_adder(addend):
    def adder(augend):
        return augend + addend

    return adder


p = make_adder(22)
q = make_adder(23)

print('%d, %d' % (p(100), q(100)))
print('{}, {}'.format(p(200), q(200)))

import string

'AAaaBBbbCCccDDdd'