import argparse
import os, sys

argparser = argparse.ArgumentParser(description=f"Solution to {os.path.basename(__file__)} of the advent of code")
argparser.add_argument( 'infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
argparser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)

################################################
#                                              #
#       Test data here                         #
#                                              #
################################################




################################################
#                                              #
#       Solution here                          #
#                                              #
################################################



