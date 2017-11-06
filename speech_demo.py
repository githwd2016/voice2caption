#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: hwd 
@time: 2017-08-22 12:01 
"""
import speech_recognition as sr
if __name__ == '__main__':
    r = sr.Recognizer()
    with sr.AudioFile('./test.wav') as source:
        audio = r.record(source)
    IBM_USERNAME = 'efb1b1b2-ed22-466b-985a-582d701469b7'
    IBM_PASSWORD = 'rwKVhts31xQV'
    text = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD, language='ja-JP', show_all=True)
    print(type(text))
    print(text)
