import asyncio
import time
import pika, sys, os

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)



async def main1():
    print (f"started at : {time.strftime('%X')}")

    task1 = asyncio.create_task(say_after(2, "hello"))
    task2 = asyncio.create_task(say_after(4, "world"))


    await task1
    await task2

    print (f"Finshed at : {time.strftime('%X')}")


asyncio.run(main1())