#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2/24/17 10:46 AM
# @Author  : Jackling 

import pyparsing as pp

# simple example
print '--------------'
letterDigit = pp.And([pp.Word(pp.alphas, exact=1),pp.Word(pp.nums, exact=1)])
print letterDigit.parseString('x5')
digitsLetters = pp.Word(pp.nums) + pp.Word(pp.alphas)
print digitsLetters.parseString('23skiddoo')

# caselessliteral
print '--------------'
ni=pp.CaselessLiteral('Ni')
print ni.parseString('Ni')
print ni.parseString('NI')
print ni.parseString('nI')
print ni.parseString('ni')

# OneOrMore
print '--------------'
name = pp.Word(pp.alphas)
number = pp.Word(pp.nums)
nameNoOrBang = pp.Or([name, number, pp.Literal('!')])
print nameNoOrBang.parseString('Brian')
print nameNoOrBang.parseString('73')
print nameNoOrBang.parseString('!')
several = pp.OneOrMore(nameNoOrBang)
print several.parseString('18 years of total silence!')
print several.parseString('18 years of total silence?')

# body exat exclude
print '--------------'
name = pp.Word('abcdef')
print name.parseString('fadedglory')
pyName = pp.Word(pp.alphas+'_', bodyChars=pp.alphanums+'_')
print pyName.parseString('_crunchyFrog13')
name4 = pp.Word(pp.alphas, exact=4)
print name4.parseString('Whizzo')
noXY = pp.Word(pp.alphas, excludeChars='xy')
print noXY.parseString('Sussex')

# Optional is like OneOrMore
print '--------------'
letter = pp.Word(pp.alphas, exact=1)
number = pp.Word(pp.nums)
chapterNo = number + pp.Optional(letter)
print chapterNo.parseString('23')
print chapterNo.parseString('23c')
chapterX = number + pp.Optional(letter, default='*')
print chapterX.parseString('23')
