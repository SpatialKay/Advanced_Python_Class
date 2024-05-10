from typing import TypedDict
from dataclasses import dataclass

command = input("Enter a command > ")
operand = float(input("Enter an operand > "))

# Equivalent of a switch statement

# match command:
#     case "add":
#         print(operand + operand)
#     case "subtract":
#         print(operand - operand)
#     case "multiply":
#         print(operand * operand)
#     case "divide":
#         print(operand / operand)
#     case _:
#         print("Invalid command")

# Multiple values match a case

# match command:
#     case "add" | "subtract":
#         print(f"do {command} numbers")
#     case _:
#         print("Invalid command")

# Conditional if statements in a case

# match command:
#     case "divide" if operand == 0:
#         print("Cannot divide by zero")
#     case "add" | "subtract" | "multiply" | "divide":
#         print(f"do {command} numbers")
#     case _:
#         print("Invalid command")

# Match list objects and capture values in variables

# history = [["subtract", 10], ["add", 20], ["multiply", 30], ["divide", 40]]

# for operation in history:
#     match operation:
#         case ["add", value]:
#             print(f"Adding {value}")
#         case ["subtract", value]:
#             print(f"Subtracting {value}")
#         case ["multiply", value]:
#             print(f"Multiplying {value}")
#         case ["divide", value]:
#             print(f"Dividing {value}")

# Match case with dictionary objects

# class HistoryEntry(TypedDict):
#     id: int
#     operation: str
#     value: int


# history2: list[HistoryEntry] = [
#     {"id": 1, "operation": "subtract", "value": 10},
#     {"id": 2, "operation": "add", "value": 20},
#     {"id": 3, "operation": "multiply", "value": 30},
#     {"id": 4, "operation": "divide", "value": 40},
# ]

# for operation2 in history2:
#     match operation2:
#         case {"id": op_id, "operation": "add", "value": op_value}:
#             print(f"Op Id: {op_id}: Adding {op_value}")

# Match case with regular objects


@dataclass
class HistoryEntry2:
    id: int
    operation: str
    value: int


history3: list[HistoryEntry2] = [
    HistoryEntry2(1, "subtract", 10),
    HistoryEntry2(2, "add", 20),
    HistoryEntry2(3, "multiply", 30),
    HistoryEntry2(4, "divide", 40),
]

for operation3 in history3:
    match operation3:
        case HistoryEntry2(op_id, "add", op_value):
            print(f"Op Id: {op_id}: Adding {op_value}")
        case HistoryEntry2(op_id, "subtract", op_value):
            print(f"Op Id: {op_id}: Subtracting {op_value}")
        case HistoryEntry2(op_id, "multiply", op_value):
            print(f"Op Id: {op_id}: Multiplying {op_value}")
        case HistoryEntry2(op_id, "divide", op_value):
            print(f"Op Id: {op_id}: Dividing {op_value}")
        case _:
            print("Invalid operation")
