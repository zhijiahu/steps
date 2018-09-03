import asyncio
from aiohttp import web


async def handler(request):
    return web.Response(text="OK")


async def main(loop):
    server = web.Server(handler)
    port = 9001
    await loop.create_server(server, "127.0.0.1", port)
    print("======= Serving on http://127.0.0.1:{}/ ======".format(port))

    # pause here for very long time by serving HTTP requests and
    # waiting for keyboard interruption
    await asyncio.sleep(100*3600)

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(main(loop))
except KeyboardInterrupt:
    pass
loop.close()
