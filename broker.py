# Broker
import time
import zmq
import sys

context = zmq.Context()
sub_socket = context.socket(zmq.SUB)


pub_socket = context.socket(zmq.PUB)


if __name__ == '__main__':
    ip_add = sys.argv[1]
    full_add1 = "tcp://" + str(ip_add) + ":1234"
    full_add2 = "tcp://" + str(ip_add) + ":5556"
    sub_socket.bind(full_add1)
    sub_socket.subscribe("")
    pub_socket.bind(full_add2)

    while True:
        #  Wait for next request from client
        message = sub_socket.recv_string()
        print("Received: %s" % message)

        ### DONT ALLOW TOPICS BEGINNING WITH THE SAME NAME
        pub_socket.send_string(message)