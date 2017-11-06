#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: hwd 
@time: 2017-08-22 12:30 
"""
import hashlib

if __name__ == '__main__':
    m = '20151113000005349愛47122osubCEzlGjzvw8qdQc41'
    m_MD5 = hashlib.md5(m.encode())
    sign = m_MD5.hexdigest()
    print('m = ', m)
    print('sign = ', sign)
