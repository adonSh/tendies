#!/usr/bin/env python3

import os
import re
import requests
import sys

url = 'http://menus.tufts.edu/foodpro/shortmenu.asp?locationNum=11'
menu = requests.get(url)

if menu.status_code != 200:
    print('Error: could not download menu', file=sys.stderr)
elif re.search('[cC]hicken [tT]enders', menu.text) != None:
    os.system('notify-send "Tendies in Dewick!"')
