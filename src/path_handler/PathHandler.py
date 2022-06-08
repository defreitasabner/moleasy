from typing import Union
import os.path


class PathHandler:
    def __init__(self, input_path: str, queried_output: str, output_path: str = ''):
        self.__input_path: str = input_path
        self.__queried_output: str = queried_output
        self.__output_path: str = self.empty_output_path_checker(output_path)

    @property
    def input_path(self) -> str:
        return self.__input_path

    @input_path.setter
    def input_path(self, input_path: str) -> None:
        self.input_path = input_path

    @property
    def queried_output(self) -> str:
        return self.__queried_output

    @queried_output.setter
    def queried_output(self, new_queried_output: str) -> None:
        self.queried_output: str = new_queried_output

    @property
    def output_path(self) -> str:
        return self.__output_path

    @output_path.setter
    def output_path(self, new_output_path: str) -> None:
            self.output_path = self.empty_output_path_checker(new_output_path)

    def empty_output_path_checker(self, output_path: str) -> str:
        if output_path == '':
            input_filename, _ = os.path.basename(self.input_path).split('.')
            input_path_dir = os.path.dirname(self.input_path)
            output_extension = None
            if self.queried_output == 'fasta':
                output_extension = '.fasta'
            elif self.queried_output == 'phyllip':
                output_extension = '.phy'
            elif self.queried_output == 'nexus':
                output_extension = '.nex'
            output_filename = f'{input_filename}{output_extension}'
            new_output_path = os.path.join(input_path_dir, output_filename)
            print('Output path not given. Redefine output directory path as the same of input file.')
            return new_output_path
        else:
            return output_path
