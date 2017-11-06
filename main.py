#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: hwd 
@time: 2017-08-22 15:05 
"""

import sys
import subprocess

import gflags

from util import SpeechRecognition, Translation


def extract_audio(input_path, output_path):
    command = ['ffmpeg',
               '-i', input_path,
               '-vn',
               output_path]
    p = subprocess.call(command, shell=True)
    return p


def main(flags):
    sr = SpeechRecognition()
    tr = Translation()
    print('extract audio...')
    # extract_audio('C:/Users/hwd/Desktop/1.m4v', 'C:/Users/hwd/Desktop/1.wav')
    extract_audio(flags.input_path, flags.output_path)
    print('transform speech to text...')
    results = sr.speech_to_text(flags.output_path)
    print('translating...')
    subtitles = []
    for result in results:
        subtitle = tr.translate(result['text'], from_lang=flags.from_lang, to_lang=flags.to_lang)
        if subtitle is not None:
            subtitles.append({'time': result['time'], 'text': subtitle})
    print('generate subtitles...')


if __name__ == '__main__':
    global_flags = gflags.FLAGS
    gflags.DEFINE_boolean('help', False, 'Show this help.')
    gflags.DEFINE_string('input_path', '', 'video file path.')
    gflags.DEFINE_string('output_path', '', 'audio file path.')
    gflags.DEFINE_string('from_lang', 'auto', 'source language.')
    gflags.DEFINE_string('to_lang', 'zh', 'destination language.')
    global_flags(sys.argv)
    if global_flags.help:
        print(global_flags.main_module_help())
        exit(0)
    exit(main(global_flags))
