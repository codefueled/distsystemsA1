# Subscriber
from __future__ import unicode_literals
import zmq
import sys
import threading

class Subscriber:

    # instantiate variables and connect to broker
    def __init__(self, ip_add):
        self.count = 0
        self.full_add = "tcp://" + str(ip_add) + ":5556"
        ctx = zmq.Context()
        self.socket = ctx.socket(zmq.SUB)

        # self.socket.setsockopt(zmq.LINGER, 0)
        # self.socket.setsockopt(zmq.AFFINITY, 1)
        # self.socket.setsockopt(zmq.RCVTIMEO, 3000)

        self.socket.connect(self.full_add)
        print("Subscriber onnected to the broker")

    def register_sub(self, topics):
        topic_list = topics.split(",")
        topic_list = [topic.strip() for topic in topics.split(',')]
        for topic in topic_list:
            #subscribe to topic
            self.socket.setsockopt_string(zmq.SUBSCRIBE, topic)

    def notify(self, stop=None):
        if not None:
            while (not stop.is_set()):
                message = self.socket.recv_string()
                topic, info = message.split("||")
                print("Topic: %s. Message: %s" % (topic, info))
                self.count = self.count + 1
        else:
            message = self.socket.recv_string()
            topic, info = message.split("||")
            print("Topic: %s. Message: %s" % (topic, info))
            self.count = self.count + 1

if __name__ == '__main__':
    # handle input
    if len(sys.argv) != 3:
        print("Please provide 2 arguments as specified in the readme")
    else:
        # parse input
        topics = str(sys.argv[1])
        ip_add = sys.argv[2]

        sub = Subscriber(ip_add)
        sub.register_sub(topics)

        while True:
            sub.notify()



