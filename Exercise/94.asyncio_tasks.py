#! /usr/bin/env python3
# -*- coding : utf-8 -*-

import asyncio
import threading

async def hello():
    print('Hello world!(%s)' % threading.current_thread())
    await asyncio.sleep(1)
    print('Hello again!(%s)' % threading.current_thread())

loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# Hello world!(<_MainThread(MainThread, started 24040)>)
# Hello world!(<_MainThread(MainThread, started 24040)>)
# Hello again!(<_MainThread(MainThread, started 24040)>)
# Hello again!(<_MainThread(MainThread, started 24040)>)