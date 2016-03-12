import unittest

from rx import Observable, Observer


class MyTestCase(unittest.TestCase):
    def test_subscribe(self):
        xs = Observable.from_iterable(range(10))
        # d = xs.subscribe(MyObserver())
        d = xs.subscribe(lambda t: print(t),
                         lambda e: print(e),
                         lambda: print("done"))

    def test_timer(self):
        timer = Observable.timer(0, 200)
        subscr = timer.subscribe(
                lambda t: print(t),
                lambda e: print(e),
                lambda: print("done")
        )


if __name__ == '__main__':
    unittest.main()


class MyObserver(Observer):
    def on_next(self, x):
        print("Got: %s" % x)

    def on_error(self, e):
        print("Got error: %s" % e)

    def on_completed(self):
        print("Sequence completed")
