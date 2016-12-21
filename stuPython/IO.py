#!/usr/bin/env python
# --*-- coding:utf-8 --*--
def readDate(path=''):
    with open(path,'rb') as f:
        date=f.read()
    return date
def readDates(path):
    try:
        with open(path,'rb') as i:
            date=i.read()
        return date
    except IOError as e:
        print e
        with open('/root/allen/stuPython/IO.py','r') as i:
            date=i.read()
        return date

path=raw_input('请输入路径:')
date=readDates(path)
print date
