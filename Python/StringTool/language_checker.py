#!/usr/bin/env python
#coding=utf-8
""" 检查字符串属于哪种语言的正则表达式 """
import re

reNotAcsii = re.compile(r"[\x80-\xff]+")
reChinsese = re.compile(u"[\u4e00-\u9fa5]+")
reKorean=re.compile(u"[\uac00-\ud7ff]+")
erJpKatakana =re.compile(u"[\u30a0-\u30ff]+")
reJpHiragana =re.compile(u"[\u3040-\u309f]+")
reJp= re.compile(u"[\u3040-\u309f\u30a0-\u30ff]+")
reCJKPunctuation =re.compile(u"[\u3000-\u303f\ufb00-\ufffd]+")
ptnPunc=re.compile(u"[…·＃●♫【】．《》「」『』\[\]\(\)（）～丨_“”‘’\"\'\|\\\/\?？!@#$%\^&\*,\.：丶:;！，、。；：\-－—+<=>、\`{}~]")
reEnglish=re.compile("[a-zA-Z]+")
