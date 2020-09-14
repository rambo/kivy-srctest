"""buildozer entrypoint"""
import sys
from srctest.app import SrcTestApp

if __name__ == "__main__":
    print("Hello world! from main.py")
    print(" *** app init ***")
    app = SrcTestApp()

    print(" *** app run ***")
    exitcode = app.run()
    print(" *** app done ***")
    sys.exit(exitcode)
