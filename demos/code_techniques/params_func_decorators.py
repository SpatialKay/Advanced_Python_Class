from typing import Callable, Any


class App:
    def __init__(self) -> None:
        self.__routes: dict = {}

    def print_routes(self) -> None:
        print(self.__routes)

    def route(self, path: str) -> Callable:
        print(f"calling route: {path}")

        def wrapper(fn: Callable[..., Any]) -> Callable[..., Any]:
            print(f"calling wrapper: {path}")
            self.__routes[path] = fn

            def inner(*args: Any, **kwargs: Any) -> Any:
                print(f"path: {path}")
                return fn(*args, **kwargs)

            return inner

        return wrapper

    def run(self, path: str, *args: Any, **kwargs: Any) -> Any:
        fn = self.__routes[path]
        return fn(*args, **kwargs)


app = App()


@app.route("/add")
def add(a: int, b: int) -> int:
    return a + b


@app.route("/sub")
def subtract(a: int, b: int) -> int:
    return a - b


app.print_routes()


print(app.run("/add", 1, 2))
print(app.run("/sub", 1, 2))
