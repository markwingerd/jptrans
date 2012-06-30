#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk

import hiragana
import katakana

""" Demonstration of jptrans modules 

Console does not display the Japanese characters so tkinter
is used instead.  Run this and in the entry box labeled Romanji,
type the suggestions below or any japanese you may know. The
Japanese entry box will automatically update with the converted
text. In the below suggestions both Amerika and peeji should
be converted to Katakana rather than hiragana. Watch the transition
when you complete the word. If you wish to test any other katakana 
you will need to add it to the kataWords array.

Suggestions:
Kuni wa Amerika desu.
Yuko dekimashita.
Gopeeji o akete kudasai.
Okaeri nasai.
Chotto ocha o nomimasen ka?

"""

# An Array of tuples containing Romanji, Katakana pairs
kataWords = [('AMERIKA', katakana.trans('Amerika')),
             ('PEEJI', katakana.trans('peeji'))]

def update_japanese(*args):
    """ Updates the display using svrJapanese
    
    Called whenever svrRomanji is changed.
    Begins with Searching the Romanji string for any katakana that
    are predefined in the KataWords array.  If there are any, it
    replaces them.  Lastly it has the hiragana module translate all
    remaining characters.
    
    """
    tmp = svrRomanji.get()
    
    tmp = tmp.upper()
    for romanjiItem, kataItem in kataWords:
        if romanjiItem in tmp:
            tmp = tmp.replace(romanjiItem, kataItem)
    
    svrJapanese.set(hiragana.trans(tmp))
    

""" Main window. Nothing too important aside from the lambda function """
root = Tk()	
root.title('jptrans Demo')
root.resizable(False,False)

# Labels
lblJapanese = ttk.Label(root, text='Japanese')
lblRomanji = ttk.Label(root, text='Romanji')

# Create StringVars to control entry boxes.
svrJapanese = StringVar()
svrRomanji = StringVar()

# Create Entry boxes which are controled with StringVars
entJapanese = ttk.Entry(root, textvariable=svrJapanese, width=50,
                        state='readonly')
entRomanji = ttk.Entry(root, textvariable=svrRomanji, width=50)

# Place all widgets on the frame
lblJapanese.grid(column=0, row=0)
lblRomanji.grid(column=0, row=1)

entJapanese.grid(column=1, row=0)
entRomanji.grid(column=1, row=1)

# Track when svrAddRomanji changes.
svrRomanji.trace("w", lambda name, index, mode, 
                    svrRomanji=svrRomanji: update_japanese())

# Runs the GUI
root.mainloop()
