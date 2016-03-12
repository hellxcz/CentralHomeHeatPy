import rx
from rx import Observable, subjects

from InfoReader import DummyInfoReader

global mainTimer, nodeTimer, eventBus, infoReader

mainTimer = Observable.timer(0, 200)
nodeTimer = Observable.timer(0, 10000)
eventBus = rx.subjects.Subject()

infoReader = DummyInfoReader(eventBus)