

person = { "first_name": "Kay", "last_name": "Ige"}

person2 = {"age": 33, **person}

print(person2)

# **other = person2 

# there is no concept of packing in Dictionary. ** is for unpacking dictionary

def do_it(a: str, b: str, c:str) -> None:
    print(a, b, c)

do_it(**{"a": "1", "b": "2", "c": "3"})

