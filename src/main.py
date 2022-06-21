import sys
from typing import List

from moleasy_cli.MoleasyCLI import MoleasyCLI

def main() -> None:

    args: List[str] = sys.argv

    MoleasyCLI(args)


if __name__ == '__main__':
    main()
