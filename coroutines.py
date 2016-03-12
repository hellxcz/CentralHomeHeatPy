import types


class Coro:
    def __init__(self):
        pass

    @types.coroutine
    def run(self):

        for i in range(10):
            print("some {0}".format(i))
            yield

