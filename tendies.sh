#!/bin/sh

url="http://menus.tufts.edu/foodpro/shortmenu.asp?locationNum=11"
menu=`curl "$url" 2> /dev/null`

if echo "$menu" | grep -q "Chicken Tenders"; then
  notify-send "Tendies in Dewick!"
fi
