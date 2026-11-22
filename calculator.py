"""PyJen004 - simple addition program (832208 DevOps, Jenkins #4)."""
import sys


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def main(argv):
    if len(argv) == 2:
        a, b = float(argv[0]), float(argv[1])
    else:
        a, b = 5, 3
    print(f"{a} + {b} = {add(a, b)}")


if __name__ == "__main__":
    main(sys.argv[1:])
