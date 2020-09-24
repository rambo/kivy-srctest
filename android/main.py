"""buildozer entrypoint"""
import sys
import asyncio
from srctest.app import SrcTestApp


# pylint: disable=R0801
if __name__ == "__main__":
    print("Hello world! from main.py")
    print(" *** app init (main.py) ***")
    app = SrcTestApp()

    print(" *** app run (main.py) ***")
    exitcode = asyncio.get_event_loop().run_until_complete(app.async_run(async_lib="asyncio"))
    print(" *** app done (main.py) ***")
    sys.exit(exitcode)
