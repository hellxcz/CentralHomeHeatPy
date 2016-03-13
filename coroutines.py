import types

import time
from queue import Queue

class CoroutineTask:
    def __init__(self, call, reEnqueue:bool = False):
        self.reEnqueue = reEnqueue
        self._call = call

    async def run(self):
        await self._task()


class MainCoroutine:
    def __init__(self):
        self.running = True
        self._tasks = Queue()

    def addTask(self, task: CoroutineTask):
        self._tasks.put(task)

    @types.coroutine
    def run(self):
        while self.running:
            task = self._tasks.get()
            # if task is CoroutineTask
            yield task.run()
            if task.reEnqueue:
                self.addTask(task)


class CoroutineTimer:
    def __init__(self, delay: int, mainCoroutine: MainCoroutine, call):
        self.mainCoroutine = mainCoroutine
        self.call = call
        self.delay = delay
        self.running = True

    @types.coroutine
    def run(self):
        while self.running:
            time.sleep(self.delay)
            self.mainCoroutine.addTask(
                CoroutineTask(self.call)
            )
            yield

    def stop(self):
        self.running = False



