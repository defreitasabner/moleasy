from abc import ABCMeta, abstractmethod


class FileManager(meta=ABCMeta):

    @staticmethod
    @abstractmethod
    def read_file(path: str):
        ...

    @staticmethod
    @abstractmethod
    def write_file(path: str):
        ...

