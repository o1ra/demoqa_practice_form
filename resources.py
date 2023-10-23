import os


def path(file_name):
    return str(os.path.abspath(os.path.join(os.path.dirname(__file__), f'tests/resources/img/{file_name}')))
