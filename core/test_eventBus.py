import unittest
from unittest import TestCase

from eventBus import EventBus, Message


class TestEventBus(TestCase):
    def test__subscribe(self):

        called = 0

        def callback(msg:Message):
            nonlocal called

            print("topic {0}, payload {1}".format(msg.topic, msg.payload))
            called += 1

        eventBus = EventBus()
        eventBus.subscribe("hello", callback)
        eventBus.subscribe("hello2", callback)

        eventBus.publish(message=Message("hello", "payload"))
        eventBus.publish(message=Message("hello2", "payload2"))

        self.assertTrue(called == 2)
