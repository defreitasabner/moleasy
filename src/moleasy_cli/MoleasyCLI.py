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
    
    def start(self):
        
        method = self.args[1] # method: convert or concat
        
        if method == 'convert' and len(self.args) >= 4:
            input_path = self.args[2] # path to input file
            required_output = self.args[3] # fasta, phyllip or nexus
            output_path = None # optional
            if len(self.args) == 5:
                output_path = self.args[4] # optional

            return method, input_path, required_output, output_path

        elif method == 'concat' and len(self.args) >= 4:
            ...

        elif method != 'convert' and method != 'concat':
            raise Exception

        elif len(self.args) < 4:
            raise Exception