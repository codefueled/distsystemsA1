# Publisher
import zmq
import time
import sys
import string
import random

# Initialize the sockets
ctx = zmq.Context()
sock_pub = ctx.socket(zmq.PUB)
sock_pub.connect("tcp://localhost:1234")

# NOTE - CURRENTLY NOT USING ID
def register_pub(topic, id):
    # format for registering publisher is "REGISTER||topic,id"
    msg = "REGISTER||" + str(topic) + "||" + str(id)
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
    if len(sys.argv) != 2:
        print("Please re-run and provide one topic as the input argument")
    elif "," in sys.argv[1]:
        print("Please re-run and remove any '||' found in the topic name")
    elif "REGISTER" in sys.argv[1]:
        print("Please re-run and remove any occurances of 'REGISTER' found in the topic name")
    else:
        topic = sys.argv[1]

        # generate id
        id = "" .join(random.choices(string.ascii_lowercase, k=8))

        # register publisher
        register_pub(topic, id)

        # use a wait routine, and wait for information associated with the routne
        while True:
            info = input("Input information about your topic and press enter to publish!\n")
            print("success!")
            publish(topic, info)

        sock.close()
        ctx.term()