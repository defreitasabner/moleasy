from abc import ABCMeta, abstractmethod
from typing import List, Dict


class FileManager(metaclass=ABCMeta):
    '''
    File Manager
    ===
    Abstract class to represent all file managers. There is one file manager to each main file format: `fasta`, `phyllip`, and `nexus`.
    '''

    @staticmethod
    @abstractmethod
    def read_file(input_path: str) -> List[Dict[str, str]]:
        ...

    @staticmethod
    @abstractmethod
    def write_file(output_path: str, output_data: List[Dict[str, str]]) -> None:
        ...

