"""PyJen004 - simple addition program (832208 DevOps, Jenkins #4)."""
import sys


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def fmt(x):
    """Show whole numbers without .0 (30.0 -> 30)."""
    return str(int(x)) if float(x).is_integer() else str(x)


def main(argv):
    if len(argv) == 2:
        a, b = float(argv[0]), float(argv[1])
    else:
        a, b = 5, 3
    print(f"{fmt(a)} + {fmt(b)} = {fmt(add(a, b))}")


if __name__ == "__main__":
    main(sys.argv[1:])
