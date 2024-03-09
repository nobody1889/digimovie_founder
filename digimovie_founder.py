import signal
import webbrowser

import aiohttp
import asyncio


# import signal
# import logging


async def found_one(url: str) -> None:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as answer:
                print(f'success url : {url}')
                webbrowser.open_new(url)
    except aiohttp.client_exceptions.ClientConnectorError:
        await asyncio.sleep(180)


def shutdown():
    tasks0 = []
    for task in asyncio.all_tasks(loop):
        task.cancel()
        tasks0.append(task)
    result = asyncio.gather(*tasks0)
    print(f'result: {result}')
    loop.stop()


async def found_all() -> set:  # found the correct link of now which is up
    print('try to find the current link . . .')
    # "https://digimovie54.top"
    tasks = [asyncio.create_task(found_one(f"https://digimovie{i}.top")) for i in range(1, 100)]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED, timeout=120)
    print(done)
    shutdown()
    return done


async def main() -> None:  # mian function to run
    await found_all()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGINT, shutdown)
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print('interrupted')
        shutdown()
    except asyncio.exceptions.CancelledError:
        print('cancelled')


