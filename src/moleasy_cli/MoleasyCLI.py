from typing import List, Tuple

from src.exceptions.InvalidMethodError import InvalidMethodError
from src.exceptions.MissingArgsError import MissingArgsError
from src.exceptions.TooMuchArgsError import TooMuchArgsError
from src.path_handler.PathHandler import PathHandler


class MoleasyCLI:
    def __init__(self, args: List[str]):
        self.__args: List[str] = args

    @property
    def args(self) -> List[str]:
        return self.__args

    @args.setter
    def args(self, new_args: List[str]) -> None:
        self.__args = new_args
    
    def start(self) -> Tuple[str]:
        
        if len(self.args) >= 4:
        
            method = self.args[1] # method: convert or concat
            
            if method == 'convert':
                if len(self.args) > 5:
                    raise TooMuchArgsError("Method 'convert' expects maximum of 5 args: script path, method, input file path, required output ('fasta', 'phyllip', or 'nexus'), and output file path (optional)")
                input_path = self.args[2] # path to input file
                required_output = self.args[3] # fasta, phyllip or nexus
                output_path = None # optional
                if len(self.args) == 5:
                    output_path = self.args[4] # optional
                if output_path == None:
                    path_handler = PathHandler(input_path, required_output)
                    output_path = path_handler.output_path
                return (method, input_path, required_output, output_path)

            elif method == 'concat':
                pass

            else:
                raise InvalidMethodError(f"Unexpected method '{method}'. Please, try one of those methods: 'convert' or 'concat'.")
        
        else:
            raise MissingArgsError('At least 4 arguments are required: script path, method, input file path, required output (convert) or input file path 2 (concat).')
