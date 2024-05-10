"""comprehensions demo"""

from itertools import islice
from pathlib import Path
from random import randint
import csv


def list_comprehension() -> None:
    """list comprehension"""

    even_nums = [x for x in range(10) if (x % 2 == 0)]
    print(even_nums)

    double_nums = [x * 2 for x in range(2)]
    print(double_nums)


def dictionary_comprehension() -> None:
    """dictionary comprehension"""

    food_groups = None

    with Path("data", "food.csv").open(encoding="UTF-8") as food_file:
        food_groups = {
            food[1]: food[0] for food in csv.reader(islice(food_file, 1, 6))
        }

    print(food_groups)


def set_comprehension() -> None:
    """set comprehension"""

    nums = [randint(0, 9) for _ in range(50)]

    unique_nums = {num for num in nums}

    print(nums)
    print(unique_nums)
    print(type(unique_nums))


def generator_comprehension() -> None:
    # example map (x * 3) and filter (x % 2 == 0)
    triple_nums = (x * 3 for x in range(10) if x % 2 == 0)

    print(type(triple_nums))
    print(list(triple_nums))


def main() -> None:
    # list_comprehension()
    # dictionary_comprehension()
    # set_comprehension()
    generator_comprehension()


if __name__ == "__main__":
    main()
