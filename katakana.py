#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

""" Katakana word translation

This module is responsible solely for translating words from Romanji
to Katakana.  Its called only by katawm and only within its add and
edit functions.  It is modeled after the hiragana module.

"""


_vowel = ('A', 'I', 'U', 'E', 'O')
_hiraganaDict = {   'A':  'ア', 'I':  'イ', 'U':  'ウ', 'E':  'エ', 'O':  'オ',
                    'KA': 'カ', 'KI': 'キ', 'KU': 'ク', 'KE': 'ケ', 'KO': 'コ',
                    'GA': 'ガ', 'GI': 'ギ', 'GU': 'グ', 'GE': 'ゲ', 'GO': 'ゴ',
                    'SA': 'サ', 'SHI':'シ', 'SU': 'ス', 'SE': 'セ', 'SO': 'ソ',
                    'ZA': 'ザ', 'JI': 'ジ', 'ZU': 'ズ', 'ZE': 'ゼ', 'ZO': 'ゾ',
                    'TA': 'タ', 'CHI':'チ', 'TSU':'ツ', 'TE': 'テ', 'TO': 'ト',
                    'DA': 'ダ', 'DI': 'ヂ', 'DU': 'ヅ', 'DE': 'デ', 'DO': 'ド',
                    'NA': 'ナ', 'NI': 'ニ', 'NU': 'ヌ', 'NE': 'ネ', 'NO': 'ノ',
                    'HA': 'ハ', 'HI': 'ヒ', 'FU': 'フ', 'HE': 'ヘ', 'HO': 'ホ',
                    'BA': 'バ', 'BI': 'ビ', 'BU': 'ブ', 'BE': 'ベ', 'BO': 'ボ',
                    'PA': 'パ', 'PI': 'ピ', 'PU': 'プ', 'PE': 'ペ', 'PO': 'ポ',
                    'MA': 'マ', 'MI': 'ミ', 'MU': 'ム', 'ME': 'メ', 'MO': 'モ',
                    'YA': 'ヤ',	           'YU': 'ユ',             'YO': 'ヨ',
                    'RA': 'ラ', 'RI': 'リ', 'RU': 'ル', 'RE': 'レ', 'RO': 'ロ',
                    'WA': 'ワ', 
                    'stsu': 'ッ',  'N':   'ン',   'dv': 'ー',
                    'KYA': 'キャ', 'KYU': 'キュ', 'KYO': 'キョ', 
                    'SHA': 'シャ', 'SHU': 'シュ', 'SHO': 'ショ', 
                    'CHA': 'チャ', 'CHU': 'チュ', 'CHO': 'チョ', 
                    'NYA': 'ニャ', 'NYU': 'ニュ', 'NYO': 'ニョ', 
                    'HYA': 'ヒャ', 'HYU': 'ヒュ', 'HYO': 'ヒョ', 
                    'MYA': 'ミャ', 'MYU': 'ミュ', 'MYO': 'ミョ', 
                    'RYA': 'リャ', 'RYU': 'リュ', 'RYO': 'リョ', 
                    'GYA': 'ギャ', 'GYU': 'ギュ', 'GYO': 'ギョ', 
                    'JA':  'ジャ', 'JU':  'ジュ', 'JO':  'ジョ', 
                    'BYA': 'ビャ', 'BYU': 'ビュ', 'BYO': 'ビョ', 
                    'PYA': 'ピャ', 'PYU': 'ピュ', 'PYO': 'ピョ', 
                    '.':   '。',   '!':   '!',   '?':   '?', 
				}

def trans(r):
    r = r.upper()
    tmp = ''
    output = ''
	
    # Loop through all letters.
    for i in range(0, len(r)):
        tmp += r[i]
		
        # Enters if tmp is a complete syllable.
        if r[i] in _vowel:
            output += inter_vowel_logic(r,i,tmp)
            tmp = ''
				
        # Enters if this is not the last character AND not a vowel.
        elif i < len(r)-1:
            output += inter_other_logic(r,i,tmp)
            # If inter_other_logic actually returned a value, delete tmp
            if inter_other_logic(r,i,tmp) != '':
                tmp = ''
        
        # Deals with punctuation.
        elif r[i] in ('.', '?', '!'):
            output += _hiraganaDict[tmp]
            tmp = ''
            
    return output
    
def inter_vowel_logic(r,i,tmp):
    # Deals with small Y syllables.  Disregards starting sylables
    if (r[i-2] is not _vowel) and (r[i-1] == 'Y') and (i >= 2):
        return _hiraganaDict[tmp]
            
    # Deals with double vowels that are the same.
    elif (r[i] in _vowel) and (i != 0) and (r[i-1] == r[i]):
        return _hiraganaDict['dv']
        
    # Displays run of the mill syllables.
    else:
        return _hiraganaDict[tmp]
    
def inter_other_logic(r,i,tmp):
    # Deals with single n syllables.
    if (r[i] == 'N') and (r[i+1] not in _vowel) and (r[i+1] != 'Y'):
        return _hiraganaDict[tmp]
        
    # Deals with small Tsu (Double consonant.)
    elif (r[i] == r[i+1]) and (i < len(r)-1):
        return _hiraganaDict['stsu']
        
    # Deals with spaces.
    elif r[i] == ' ':
        return '    '
        
    # Enters if no translation can be made. (Not a bad thing.)
    else:
        return ''
