#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

""" Module to translate from Romanji to Hiragana

This module is responsible solely for translating words from Romanji
to Hiragana.  Its called only by the deck module and only within its 
add and edit functions.  It is modeled after the katakana module.

Important work that needs to be done:
Catch errors from bad romanji (eg. Computer, Love, etc)

"""

_vowel = ('A', 'I', 'U', 'E', 'O')
_hiraganaDict = {   'A':  'あ', 'I':  'い', 'U':  'う', 'E':  'え', 'O':  'お',
                    'KA': 'か', 'KI': 'き', 'KU': 'く', 'KE': 'け', 'KO': 'こ',
                    'GA': 'が', 'GI': 'ぎ', 'GU': 'ぐ', 'GE': 'げ', 'GO': 'ご',
                    'SA': 'さ', 'SHI':'し', 'SU': 'す', 'SE': 'せ', 'SO': 'そ',
                    'ZA': 'ざ', 'JI': 'じ', 'ZU': 'ず', 'ZE': 'ぜ', 'ZO': 'ぞ',
                    'TA': 'た', 'CHI':'ち', 'TSU':'つ', 'TE': 'て', 'TO': 'と',
                    'DA': 'だ', 'DI': 'ぢ', 'DU': 'づ', 'DE': 'で', 'DO': 'ど',
                    'NA': 'な', 'NI': 'に', 'NU': 'ぬ', 'NE': 'ね', 'NO': 'の',
                    'HA': 'は', 'HI': 'ひ', 'FU': 'ふ', 'HE': 'へ', 'HO': 'ほ',
                    'BA': 'ば', 'BI': 'び', 'BU': 'ぶ', 'BE': 'べ', 'BO': 'ぼ',
                    'PA': 'ぱ', 'PI': 'ぴ', 'PU': 'ぷ', 'PE': 'ぺ', 'PO': 'ぽ',
                    'MA': 'ま', 'MI': 'み', 'MU': 'む', 'ME': 'め', 'MO': 'も',
                    'YA': 'や',			    'YU': 'ゆ', 		   'YO': 'よ',
                    'RA': 'ら', 'RI': 'り', 'RU': 'る', 'RE': 'れ', 'RO': 'ろ',
                    'WA': 'わ', 					  			   'WO': 'を',
                    'stsu': 'っ',                                  'N':  'ん',
                    'KYA': 'きゃ', 'KYU': 'きゅ', 'KYO': 'きょ', 
                    'SHA': 'しゃ', 'SHU': 'しゅ', 'SHO': 'しょ', 
                    'CHA': 'ちゃ', 'CHU': 'ちゅ', 'CHO': 'ちょ', 
                    'NYA': 'にゃ', 'NYU': 'にゅ', 'NYO': 'にょ', 
                    'HYA': 'ひゃ', 'HYU': 'ひゅ', 'HYO': 'ひょ', 
                    'MYA': 'みゃ', 'MYU': 'みゅ', 'MYO': 'みょ', 
                    'RYA': 'りゃ', 'RYU': 'りゅ', 'RYO': 'りょ', 
                    'GYA': 'ぎゃ', 'GYU': 'ぎゅ', 'GYO': 'ぎょ', 
                    'JA':  'じゃ', 'JU':  'じゅ', 'JO':  'じょ', 
                    'BYA': 'びゃ', 'BYU': 'びゅ', 'BYO': 'びょ', 
                    'PYA': 'ぴゃ', 'PYU': 'ぴゅ', 'PYO': 'ぴょ', 
                    '.':   '。',   '!':   '!',   '?':   '?', 
				}

def trans(r):
    """ Translates Romanji text to Hiragana text.
    
    This function takes in a string of Romanji text and outputs a string
    of Hiragana text using two other functions for the more detailed
    rules.  The module uppers the text and begins looping through the
    string using an integer as the index (This is because the two other
    functions need to look at surrounding characters).  First it adds the
    character to a tmp variable that will establish a Japanese syllable
    that will be used to make the conversion from the hiraganaDict. Then
    it detects if the current character is in ASCII range. If it is not, 
    it skips the character (These characters have probably been converted 
    to Katakana or Kanji already).  Then it checks to see if the currect
    character is a vowel, if it is, it skips to the _inter_vowel_logic
    function. After that it deletes tmp and continues the loop.  -----
    
    """
    r = r.upper()
    tmp = ''
    output = ''
	
    # Loop through all letters.
    for i in range(0, len(r)):
        if ord(r[i]) > 255:
            output += r[i]
            continue
        
        tmp += r[i]
		
        # Enters if tmp is a complete syllable.
        if r[i] in _vowel:
            output += _inter_vowel_logic(r,i,tmp)
            tmp = ''
            continue
				
        # Handles other syllables where the next character needs to be 
        # checked.  Enters if this is not the last character AND not a
        # vowel.
        elif (i < len(r)-1) or (r[i] == 'N'):
            output += _inter_other_logic(r,i,tmp)
            # If inter_other_logic actually returned a value, delete tmp
            if _inter_other_logic(r,i,tmp) != '':
                tmp = ''
            continue
        
        # Deals with punctuation.
        elif r[i] in ('.', '?', '!'):
            output += _hiraganaDict[tmp]
            tmp = ''
            
    return output
    
def _inter_vowel_logic(r,i,tmp):
    # Deals with small Y syllables.  Disregards starting sylables
    if (i >= 2) and (r[i-2] is not _vowel) and (r[i-1] == 'Y'):
        return _hiraganaDict[tmp]
        
    # Deals with single char relationals.
    elif ((i >= 1) and (r[i] in ('E', 'O')) and (r[i-1] == ' ') and 
          (r[i+1] == ' ')):
        if r[i] == 'E':
            return _hiraganaDict['HE']
        if r[i] == 'O':
            return _hiraganaDict['WO']
            
    # Deals with changing Wa relational to Ha
    elif ((2 < i < len(r)-1) and (r[i-2] == ' ') and 
          (r[i+1] == ' ') and (tmp == 'WA')):
        return _hiraganaDict['HA']
            
    # Deals with double O
    elif (r[i] == 'O') and (r[i-1] == 'O'):
        return _hiraganaDict['U']
        
    # Displays run of the mill syllables.
    elif (tmp in _hiraganaDict.keys()):
        return _hiraganaDict[tmp]
    
    # Enters if no translation can be made. (Is a user error)
    else:
        return tmp
    
def _inter_other_logic(r,i,tmp):
    # Deals with single n syllables but not if they are at the end of r.
    if ((i < len(r)-1) and (r[i] == 'N') and (r[i+1] not in _vowel) and 
            (r[i+1] != 'Y')):
        return _hiraganaDict[tmp]
        
    # Deals with single n syllables that are specifically at the end of r
    elif (i == len(r)-1) and (r[i] == 'N'):
        return _hiraganaDict[tmp]
        
    # Deals with small Tsu (Double consonant.)
    elif (i < len(r)-1) and (r[i] == r[i+1]):
        return _hiraganaDict['stsu']
        
    # Deals with spaces.
    elif r[i] == ' ':
        return '    '
        
    # Enters if no translation can be made. (Not an error.)
    else:
        return ''
