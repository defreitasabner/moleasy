import sys
from typing import List

from moleasy_cli.MoleasyCLI import MoleasyCLI
from moleasy_gui.MoleasyGUI import MoleasyGUI

def main() -> None:

    args: List[str] = sys.argv

    if len(args) > 2:
        MoleasyCLI(args)

    elif (len(args) > 2) and ('gui' in args):
        MoleasyGUI()

    else:
        raise Exception('If you want to use Moleasy via CLI, use more arguments. If you want to use it via GUI (Graphic Interface) use single arg: "gui".')


if __name__ == '__main__':
    main()
