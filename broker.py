# Broker
from __future__ import unicode_literals
import zmq
import sys

context = zmq.Context()
sub_socket = context.socket(zmq.SUB)
pub_socket = context.socket(zmq.PUB)
current_topics = []


if __name__ == '__main__':
    ip_add = sys.argv[1]
    full_add1 = "tcp://" + str(ip_add) + ":1234"
    full_add2 = "tcp://" + str(ip_add) + ":5556"
    # bind to ip/ports
    sub_socket.bind(full_add1)
    sub_socket.subscribe("")
    pub_socket.bind(full_add2)

    while True:
        message = sub_socket.recv_string()
        print(message)
        topic, info = message.split("||")
        error_flag = False
        for curr_topic in current_topics:
            if topic.startswith(curr_topic):
                print("Topic is too similar to topic of another publisher, choose another")
                error_flag = True
        if not error_flag:
            current_topics.append(topic)
            print("Received: %s" % message)
            pub_socket.send_string(message)