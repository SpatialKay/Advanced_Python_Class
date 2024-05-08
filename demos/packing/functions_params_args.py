from typing import Any

# *args - will collect the positional arguments
# **kwargs - will collect the keyword arguments


def do_it(*args: list[Any], **kwargs: dict[str, Any]) -> None:
    print(args)
    print(kwargs)

# 1, 2, 3, 4 are positional arguments
# a, b, c are keyword arguments
