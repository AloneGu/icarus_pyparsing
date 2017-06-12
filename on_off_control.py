#!/usr/bin/env python
# encoding: utf-8

"""
@author: Jackling Gu
@file: on_off_control.py
@time: 2017-06-12 14:10
"""

import pyparsing as pp

CONTROL_WORDS = ["打开", "关闭", "关掉", "启动", "开启"]
HELP_WORDS = ["帮我把", "把"]
MISC_WORDS = ["啊", "吧"]


class OnOffDetector(object):
    def __init__(self):
        pass

    def preprocess(self, text):
        tmp_txt = text
        for k in MISC_WORDS:
            tmp_txt.replace(k, '')
        return tmp_txt

    def process(self, text):
        try:
            text = self.preprocess(text)
            # match 打开 xxx
            for k in CONTROL_WORDS:
                if text.startswith(k):
                    dev_name = text[2:]
                    if len(dev_name) >= 1:
                        return True, dev_name

            # match 把  xxx 打开
            for start_k in HELP_WORDS:
                if text.startswith(start_k):
                    for end_k in CONTROL_WORDS:
                        if text.endswith(end_k):
                            dev_name = text[len(start_k):-2]
                            if len(dev_name) >= 1:
                                return True, dev_name
        except:
            pass
        return False, None


test_text = ["把书房灯打开", "打开书房灯", "关掉空调吧", "打开88","不要打开空调","打开书法灯"]

t = OnOffDetector()
for txt in test_text:
    print(t.process(txt))
