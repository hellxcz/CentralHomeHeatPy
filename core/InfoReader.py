from rx import Observable
from rx.subjects import Subject

from eventBus import Message


class InfoMessage(Message):
    def __init__(self, payload:Temperature):
        super(InfoMessage, self).__init__("InfoMessage", payload)


class InfoReader:
    def __init__(self, eventbus: Subject):
        self.eventBus = eventbus
        self.initialized = True
        self.started = False
        self._runTimer = Observable.timer(0, 10000)
        self._runSubscription = None

    def start(self):
        self._runSubscription = self._runTimer.subscribe(self._run)
        self.started = True

    def stop(self):
        self._runSubscription.dispose()
        self.started = False

    def _run(self, x):
        # TODO
        print('inforeader RUN')
        self._read_info()

    def _read_info(self):
        pass


class DummyInfoReader(InfoReader):
    def _read_info(self):
        message = InfoMessage(10)
        self.eventBus.on_next(message)
        # super(DummyInfoReader, self)._read_info()
