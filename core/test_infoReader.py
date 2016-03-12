from unittest import TestCase

from InfoReader import DummyInfoReader, InfoMessage
from settings import eventBus
from threading import Thread, current_thread


class TestInfoReader(TestCase):
    def setUp(self):
        self.testee = DummyInfoReader(eventBus)

    def test__Start__Stop(self):
        self.testee.start()
        self.testee.stop()

    def test__DummyInfoReader(self):
        self.testee.start()

        count = 0

        def subscriber(msg: InfoMessage):
            nonlocal count
            count += 1

            currentThread = current_thread()

            print(msg.payload, " on ", currentThread.name, ", ", currentThread.ident)

            if count == 10:
                subscription.dispose()
                self.testee.stop()

        subscription = eventBus\
            .subscribe(subscriber)

        print("running test")