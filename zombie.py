#!/usr/bin/env python2
# -*- coding: utf8 -*-
import subprocess
import time
import threading

proc = subprocess.Popen(['ls','-l'])
time.sleep(5)
proc.communicate()
time.sleep(5)
