import datetime


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
