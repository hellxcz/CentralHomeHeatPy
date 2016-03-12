from settings import nodeTimer

class Node:
    def __init__(self, code: str):
        self.code = code
        self.run()

    def run(self):
        nodeTimer.subscribe(lambda t: self._run())

    def _run(self):
        print("run of ", self.code)


class Room:
    def __init__(self, node: Node, name: str):
        self.node = node
        self.name = name

    def get_current_temperature(self):
        self.name
        return Temperature(0)


class Temperature:
    def __init__(self, value):
        self.value = value


