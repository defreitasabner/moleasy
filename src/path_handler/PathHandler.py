from typing import Union
import os.path


class PathHandler:
    def __init__(self, input_path: str, queried_output: str, output_path: str = None):
        self.__input_path: str = input_path
        self.__queried_output: str = queried_output
        self.__output_path: str = output_path

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
    def output_path(self, output_path: Union[str, None]) -> None:
        if output_path != None:
            self.output_path = self.define_output_path_as_input_path()
        if output_path == None:
            input_path_dir = os.path.dirname(self.input_path)
            self.output_path = input_path_dir

    def define_output_path_as_input_path(self) -> str:
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
        output_path = os.path.join(input_path_dir, output_filename)
        return output_path
