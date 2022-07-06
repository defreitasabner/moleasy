import sys
from typing import List, Tuple

from src.moleasy_cli.MoleasyCLI import MoleasyCLI
from src.moleasy_gui.MoleasyGUI import MoleasyGUI
from src.exceptions.InitializeError import InitializeError

def main() -> None:

    args: List[str] = sys.argv

    if len(args) > 2:
        moleasy = MoleasyCLI(args)
        moleasy.start()

    elif (len(args) == 2) and ('gui' in args):
        moleasy = MoleasyGUI()
        moleasy.start()

    else:
        raise InitializeError('If you want to use Moleasy via CLI, use more arguments. If you want to use it via GUI (Graphic Interface) use single arg: "gui".')


if __name__ == '__main__':
    main()
