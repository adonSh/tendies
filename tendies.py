#!/usr/bin/env python3

"""
Are there tendies in Dewick? Now also featuring other foods and Carm.
    --Adon Shapiro
"""

import argparse
import re
import requests
import string
import sys

def parse_args(p):
    """ parses command-line arguments and returns an arguments object """
    p.add_argument('-l', '--location', metavar='LOCATION', action='store',
                   dest='location', choices=['dewick', 'Dewick', 'carm', 'Carm',
                                             'carmichael', 'Carmichael'],
                   default='dewick', help='Dewick or Carm? (Default: Dewick)')
    p.add_argument('-i', '--item', metavar='ITEM', action='store', dest='item',
                   default='chicken tenders',
                   help='What are you looking for? (Default: tendies)')
    return p.parse_args()

def main():
    """ downloads menu and searches for food; returns int """
    parser = argparse.ArgumentParser(description='Are there tendies in Dewick?')
    args = parse_args(parser)
    # Tufts' menu corresponds 11 to dewick and 9 to carm. Don't ask me why.
    location = '11' if args.location.lower() == 'dewick' else '9'
    url = 'http://menus.tufts.edu/foodpro/shortmenu.asp?locationNum=' + location
    menu = requests.get(url)
    regex = string.capwords(args.item)

    # return 0 on success, 1 on failure, 2 on error
    if menu.status_code != 200:
        print('Error: could not download menu', file=sys.stderr)
        return 2
    elif re.search(regex, menu.text) != None:
        print(regex + ' in ' + args.location.capitalize() + '!')
        return 0
    return 1

exit(main())
