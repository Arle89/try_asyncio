import asyncio
import time
import pika

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)



async def main():
    print (f"started at : {time.strftime('%X')}")

    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))


    await task1
    await task2

    print (f"Finshed at : {time.strftime('%X')}")


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue = 'hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello world!')
print ('Hello world')
connection.close()


asyncio.run(main())