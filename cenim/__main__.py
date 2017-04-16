import sys

from runnables.train import run as train


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]
    if len(args) == 0:
        train()

    print("This is the main routine.")
    print("It should do something interesting.")

if __name__ == "__main__":
    main()
