#!/usr/bin/env python
# --*-- coding:utf-8 --*--
def logs(test):
    def funs(func):
        def wrap(*args,**kw):
            print('call %s is %s' % (func.__name__,test))
            s=func(*args,**kw)
            print('ebd')
            return s
        return wrap
    return funs

def log(func):
    def wrap(*args,**kw):
        print('call %s' % func.__name__)
        return func(*args,**kw)
    return wrap

@logs('你好')
def now():
    print('2016-12-1')

now()
