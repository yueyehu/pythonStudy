import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbose",help="increase output verbosity")

args = parser.parse_args()

if args.verbose:
	print "verbosity turned on"
