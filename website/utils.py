from itertools import cycle
from random import choice


def get_random_string(length) -> str:
    letters = ('qwrtpsdfghjklzxcvbnm', 'eyuioa')
    cycle_ = zip(cycle(letters), range(length))
    return ''.join(choice(letter) for letter, _ in cycle_)


def get_random_string2(length) -> str:
    letters = 'qwrtpsdfghjklzxcvbnmeyuioa0123456789!@#$%^&*()_+=-|'
    return ''.join(choice(letters) for _ in range(length))


def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in range(0, len(l), n):
        yield l[i:i+n]


def allow_post_only(func):
    def func_wrapper(request):
        if request.method == 'POST':
            return func(request)
    return func_wrapper


class Struct:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return self.__dict__ != other.__dict__