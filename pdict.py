''' Dictionaries in readable format

usage: pdict.detail(obj, level=0, space=3, metric=[0], sign="-")

>>> import pdict
>>> myDict = {12.98675:  [{1:3}], "test2": [(1,{1:'qrest1',2:'qrest2'}), (3,4)], }
>>> pdict.displ(myDict, space=5) 

optional arguments:
    -h, --help  show this help message and exit
    space=3     determine what width to use for the levels in detail function 
    level=0     determine starting level 

Description:
This file can be used as a module with 2 methods: detail() and summary()
The file can be used also as a stand alone code for further exploring dicts
'''

# ---- [ INFO ]--------------------------------------------------------------------------
# Module to make it easy to read dictionaries on a terminal
#   
# Goal: provide a dict to a definition in the module to print it out
# For use in python 2, add; 
#         from __future__ import print_function
# Python version: >= python 3 
# ----------------------------------------------------------------------------------------

# ---- [ INITIALIZE & IMPORTS ] ----------------------------------------------------------
__author__ = 'Your Name'
__pyversion__ = '3.0.0'
from os import system
system('clear')                                             # clear screen before output
from time import time, localtime, perf_counter, asctime     # import only what is needed
from sys import version_info

def decorator_main(func):
    def wrap():
        if ".".join(map(str, version_info[:3])) < __pyversion__:
            print(f'Use Python vs {__pyversion__} for best result')
        starttime = perf_counter()
        print(f'[ Code made by: {__author__:<20}                   {asctime(localtime(time()))} ]')
        print(f'{"":-<81}\n\n')

        func()

        print(f'\n\n{"":-<81}')
        print(f'[ END                              code total time costs: {perf_counter() - starttime} ] \n\n')
    return wrap


# ---- [ CODE BLOCK ] --------------------------------------------------------------------------

# ---- [ FUNCTIONS ] ---------------------------------------------------------------------------
# ---- [ whatInstance: returns type of object in format '<type>  ==> <object>'
def whatInstance(obj):
    if isinstance(obj, dict):
        return f'dict  => {obj}'
    elif isinstance(obj, list):
        return f'list  => {obj}'
    elif isinstance(obj, tuple):
        return f'tuple => {obj}'
    elif isinstance(obj, int):
        return f'int   => {obj}'
    elif isinstance(obj, str):
        return f'str   => {obj}'
    elif isinstance(obj, float):
        return f'float => {obj}'
    elif isinstance(obj, bool):
        return f'bool  => {obj}'
    else:
        return f'object > {obj}'

def wIn(obj):
    return f'{obj} = {"dict" if isinstance(obj, dict) else "list" if isinstance(obj, list) else "nor dict or list"}'

def detail(obj, level=0, space=3, metric=[0], sign="-"):
    if level == 0 and metric == [0]:
        metric = 1
        # listObject = [name for name in namespace if namespace[name] is obj]
        print(f'Dictionary made readable')
        print(f'{"":.<81}')
        print(f'dict = {obj}')
        print(f'level: key_type => key  , value_type => value')
        print(f'{"":.<81}\n')
    if isinstance(obj, dict):
        for k, v in obj.items():
            # k only be bool, str, int, float, tuple
            print(level*(sign*(space-1)) + level*(' '*2) + f'{level}: {whatInstance(k)}\t,  {whatInstance(v)}')

            if isinstance(v, dict):
                detail(v, level+1, space)
            if isinstance(v, list):
                for e in v:
                    if isinstance(e, dict):
                        detail(e, level+1, space)
                    if isinstance(e, tuple):
                        detail(e, level+1, space)
    
    if isinstance(obj, tuple):
        print(level*(sign*(space-1)) + level*(' '*2) + f'{level}: {whatInstance(obj)}')
        if isinstance(obj[0], dict):
            detail(obj[0], level+1, space)
        if isinstance(obj[0], tuple):
            detail(obj[0], level+1, space)
        if isinstance(obj[1], dict):
            detail(obj[1], level+1, space)
        if isinstance(obj[1], tuple):
            detail(obj[1], level+1, space)  

def summary(obj, level=0, space=3, metric=[0], sign="-"):
    if level == 0 and metric == [0]:
        metric = 1
        print(f'Display dictionary; method 2 = summary')
        print(f'{"":.<81}')
        print(f'The dictionary looks like {obj}')
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, dict):
                print(f'found dictionary on level {v}')
                summary(v, level+1, space)
            if isinstance(v, list):
                for e in v:
                    if isinstance(e, dict):
                        summary(e, level+1, space)
                    if isinstance(e, tuple):
                        summary(e, level+1, space)
    if isinstance(obj, tuple):
        if isinstance(obj[0], dict):  
            print(f'found dictionary on level {obj[0]}')
            summary(obj[0], level+1, space,)
        if isinstance(obj[1], dict):  
            print(f'found dictionary on level {obj[1]}')
            summary(obj[1], level+1, space)
                              
@decorator_main
def main():
    # ---- test dictionaries
    dict_simple = {'A':{'speed':70,'color':2},'B':{'speed':60,'color':3}}
    dict_complex = {"test":  [{1:3}], 
                    "test2": [(1,{1:'qrest1',2:'qrest2'}), (3,4)],
                    "test3": {(1,2):['abc', 'def', 'ghi'],  (4,5):'def',  "nakje":{1:'nak',2:'naque'}},
                    "test4": 900,
                    }
    dict_complex = {12.98675:  [{1:3}], "test2": [(1,{1:'qrest1',2:'qrest2'}), (3,4)], }
    displ(dict_complex, 0, 4, [0])       
    

if __name__ == '__main__': main()

# ---- [ END CODE BLOCK ] --------------------------------------------------------------------------

