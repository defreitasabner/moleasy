from typing import List
import sys


class MoleasyCLI:
    def __init__(self, args: List[str]):
        self.__args: List[str] = args

    @property
    def args(self) -> List[str]:
        return self.__args

    @args.setter
    def args(self, new_args: List[str]) -> None:
        self.__args = new_args
    
    def start(self, args):
        ...