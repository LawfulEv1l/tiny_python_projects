#!/usr/bin/env python3
"""
Author:  Federico Martinez
Purpose: Say hello
"""
#print('hello World!')
import argparse

parser = argparse.ArgumentParser(description='Say Hello')
parser.add_argument('-n',
                    '--name',
                    metavar="name",
                    default='World',
                    help='name to greet')
args = parser.parse_args()
name = args.name

print("Hello, " + name + '!')