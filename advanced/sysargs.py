import sys

args = [
    "test",
    "temp",
    "go"
]

try:
    if str(sys.argv[1]) == "go":
        print("My fav lang")
    else:
        print("Hey") if str(sys.argv[1]) in args else print("yeH", sys.argv)
except IndexError:
    pass
