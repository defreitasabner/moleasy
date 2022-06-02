from abc import ABCMeta, abstractmethod


class FileManager(meta=ABCMeta):

    @staticmethod
    @abstractmethod
    def read_file():
        ...

    @staticmethod
    @abstractmethod
    def write_file():
        ...

