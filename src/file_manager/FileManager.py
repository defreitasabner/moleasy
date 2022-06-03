from abc import ABC, abstractmethod
from typing import List, Dict

class FileManager(ABC):

    @staticmethod
    @abstractmethod
    def read_file(path: str):
        ...

    @staticmethod
    @abstractmethod
    def write_file(path: str, data: List[Dict[str, str]]):
        ...

