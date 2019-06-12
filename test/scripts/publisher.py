#!/usr/bin/python
import rospy
import subprocess
from test.msg import result

def publisher():
    pub = rospy.Publisher('result', result, queue_size=10)
    rospy.init_node('test')
    rate = rospy.Rate(10)
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

