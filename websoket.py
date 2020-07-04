import asyncio
import datetime
import random
import websockets
from gpiozero import CPUTemperature



async def loop(websocket, path):
    while True:
        cpu = CPUTemperature()

        await websocket.send(cpu.temperature)
        await asyncio.sleep(1000)

start_server = websockets.serve(loop, '0.0.0.0', 4001)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
