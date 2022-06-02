from abc import ABCMeta, abstractmethod


class FileManager(meta=ABCMeta):

    @abstractmethod
    def read_file(self):
        ...

    @abstractmethod
    def write_file(self):
        ...

