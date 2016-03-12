# from core.model import Node, Room
import asyncio

from coroutines import Coro


# def create_and_run_model():
#     rooms = [Room(Node("123"), "pracovna"),
#              Room(Node("312"), "obyvak")
#              ]

async def play_with_coroutines():
    coroutine = Coro()

    await coroutine.run()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(play_with_coroutines())
    loop.close()

