#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: hwd 
@time: 2017-08-22 16:24 
"""
import json
import speech_recognition as sr
import hashlib
from urllib import request, parse
import random


class SpeechRecognition(object):
    def __init__(self, credential_path='./credentials.json'):
        with open(credential_path, 'r') as f:
            baidu = json.load(f)['ibm']
        self._url = baidu['url']
        self._username = baidu['username']
        self._password = baidu['password']

    def speech_to_text(self, input_path):
        recognizer = sr.Recognizer()
        with sr.AudioFile(input_path) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_ibm(audio,
                                        username=self._username,
                                        password=self._password,
                                        language='ja-JP',
                                        show_all=True
                                        )
        return text


class Translation(object):
    def __init__(self, credential_path='./credentials.json'):
        with open(credential_path, 'r') as f:
            baidu = json.load(f)['baidu']
        self._url = baidu['url']
        self._appid = baidu['appid']
        self._secretKey = baidu['secretKey']

    def translate(self, q, from_lang='auto', to_lang='zh'):
        # 为保证翻译质量，请将单次请求长度控制6000在bytes以内。（汉字约为2000个）
        salt = random.randint(32768, 65536)
        m = self._appid + q + str(salt) + self._secretKey
        m_MD5 = hashlib.md5(m.encode())
        sign = m_MD5.hexdigest()
        data = {
            'appid': self._appid,
            'q': q,
            'from': from_lang,
            'to': to_lang,
            'salt': str(salt),
            'sign': sign
        }
        data = parse.urlencode(data).encode('utf-8')
        try:
            req = request.Request(self._url, data=data)
            page = request.urlopen(req).read()
            page = page.decode('utf-8')
            result = json.loads(page)
            return result['trans_result'][0]['dst']
        except Exception as e:
            print(e)
            return None
