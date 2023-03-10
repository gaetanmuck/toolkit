import datetime
import threading


def percent(nb):
    """Format the number sent into a % number."""
    the_number = round(100 * nb, 2)
    the_string = '{: >6.2f}%'.format(the_number)
    return the_string


def convert_bytes(size):
    """Convert bytes to KB, or MB or GB"""
    for x in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1000.0: return "%3.1f %s" % (size, x)
        size /= 1000.0


def now():
    """Get current timestamp in seconds (number)."""
    return  int(datetime.datetime.now().timestamp())


def format_time(time):
    """Transform a number of second into a human readable string."""

    # Calculations
    hours = int(time / 3600)
    minutes = int((time - (3600 * hours)) / 60)
    seconds = int(round(time - (60 * minutes + 3600 * hours)))

    # Stringify to right format
    hours = '{:0>2.0f}'.format(hours)
    minutes = '{:0>2.0f}'.format(minutes)
    seconds = '{:0>2.0f}'.format(seconds)

    return f"[{hours}h{minutes}'{seconds}]"


def set_interval(func, sec):
    """Run the given function every given seconds."""
    
    def func_wrapper():
        set_interval(func, sec) 
        func()  

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t