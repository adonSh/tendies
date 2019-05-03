#!/usr/bin/env python3

import os
import urllib.request

url = 'http://menus.tufts.edu/foodpro/shortmenu.asp?locationNum=11'

with urllib.request.urlopen(url) as menu:
    if 'Chicken Tenders' in menu.read().decode('utf-8'):
        os.system('notify-send "Tendies in Dewick!"')
