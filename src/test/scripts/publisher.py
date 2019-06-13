#!/usr/bin/python
import rospy
import subprocess
import os
import sys
from test.msg import result

def search(path,name):
	path = subprocess.Popen(["locate", "scripts/print.py"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	(o,e) = path.communicate()
	print(o)
	o.replace("\n","")
	print(os.path.dirname(o))
	o = os.path.dirname(o)
	return o

def publisher():
    pub = rospy.Publisher('result', result, queue_size=10)
    rospy.init_node('test')
    rate = rospy.Rate(10)
    path = search('/home','scripts/print.py')
    print(path)
    os.chdir(path)
    os.system("pwd")
    while not rospy.is_shutdown():
        r = bool(subprocess.Popen(['python', 'print.py']))
        rospy.loginfo(r)
        pub.publish(r)
        rate.sleep()

if __name__ == "__main__":
    try :
        publisher()
    except rospy.ROSInterruptException:
        pass

