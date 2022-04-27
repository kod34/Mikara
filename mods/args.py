import argparse

parser = argparse.ArgumentParser()
requiredNamed = parser.add_argument_group('required named arguments')

requiredNamed.add_argument("-o", "--output", dest="output", help="wordlist path")
requiredNamed.add_argument("-t", "--type", dest="type", help="list type (simple, moderate, complex)")

args = parser.parse_args()

wordlist = args.output
type = args.type
