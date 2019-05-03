#!/usr/bin/env python3

import argparse
import os
import re
import requests
import sys

def parse_args(p):
    """ parses command-line arguments and returns an arguments object """
    p.add_argument('--location', '-l', metavar='LOCATION', action='store',
                   dest='location', choices=['dewick', 'carm'],
                   default='dewick', help='Dewick or Carm?')
    return p.parse_args()

parser = argparse.ArgumentParser(description='Are there tendies in Dewick?')
args = parse_args(parser)
location = '11' if args.location == 'dewick' else '9'
url = 'http://menus.tufts.edu/foodpro/shortmenu.asp?locationNum=' + location
menu = requests.get(url)
regex = '[cC]hicken [tT]enders'

if menu.status_code != 200:
    print('Error: could not download menu', file=sys.stderr)
elif re.search(regex, menu.text) != None:
    os.system('notify-send "Tendies in Dewick!"')
