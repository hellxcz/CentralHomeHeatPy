import rx
from rx import subjects


class Message:
    def __init__(self, topic: str, payload):
        self.topic = topic
        self.payload = payload


class EventBus:
    def __init__(self):
        self.subject = rx.subjects.Subject()

    def publish(self, message: Message):
        self.subject.on_next(message)

    def _subscribe(self,msg:Message, topic: str, func=None):
        if msg.topic == topic:
            func(msg)

    def subscribe(self, topic: str, func=None):
        self.subject.subscribe(lambda msg: self._subscribe(msg, topic, func))