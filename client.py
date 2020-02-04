# Subscriber
import zmq
import sys
import random
import string
import time

context = zmq.Context()

#  Socket to talk to server
print("Connecting to the broker…")
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5556")
print("Connected to the broker")

def register_sub(topicname):
    socket.setsockopt_string(zmq.SUBSCRIBE, topicname)

def notify():
    while True:
        message = socket.recv_string()
        print("Received message topic: with message %s" % message)

if __name__ == '__main__':
    #Handle input
    if len(sys.argv) != 2:
        print("Please re-run and provide a string containing the list of topics (separated by a comma) as the input argument")
    else:
        topics = str(sys.argv[1])
        topic_list = topics.split(",")
        topic_list = [topic.strip() for topic in topics.split(',')]
        print(topic_list)

        for topic in topic_list:
            #Register subscriber
            register_sub(topic)

        notify()

