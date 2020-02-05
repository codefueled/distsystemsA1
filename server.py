# Publisher
from __future__ import unicode_literals
import zmq
import time
import sys

# Initialize the socket
ctx = zmq.Context()
sock_pub = ctx.socket(zmq.PUB)

def register_pub(topic):
    # format for registering publisher is "REGISTER||topic"
    msg = "REGISTER||" + str(topic) + "||"
    time.sleep(1)
    sock_pub.send_string(msg)
    return True

def publish(topic, info):
    # format for published string is "topic||info"
    msg = str(topic) + "||" + str(info)
    sock_pub.send_string(msg)
    return True

if __name__ == '__main__':
    # handle input
    if len(sys.argv) != 3:
        print("Please re-run and provide two inputs")
    elif "," in sys.argv[1]:
        print("Please re-run and remove any '||' found in the topic name")
    elif "REGISTER" in sys.argv[1]:
        print("Please re-run and remove any occurances of 'REGISTER' found in the topic name")
    else:
        topic = sys.argv[1]
        ip_add = sys.argv[2]
        full_add = "tcp://" + str(ip_add) + ":1234"

        # connnect to broker
        sock_pub.connect(full_add)

        # register publisher
        register_pub(topic)

        # wait for inputted information to publish
        while True:
            info = input("Input information about your topic and press enter to publish!\n")
            publish(topic, info)
            print("Success!")

        sock.close()
        ctx.term()