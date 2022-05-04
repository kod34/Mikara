import argparse
import sys
from mods.colors import color

parser = argparse.ArgumentParser()
requiredNamed = parser.add_argument_group('required named arguments')

requiredNamed.add_argument("-o", dest="output", help="wordlist path")
requiredNamed.add_argument("-t", dest="type", help="list type (simple, moderate, complex)")
requiredNamed.add_argument("-s", dest="size", help="minimum word size")

args = parser.parse_args()

wordlist = args.output
type = args.type
size = args.size
