#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import argparse
import yaml

class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

def handle_hello(args):
    print(f'Hello World : {bcolors.HEADER}{args.v1}{bcolors.ENDC}')
    print(f'Hello World : {bcolors.OKBLUE}{args.v1}{bcolors.ENDC}')
    print(f'Hello World : {bcolors.OKGREEN}{args.v1}{bcolors.ENDC}')
    print(f'Hello World : {bcolors.WARNING}{args.v1}{bcolors.ENDC}')
    print(f'Hello World : {bcolors.FAIL}{args.v1}{bcolors.ENDC}')
    print(f'Hello World : {bcolors.BOLD}{args.v1}{bcolors.ENDC}')
    print(f'Hello World : {bcolors.UNDERLINE}{args.v1}{bcolors.ENDC}')

def handle_login(args):
    pass

def gen_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--env', default='.env', help='env config file.')

    subs = parser.add_subparsers(required=True)

    sub = subs.add_parser('hello', help='Print colors "Hello World"')
    sub.add_argument('v1', help='v1 value.')
    sub.set_defaults(func=handle_hello)
 
    sub = subs.add_parser('login', help='Login server and get "access_token" and "refresh_token".')
    sub.add_argument('email', help='Account email')
    sub.add_argument('passworld', help='Account password')
    sub.set_defaults(func=handle_login)
  

    return parser

def main():
    parser = gen_parser()
    result = parser.parse_args(sys.argv[1:])
    result.func(result)

if __name__ == '__main__':
    main()
