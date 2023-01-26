import os


def create_file(path, content):
    """Create a new file. If it aleady exists, delete it and create it."""

    if os.path.exists(path): os.remove(path)

    f = open(path, 'w')
    f.write(content)
    f.close()


def read_file(path):
    """Read the full content of a file"""

    f = open(path, 'r')
    content = f.read()
    f.close()
    return content


def read_lines(path):
    """Read the content of a file, as an array, each element being a line."""

    f = open(path, 'r')
    lines = f.readlines()
    f.close()
    return lines


def append_file(path, content):
    """Append to an existing file."""

    f = open(path, 'a')
    f.write(content)
    f.close()