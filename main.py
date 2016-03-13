# from core.model import Node, Room
import asyncio

from coroutines import MainCoroutine


# def create_and_run_model():
#     rooms = [Room(Node("123"), "pracovna"),
#              Room(Node("312"), "obyvak")
#              ]

async def start_main_coroutine():
    coroutine = MainCoroutine()

    await coroutine.run()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_main_coroutine())
    loop.close()

