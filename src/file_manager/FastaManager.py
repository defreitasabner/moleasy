from FileManager import FileManager


class FastaManager(FileManager):

    @staticmethod
    def read_file(path: str):
        with open(path, mode='r', encoding='utf-8'):
            ...

    @staticmethod
    def write_file(path: str):
        with open(path, mode='w', encoding='utf-8'):
            ...

