
import zmq
import sys
import random
import string
import time

context = zmq.Context()

def register_sub(topicname):
    #  Socket to talk to server
    print("Connecting to the broker…")
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5556")
    socket.setsockopt_string(zmq.SUBSCRIBE, topicname)
    print("Connected to the broker")

    # Process 5 updates
    while True:
        time.sleep(1)
        message = socket.recv_string()
        time.sleep(1)
        #my_topic, messagedata = message.split()
        print("Received message topic: with message %s" % message)


if __name__ == '__main__':
    #Handle input
    if len(sys.argv) != 2:
        print("Please re-run and provide one topic as the input argument")
    else:
        topic = str(sys.argv[1])

    #Register subscriber
    register_sub(topic)

