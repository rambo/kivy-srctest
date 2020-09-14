"""CLI entrypoints for kivy src structure test"""
import sys
import logging

from srctest.app import SrcTestApp


LOGGER = logging.getLogger(__name__)


def srctest_cli() -> None:
    """Test Kivy with src project structure"""
    print("Hello world! from console.py")
    LOGGER.setLevel(10)

    print(" *** app init ***")
    app = SrcTestApp()

    print(" *** app run ***")
    exitcode = app.run()
    print(" *** app done ***")
    sys.exit(exitcode)
