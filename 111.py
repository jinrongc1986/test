#!/usr/bin/python
#-*- coding:utf-8 -*-
def mymap(func,*seqs):
    res=[]
    for args in zip(*seqs):
        res.append(func(*args))
    return res

#print(mymap(abs,[1,-2,3,-4,-5]))

def myzip3(*args):
    iters=list(map(iter,args))
    while iters:
        res=[next(i) for i in iters]
        yield tuple(res)
#print(list(myzip3('abc','lmnop')))

def myzip2(*args):
    iters=map(iter,args)
    while iters:
        res=[next(i) for i in iters]
        yield tuple(res)
print(list(myzip2('abc','lmnop')))
