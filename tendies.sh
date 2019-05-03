#!/bin/sh

URL="http://menus.tufts.edu/foodpro/shortmenu.asp?locationNum=11"
MENU=`curl "$URL" 2> /dev/null`

if echo "$MENU" | grep -E "[cC]hicken [tT]enders" > /dev/null 2>&1; then
  notify-send "Tendies in Dewick!"
fi
