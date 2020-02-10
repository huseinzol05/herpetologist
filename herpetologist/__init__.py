from functools import wraps
from typing import Dict, List, Tuple
import inspect

__version__ = '0.0.6'


def recursive_check(v, t):
    if '__module__' in dir(t):
        if t.__module__ != 'typing':
            return isinstance(v, t)
    else:
        return isinstance(v, t)

    args = t.__args__
    if args:
        origin = isinstance(v, t.__origin__)

        if isinstance(v, (tuple, list, dict, set)):
            if len(v) == len(args) and len(args) != 1:
                return all(
                    [recursive_check(v[i], args[i]) for i in range(len(v))]
                )

        if 'typing.' in str(args[0]):
            return origin and all(
                [recursive_check(v[i], args[0]) for i in range(len(v))]
            )
        else:
            if t.__origin__ in [dict, Dict] and origin:
                key_type = args[0]
                value_type = args[1]
                return all(
                    [recursive_check(k, key_type) for k in v.keys()]
                ) and all([recursive_check(k, value_type) for k in v.values()])
            else:
                if not isinstance(v, (tuple, list, dict, set)):
                    return False
                if len(args) == 1:
                    return origin and all(
                        [recursive_check(p, args[0]) for p in v]
                    )
                if len(v) != len(args):
                    return False
                if len(args) == len(v):
                    return origin and all(
                        [recursive_check(v[i], args[i]) for i in range(len(v))]
                    )
    else:
        return isinstance(v, t)


def proper_text(string):

    replaced = ['typing.', '<class ', '>', '__main__.']
    for r in replaced:
        string = string.replace(r, '')
    return string


def check_type(func):
    fullspec = inspect.getfullargspec(func)
    parameters = fullspec.args
    annotations = fullspec.annotations

    @wraps(func)
    def check(*args, **kwargs):
        def nested_check(v, p):
            t = annotations.get(p)
            if t:
                if not recursive_check(v, t):
                    raise TypeError(
                        proper_text(f'type of argument "{p}" must be {t}')
                    )

        for v, p in zip(args, parameters):
            nested_check(v, p)

        for p, v in kwargs.items():
            nested_check(v, p)

        return func(*args, **kwargs)

    return check
