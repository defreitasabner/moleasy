import os.path


class PathHandler:
    def __init__(self, input_path: str, required_output: str, output_path: str = ''):
        self.__input_path: str = input_path
        self.__required_output: str = required_output
        self.__output_path: str = self.empty_output_path_checker(output_path)

    @property
    def input_path(self) -> str:
        return self.__input_path

    @input_path.setter
    def input_path(self, new_input_path: str) -> None:
        self.__input_path = new_input_path

    @property
    def required_output(self) -> str:
        return self.__required_output

    @required_output.setter
    def required_output(self, new_required_output: str) -> None:
        self.__required_output: str = new_required_output

    @property
    def output_path(self) -> str:
        return self.__output_path

    @output_path.setter
    def output_path(self, new_output_path: str) -> None:
            self.__output_path = self.empty_output_path_checker(new_output_path)

    def empty_output_path_checker(self, output_path: str) -> str:
        if output_path == '':
            input_filename, _ = os.path.basename(self.input_path).split('.')
            input_path_dir = os.path.dirname(self.input_path)
            output_extension = None
            if self.required_output == 'fasta':
                output_extension = '.fasta'
            elif self.required_output == 'phyllip':
                output_extension = '.phy'
            elif self.required_output == 'nexus':
                output_extension = '.nex'
            output_filename = f'{input_filename}{output_extension}'
            new_output_path = os.path.join(input_path_dir, output_filename)
            print('Output path not given. Redefine output directory path as the same of input file.')
            return new_output_path
        else:
            return output_path
