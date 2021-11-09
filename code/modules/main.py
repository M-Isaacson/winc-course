import this
import time
import math
from datetime import datetime
import sys
import greet

# Do not modify these lines
__winc_id__ = "78029e0e504a49e5b16482a7a23af58c"
__human_name__ = "modules"

# Add your code after this line
def wait(seconds: int) -> None:
    """
    Makes the computer wait for a number of seconds

    Parameters
    ----------
    seconds : int
        The time in seconds to wait
    """

    time.sleep(seconds)


def my_sin(sine_of: float) -> float:
    """
    Calculates the sine of a number(float)

    Parameters
    ----------
    sine_of : float
        The number as float from which the sine is calculated
    """

    return math.sin(sine_of)


def iso_now() -> str:
    """
    Returns the current date and time in ISO-8601
    """

    return f"{datetime.now().strftime('%Y-%m-%d')}T{datetime.now().strftime('%H:%M')}"


def platform():
    """
    Shows which platform is in use
    """
    return sys.platform


def supergreeting_wrapper(name: str) -> str:
    """
    Returns an awesome personal supergreet.

    Parameters
    ----------
    name : str
        Name of the person to greet

    Returns
    -------
    str
        The super awesome greeting thru a module.
    """
    return greet.supergreeting(name)
