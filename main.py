"""buildozer entrypoint"""
import sys
from srctest.app import SrcTestApp


# pylint: disable=R0801
if __name__ == "__main__":
    print("Hello world! from main.py")
    print(" *** app init (main.py) ***")
    app = SrcTestApp()

    print(" *** app run (main.py) ***")
    exitcode = app.run()
    print(" *** app done (main.py) ***")
    sys.exit(exitcode)
