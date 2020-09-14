"""CLI entrypoints for kivy src structure test"""
import sys
import asyncio
import logging

from srctest.app import SrcTestApp


# pylint: disable=R0801
LOGGER = logging.getLogger(__name__)


def srctest_cli() -> None:
    """Test Kivy with src project structure"""
    print("Hello world! from srctest_cli (console.py)")
    LOGGER.setLevel(10)

    print(" *** app init srctest_cli (console.py) ***")
    app = SrcTestApp()

    print(" *** app run srctest_cli (console.py) ***")
    exitcode = app.run()
    print(" *** app done srctest_cli (console.py) ***")
    sys.exit(exitcode)


def srctest_async_cli() -> None:
    """Test Kivy with src project structure (asyncio)"""
    print("Hello world! from srctest_async_cli (console.py)")
    LOGGER.setLevel(10)

    print(" *** app init srctest_async_cli (console.py) ***")
    app = SrcTestApp()

    print(" *** app async_run srctest_async_cli (console.py) ***")
    exitcode = asyncio.get_event_loop().run_until_complete(app.async_run(async_lib="asyncio"))
    print(" *** app done srctest_async_cli (console.py) ***")
    sys.exit(exitcode)
