#!/usr/bin/env python3
#say hello
#print('hello World!')

import argparse

parser = argparse.ArgumentParser(description= 'Say Hello')
parser.add_argument('name', help='name to greet')
args = parser.parse_args()
name = args.name

print( "Hello,"+ name + '!' )
