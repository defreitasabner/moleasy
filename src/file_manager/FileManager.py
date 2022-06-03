from abc import ABC, abstractmethod
from typing import List, Dict


class FileManager(ABC):

    @staticmethod
    @abstractmethod
    def read_file(input_path: str):
        ...

    @staticmethod
    @abstractmethod
    def write_file(output_path: str, output_data: List[Dict[str, str]]):
        ...

