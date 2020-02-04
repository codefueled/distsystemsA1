# Broker
import time
import zmq

context = zmq.Context()
sub_socket = context.socket(zmq.SUB)
sub_socket.bind("tcp://127.0.0.1:1234")
sub_socket.subscribe("")

pub_socket = context.socket(zmq.PUB)
pub_socket.bind("tcp://*:5556")
while True:
    #  Wait for next request from client
    message = sub_socket.recv_string()
    print("Received request: %s" % message)
    #  Do some 'work'
    #my_topic, messagedata = message.split("||")
    pub_socket.send_string(message)