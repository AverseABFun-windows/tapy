"""The messaging/error components of tapy."""
from inspect import FrameInfo
import inspect

from color import colored

def no_origin():
    """The no origin mode of logging."""
    return [FrameInfo('',0,'','',0,0),FrameInfo('',0,'','',0,0)]
origin = inspect.stack


def setinfomode(mode):
    """Set the info mode of messaging."""
    inspect.stack = mode


def error(message, target):
    """Print an error to the target."""
    ocolored(message, target, 'red')


def info(message, target):
    """Print an info message to the target"""
    ocolored(message, target, 'black')


def ocolored(message, target, color):
    """Print an colored message to the target if it is supported."""
    if target.colored:
        target.outstream.write(
            colored(inspect.stack()[1].function + ": " + message, color))
    else:
        target.outstream.write(inspect.stack()[1].function.upper() + ": " + message)
    target.outstream.flush()
