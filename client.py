# Subscriber
from __future__ import unicode_literals
import zmq
import sys

context = zmq.Context()
#  Socket to talk to server
print("Connecting to the broker…")
socket = context.socket(zmq.SUB)

def register_sub(topicname):
    socket.setsockopt_string(zmq.SUBSCRIBE, topicname)

def notify():
    while True:
        message = socket.recv_string()
        topic, info = message.split("||")
        print("Topic: %s. Message: %s" % (topic, info))

if __name__ == '__main__':
    # handle input
    if len(sys.argv) != 3:
        print("Please provide 2 arguments as specified in the readme")
    else:
        # parse topics
        topics = str(sys.argv[1])
        topic_list = topics.split(",")
        topic_list = [topic.strip() for topic in topics.split(',')]

        # connect to broker
        ip_add = sys.argv[2]
        full_add = "tcp://" + str(ip_add) + ":5556"
        socket.connect(full_add)
        print("Connected to the broker")

        for topic in topic_list:
            #subscribe to topic
            register_sub(topic)

        # listen for updates
        notify()

