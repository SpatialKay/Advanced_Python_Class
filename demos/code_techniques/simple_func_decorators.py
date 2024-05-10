from typing import Callable, Any


def wrapper(fn: Callable[..., Any]) -> Callable[..., Any]:
    print("wrapper executed")

    def inner(*args: Any, **kwargs: Any) -> Any:
        print("inner executed")
        print("Before")
        result = fn(*args, **kwargs)
        print(f"Result in Inner: {result}")
        print("After")

        return result

    return inner


@wrapper
def do_it(a: int, b: int) -> int:
    return a + b


# wrapped_do_it = wrapper(do_it)
# print(wrapped_do_it(1, 2))

print(do_it(1, 2))
