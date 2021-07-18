from asyncio import get_event_loop

from rfxcom.transport import AsyncioTransport


def collect(dev_name, callbacks):

    loop = get_event_loop()

    try:

        AsyncioTransport(dev_name, loop, callbacks=callbacks)
        loop.run_forever()

    finally:
        loop.close()
