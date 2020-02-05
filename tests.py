"""
TEST 1
Establish broker, 1 publisher, and 1 subscriber
Publisher provides topic = "cats" with message "tabby" and subscriber is subscribed to topic "cats"
Test ensures that the topic/message provided by the publisher travels across the broker to subscriber
"""

"""
TEST 2
Establish broker, 1 publisher, and 1 subscriber
Publisher provides topic = "cats" with message "tabby" and subscriber is subscribed to topic "dogs"
Test ensures that the topic/message provided by the publisher is recognized by broker but not published to subscriber
"""

"""
TEST 3
Establish broker, 1 publisher, and 2 subscribers
Publisher provides topic "cats" with message "tabby" and 1 subscriber is subscribed to topic 
"cats" and 1 subscriber is subscribed to topic "dogs".
Test ensures that the subscriber subscribed to "cats" is the only one that receives the message.
"""

"""
TEST 4
Establish broker, 2 publishers, and 1 subscriber
Publisher provides topic "cat" with message "tabby"  and 1 subscriber is subscribed to topic = "cats".
We then try to establish another publisher with topic = "cats".
Test ensures that the publishers with too similar topics will be rejected by the broker.
"""

"""
TEST 5
Establish broker, 1 publisher, and 1 subscriber
Publisher provides topic = "cats" with message "tabby" and  1 subscriber is subscribed to topic "cats".
Publisher then changes the message for topic "cats" to "shorthair".
Test ensures that the change in message provided by the publisher is reflected in the subscriber to "cats".
"""

"""
TEST 6
Establish broker, 3 publishers, and 4 subscribers
1 Publisher provides topic = "cats" with message "tabby" 
1 Publisher provides topic = "dogs" with message "pitbull" 
1 Publisher provides topic = "horse" with message "mustang" 
1 subscriber is subscribed to topic = "cats"
1 subscriber is subscribed to topic = "dogs"
1 subscriber is subscribed to topic = "horse"
1 subscriber is subscribed to topic = "rabbit"
Test ensures that the change the broker should see all of the publications, but the subscribers should only see
messages corresponding to their topics.
"""

"""
TEST 7
Establish broker and 1 publisher
Publisher provides topic = "cats" with message "tabby" 
Test ensures that broker will see publication regardless of there being subscribers.
"""

"""
TEST 8
Establish 1 publisher and 1 subscriber
Publisher provides topic = "cats" with message "tabby" and all subscribers are subscribed to topic "cats"
Test ensures that there is no message transfer due to lack of broker.
"""

"""
TEST 9
Establish 1 broker, 1 publisher, and 1 subscriber.
Publisher provides topic = "cats" with message "tabby" and all subscribers are subscribed to topic "cats"
After message is seen to subscriber, create another publisher with topic = "dogs" and message "hound" with corresponding
subscriber topic = "dogs".
This test ensures that publishers and subscribers can be added during anytime in the process.
"""


