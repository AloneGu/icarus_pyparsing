#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2/24/17 11:21 AM
# @Author  : Jackling 


import pyparsing as pp

# set|make the|a|my|this air condictioner|ac|temperature to|as|None 25

set1_list = ['set', 'make']
set2_list = ['the', 'a', 'my', 'this']
set3_list = ['air condictioner', 'ac', 'temperature']
set4_list = ['to', 'as']

pp_set1 = pp.Or([pp.CaselessLiteral(x) for x in set1_list])
pp_set2 = pp.Optional(pp.Or([pp.CaselessLiteral(x) for x in set2_list]))
pp_set3 = pp.Or([pp.CaselessLiteral(x) for x in set3_list])
pp_set4 = pp.Optional(pp.Or([pp.CaselessLiteral(x) for x in set4_list]))
pp_set5 = pp.Word(pp.nums)

pp_parse = pp_set1 + pp_set2 + pp_set3 + pp_set4 + pp_set5

test_str = [
    'set the ac 25 degree',
    'set this ac to 26 degree',
    'set the temperature to 27',
    'siri, set ac 28'
]

for t in test_str:
    try:
        x = pp_parse.parseString(t)
        print 'suc',x
    except:
        print 'err', t

