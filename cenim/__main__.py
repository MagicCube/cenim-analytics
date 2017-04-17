import sys

from runnables.test import run as test
from runnables.train import run as train


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]
    if len(args) == 0:
        train()
    elif args[0] == 'train':
        train()
    elif args[0] == 'test':
        test()

if __name__ == "__main__":
    main()
