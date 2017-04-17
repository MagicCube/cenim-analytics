import sys

from runnables.train import run as train


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]
    if len(args) == 0:
        train()
    elif args[0] == 'train':
        train()

if __name__ == "__main__":
    main()
