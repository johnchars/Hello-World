#!/usr/bin/python
import rospy
from test.msg import result
<<<<<<< HEAD:src/test/scripts/subscriber.py
from xbot_talker.srv import chat, play
=======
from talker.srv import chat, play
>>>>>>> ed6295d44982de2b1e36436f4b4ecb9693a8aa2a:test/scripts/subscriber.py

def chat_CB(data):
    #print("successful")
    rospy.loginfo(data.result)
    if True == data.result:
        communicate.chat_srv(True)
    else :
        communicate.play_srv(False, 1, "", "error")

class communicate():
    #def __init__(self):
        chat_srv = rospy.ServiceProxy('/chat', chat)
        play_srv = rospy.ServiceProxy('/play', play)

def subscriber():
    rospy.init_node('test_sub')
    rospy.Subscriber("result", result, chat_CB)
    rospy.spin()

if __name__ == "__main__":
    try :
        subscriber()
    except rospy.ROSInterruptException():
        pass
