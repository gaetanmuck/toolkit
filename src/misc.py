import datetime


def percent(nb):
    """Format the number sent into a % number."""
    the_number = round(100 * nb, 2)
    the_string = '{: >6.2f}%'.format(the_number)
    return the_string


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