from typing import Union
import os.path


class PathHandler:
    def __init__(self, input_path: str, output_path: str = None):
        self.__input_path: str = input_path
        self.__output_path: str = output_path

    @property
    def input_path(self) -> str:
        return self.__input_path

    @input_path.setter
    def input_path(self, input_path: str) -> None:
        self.input_path = input_path
        
    @property
    def output_path(self) -> str:
        return self.__output_path

    @output_path.setter
    def output_path(self, output_path: Union[str, None]) -> None:
        if output_path != None:
            self.output_path = output_path
        if output_path == None:
            input_path_dir = os.path.dirname(self.input_path)
            self.output_path = input_path_dir
        