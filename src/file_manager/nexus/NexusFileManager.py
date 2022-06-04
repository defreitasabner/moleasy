from typing import List, Dict

from ..FileManager import FileManager


class NexusFileManager(FileManager):
    
    @staticmethod
    def read_file(input_path: str):
        ...

    @staticmethod
    def write_file(output_path: str, output_data: List[Dict[str, str]]):
        ...