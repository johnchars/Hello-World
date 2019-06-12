#!/usr/bin/python

import subprocess
import rospy
args = "print.py"
result = bool(subprocess.Popen(['python', 'print.py']))

print(result)
