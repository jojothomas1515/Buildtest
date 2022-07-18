import asyncio


async def function1():
    for i in range(20):
        if (i == 10):
            print("now")
            await asyncio.sleep(5)
        await asyncio.sleep(.5)
        print("hello from function 1")


async def function2():
    for j in range(10):
        print('wording')
        await asyncio.sleep(1)


async def main():

    loop = asyncio.get_running_loop()
    task = loop.create_task(function1())
    task2 = loop.create_task(function2())

    await task
    await task2


if __name__ == "__main__":
    asyncio.run(main())
