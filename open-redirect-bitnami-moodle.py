#!/usr/bin/env python3

from requests import *
import sys
import json

def print_usage():
    s='''
Usage:
\t./'''+sys.argv[0]+''' <URL/Domain/IP>  
\texamples:
\t\t->  ./'''+sys.argv[0]+''' 192.168.161.178
\t\t->  ./'''+sys.argv[0]+''' mymoodle.domain.com
\t\t->  ./'''+sys.argv[0]+''' http://mymoodle.domain.com/
'''
    print(s)
    exit()

def argparser():
    if '-h' in sys.argv or '--help' in sys.argv:
        print_usage()
        exit()
    if len(sys.argv)!=2:
        print_usage()
        exit()


argparser()

try:
    url = sys.argv[1]
    if 'http' not in url:
        url='http://'+url

    url+='/my/'
    headers = {'Host': 'google.com'}
    s=Session()
    r=s.get(url,headers=headers)
    
    if  'google.com' in r.url:    # if it's google.com, then it is vulnerable!
        print("\n\033[32;1m-> Vulnerable!\033[0m\n")
    else:
        print("\n\033[31;1m-> Not Vulnerable...\033[0m\n")
except:
    print("\n\033[31;1m-> Some error occurred... check connection or argument\033[0m\n")
    exit()