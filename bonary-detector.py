#!/usr/bin/env python3

import os, sys
from time import time, sleep
from ghstats import ghstats
import blinkt

print('Press Ctrl+C to quit.')

def blockPrint():
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    sys.stdout = sys.__stdout__

#downloads = ghstats.download_stats("RetroPie", "RetroPie-Setup", None, True, ghstats.get_env_token(), True)
print('Total Bonaries Downloaded:')
downloadtotal = ghstats.main_cli(["RetroPie", "RetroPie-Setup", "-q"])

try:
  while True:
    sleep(60 - time() %60)
    blockPrint()
    newdownloadtotal = ghstats.main_cli(["RetroPie", "RetroPie-Setup", "-q"])
    enablePrint()
    difference = newdownloadtotal - downloadtotal
    for i in range(difference):
      blinkt.set_all(255, 0, 0, 1)
      blinkt.show()
      sleep(0.20)
      blinkt.set_all(0,0,0,0)
      blinkt.show()
      sleep(0.20)
    print(difference, 'New Bonarie(s) Downloaded!')
    print(newdownloadtotal, 'Total Bonaries Downloaded')
    downloadtotal = difference + downloadtotal
except KeyboardInterrupt:
    print('\n')
