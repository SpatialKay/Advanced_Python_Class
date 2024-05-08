from typing import Any

# def do_it(a: Any = None, b: Any = None, c: Any = None) -> None:
#     print(a, b, c)


# do_it(["a", "b", "c"])


def do_it(a: Any = None, b: Any = None, *c: Any) -> None:
    print(a, b, c)


do_it(1, 2, 3, 4, 5, 6, 7)

# asterisks applied to the argument is the unpacking.
# asterisks applied to the parameters is the packing function