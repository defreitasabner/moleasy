from abc import ABCMeta, abstractmethod
from typing import List, Dict


class FileManager(metaclass=ABCMeta):
    """
    File Manager
    ===
    Abstract class to represent all file managers. There is one file manager to each main file format: `fasta`, `phyllip`, and `nexus`.
    """
    def __init__(self):
        self.data = None

    @abstractmethod
    def read_file(self, input_path: str) -> None:
        """
        read_file()
        ---
        Open a specific file, with extension based on file manager type, and read all data within it. Store all readed data in a list of dictionaries and return it.
        """
        ...

    @abstractmethod
    def write_file(self, output_path: str, output_data: List[Dict[str, str]]) -> None:
        """
        write_file()
        ---
        Write all data stored in a new file. The output file has the extension of the file manager type.
        """
        ...

