from abc import ABC, abstractmethod


class FileManager(ABC):

    @staticmethod
    @abstractmethod
    def read_file(path: str):
        ...

    @staticmethod
    @abstractmethod
    def write_file(path: str):
        ...

