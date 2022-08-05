import asyncio


acync def foo():
    for i in range(1, 11):
        print(i)
        await asyncio.sleep(1)


async def main():
    loop = async.get_event_loop()
    task - [loop.creat_task(foo()) for i in range(10)]
    for task in tasks:
        await task