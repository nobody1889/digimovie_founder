import webbrowser

import aiohttp
import asyncio


async def found_one(url) -> dict:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as answer:
                print(f'success url : {url}')
                return {answer.status: url}
    except aiohttp.client_exceptions.ClientConnectorError:
        print(f'field url : {url}')
        return {404: url}


async def found_all():  # found the correct link of now that's up
    print('try to find the current link . . .')
    # site_name = "https://digimovie54.top"
    task = [found_one(f"https://digimovie{i}.top") for i in range(1, 100)]
    status = await asyncio.gather(*task)
    return status


async def main():  # mian function to run
    status_dic = await found_all()
    for i in status_dic:
        print(i)
    # url = status_dic[200]
    # print(f"current url is : {url}")
    # webbrowser.open_new_tab(url)
    loop.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print('interrupted')
        loop.close()
