import re

def snake_case(name):
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", str(name))
    name = re.sub(r"[^A-Za-z0-9]+", "_", name)
    return name.strip("_").lower()
