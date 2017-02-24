#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2/24/17 10:47 AM
# @Author  : Jackling 

# my test
import pyparsing as pp

# start|open|turn on the|a|my|None lamp|light
verb = ['start','open','turn on']
mid = ['the','a','my']
light = ['light','lamp']

pp_verb = pp.Or([pp.CaselessLiteral(x) for x in verb])
pp_mid = pp.ZeroOrMore(pp.Or([pp.CaselessLiteral(x) for x in mid]))
pp_light = pp.Or([pp.CaselessLiteral(x) for x in light])
pp_parse = pp_verb  + pp_mid + pp_light

test_str=[
    'start the light',
    'turn on my light',
    'start lamp',
    'Start Lamp',
    'Start a a a Lamp',
    'xxx lamp',
    'start lamp please',
    'open lamp, open lamp',
    'please open the lamp',
    'please open the lamp!!!',
    'please do not open the lamp'
]

def get_start_str(s):
    s = str(s).lower()
    for v in verb:
        try:
            idx = s.index(v)
            return s[idx:]
        except:
            pass
    return s

def check_one_str(t):
    if 'not' in str(t).lower():
        return False
    else:
        start_t = get_start_str(t)
        try:
            pp_parse.parseString(start_t)
            return True
        except:
            return False

for t in test_str:
    if check_one_str(t):
        print 'suc',t
    else:
        print 'err',t
